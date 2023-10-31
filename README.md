keyword_finder
==============================

This project objective is to isolate keyword in some paragraphs in order to fasten the reading of docx or txt files. It will generate a unique docx file containing all the extracted paragraphs. It can also be used to extract contextual sentences in order to provide examples in training an NLP Model (please see my other repos on [spacy](https://github.com/JonathanGarson/spacy_NER_2023), on [CamemBERT](https://github.com/JonathanGarson/CamemBERT_NER_2023) or [GPT](https://github.com/JonathanGarson/gpt_2023)).

There is no need to use the code as the app has been [deployed](https://streamlitkeyword.lab.sspcloud.fr/) online.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   |── raw            <- The original, immutable data dump.
    |   └── text           <- Texts used for training.
    |       ├── docx       <- docx documents
    |       └── txt        <- txt documents used for traning (converted from docx documents).
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── treatments     <- Scripts to treat docx text files.
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

***
## How to run the code 

You can download the data on [Legifrance](https://www.legifrance.gouv.fr/) via the download.py script, it will webscrapped data from a list of URL that you can find in the raw data, in the file : full_data_link_legifrance.xlsx (for now only available on my [CamemBERT](https://github.com/JonathanGarson/CamemBERT_NER_2023/tree/main/data/raw) repo). Then treat them with the cleaning.py script. You need to upload a xlsx file containing all the keywords you're looking for and finally run extract_highlight_merged.py to obtain the final outputs.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
