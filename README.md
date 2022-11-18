# OpenAlex concept tagger

Code adapted and modified from: https://github.com/ourresearch/openalex-concept-tagging

---

## Model

I am using the V2 model which can be downloaded from AWS using its CLI:
https://aws.amazon.com/cli/

Make sure to create an account first and then configure the CLI like this:

```bash
aws configure
```

Now run the following to download the models.

```bash
aws s3 cp s3://openalex-concept-tagger-model-files/ . --recursive
```

We will only be using V2 so make sure to place it under */model* within this directory.

---

## Tagger

The script runs the concept tagger on publication metadata (e.g., Pure exports).

Make sure the file(s) (.csv) is/are in */input*, the tagged file(s) will then be placed under */output*.

Any input file needs to contain the following columns and content:
* title
* abstract
* journal
* doc_type: can be one of
    * *Contribution to Journal - Article*
    * everything else will be considered of type book

Run the tagger like this:

```bash
python -m tagger
```

Make sure to have installed and activated an environment containing the libraries specified in *requirements.txt*