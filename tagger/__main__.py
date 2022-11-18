from tagger import predictor
import pandas as pd
import json
import glob
import os


def main():
    
    for filename in glob.glob(os.path.join('input', '*.csv')):
        
        # make path os-specific
        filename = os.path.normpath(filename)

        print('running tagger for', filename)
        data = pd.read_csv(filename)
        
        # type mapping pure-openalex
        def map_type(pure_type):
            if pure_type=="Contribution to Journal - Article": 
                return "Journal"
            else:
                return "BookChapter"


        input_dicts = []
        for index, row in data.iterrows():

            input_dict = {
                "title": row["title"],
                "doc_type": map_type(row["doc_type"]),
                "journal": row["journal"],
                "abstract": row["abstract"], 
                "inverted_abstract": False,
            }
            input_dicts.append(input_dict)

        # run tagger on batches (to avoid memory overflow)
        results = []
        n = 20
        for i in range(0, len(input_dicts), n):
            subset = input_dicts[i:i+n]
            result_json = predictor.predict(json.dumps(subset))
            results.extend(json.loads(result_json))

        # lists to string (for text output)
        results_df = pd.DataFrame(results)
        results_df = results_df.applymap(lambda x: '|'.join([str(i) for i in x]) if type(x)==list else x)

        # merge with input data
        merged_df = pd.concat([data, results_df], axis=1)

        merged_df.to_csv(
            os.path.join('output', os.path.basename(filename)), 
            index=False)


if __name__ == '__main__':
    main()
