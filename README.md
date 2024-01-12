---
license: cc0-1.0
language:
- fi
- sv
- en
pipeline_tag: text-classification
thumbnail: https://raw.githubusercontent.com/NatLibFi/FintoAI/main/ai.finto.fi/static/img/finto-ai-social.png
tags:
- glam
- lam
- subject indexing
- annif
---
# FintoAI-data-YSO
This repository is for the Annif projects with the
[YSO vocabulary](https://finto.fi/yso)
used at the [Finto AI service](https://ai.finto.fi/).
The current models were published there 2023-09-04.
The models have been trained on Python 3.8.10 with [Annif](https://annif.org) version 1.0.0.
See [projects.toml](projects.toml) for the configurations of the models.

This repository is mirrored from GitHub to the 🤗 Hugging Face Hub;
the GitHub repository does not contain the model files, but only the configurations for the projects and the DVC pipeline, see below.

The training corpora that are public can be found from the [Annif-corpora repository](https://github.com/NatLibFi/Annif-corpora/).

The [notebook](/repository-metrics-analysis/analyse-theseus-tietolinja.ipynb) contains analysis of Annif suggestions in [Theseus repository](https://www.theseus.fi/).

## Models
The downloadable directories for projects and vocabularies are stored in the
[`/data`](https://huggingface.co/juhoinkinen/FintoAI-data-YSO/tree/main/data)
directory of this repository in the 🤗 Hugging Face Hub.

## DVC pipeline
The projects are trained and evaluated using a [DVC (Data Version Control) pipeline](https://dvc.org/doc/start/data-management/data-pipelines) defined in [dvc.yaml](./dvc.yaml).

The pipeline takes care of

1. installing Annif in a venv,
2. loading the vocabulary,
3. training the projects,
4. evaluating the projects.

When the necessary vocabulary and training corpora are in place the pipeline can be run using the command

    dvc repro

For more information about using DVC with Annif projects see the [DVC exercise of Annif tutorial](https://github.com/NatLibFi/Annif-tutorial/blob/master/exercises/OPT_dvc.md).
