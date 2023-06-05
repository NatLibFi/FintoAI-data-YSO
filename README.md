# FintoAI-data-YSO

Configurations for maintaining the Annif projects with YSO vocabulary used at [Finto AI service](ai.finto.fi/) and the [analysis notebook](/repository-metrics-analysis/analyse-theseus-tietolinja.ipynb) of Annif suggestions in [Theseus repository](https://www.theseus.fi/).

The projects are trained and evaluated using a [DVC (Data Version Control) pipeline](https://dvc.org/doc/start/data-management/data-pipelines) defined in [dvc.yaml](/dvc.yaml).
The training corpora that are public can be found from [Annif-corpora repository](https://github.com/NatLibFi/Annif-corpora/).

The pipeline takes care of 

1. installing Annif in a venv,
2. loading YSO vocabulary,
3. training the projects,
4. evaluating the projects.

When the necessary vocabulary and training corpora are in place the pipeline can be run using by the command

    dvc repro
    
For more information about using DVC with Annif projects see the [DVC exercise of Annif tutorial](https://github.com/NatLibFi/Annif-tutorial/blob/master/exercises/OPT_dvc.md).
