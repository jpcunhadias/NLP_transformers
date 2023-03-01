# Text Classification of Bank Call Transcripts

This is a Python project that demonstrates how to use natural language processing (NLP) techniques for text classification of bank call transcripts. It uses primarily transformers models and NLP techniques to classify bank call transcripts into categories such as account inquiries, customer complaints, and new account requests.

It uses a dataset of bank call transcripts, which includes various types of customer inquiries and requests.

## Future updates

- To apply other deep learning models in order to compare performances
- To develop automated tests
- [To build data preprocessing pipelines using Kedro](https://kedro.readthedocs.io/en/stable/index.html)

## Referencies

 - [Blueprints with text analytics using python](https://www.amazon.com.br/Blueprints-Text-Analysis-using-Python/dp/149207408X)
 - [NLP with pytorch](https://www.amazon.com.br/Natural-Language-Processing-PyTorch-Applications-ebook/dp/B07N17TMFH)
 - [Introduction to Transformers for NLP](https://www.amazon.com/Introduction-Transformers-NLP-Hugging-Problems/dp/1484288432)
 - [NLP with transformers](https://www.amazon.com.br/Natural-Language-Processing-Transformers-Applications/dp/1098103246)
 - [Transformers for Natural Language Processing](https://www.amazon.com.br/Transformers-Natural-Language-Processing-architectures/dp/1803247339)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
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
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
