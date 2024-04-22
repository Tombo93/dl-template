Deep Learning Template Package
==============================

Install
------------
    $ make requirements
    
Set up project & download data
------------
    $ make data

Run experiments
------------
    $ make experiment 



Project Organization
------------

├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── config.yaml
│   ├── data
│   │   └── data.yaml
│   ├── hparams
│   │   └── params.yaml
│   ├── preprocessing
│   │   └── preprocessing.yaml
│   └── task
│       └── task.yaml
├── config.py
├── docs
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── environment.yml
├── models
├── notebooks
│   ├── isic_diagnosis.ipynb
│   ├── isic_img.ipynb
│   ├── plot.ipynb
│   ├── predict_poison_labels.ipynb
│   └── trigger_design.ipynb
├── pyproject.toml
├── references
├── reports
│   └── figures
├── setup.cfg
├── setup.py
├── src
│   ├── backdoor
│   │   ├── cifar.py
│   │   ├── gen_adv_dataset.py
│   │   ├── label_consistent.py
│   │   ├── simple.py
│   │   └── trigger
│   │       ├── 2x2_trigger.png
│   │       ├── 4x4_trigger.png
│   │       ├── cifar10.png
│   │       ├── cifar_1.png
│   │       └── isic-base.png
│   ├── data
│   │   ├── create_npz.py
│   │   ├── dataloader.py
│   │   ├── dataset.py
│   │   ├── download_isic.py
│   │   ├── make_cifar10.py
│   │   ├── make_data_dirs.py
│   │   ├── make_isic.py
│   │   ├── make_isic_metadata.py
│   │   ├── manager.py
│   │   ├── meta_dist.py
│   │   └── notinuse.py
│   ├── models
│   │   ├── cifar_backdoor_main.py
│   │   ├── genomic_main.py
│   │   ├── isic_backdoor_main.py
│   │   ├── isic_main.py
│   │   └── models.py
│   ├── py.typed
│   ├── utils
│   │   ├── custom_transforms.py
│   │   ├── evaluation.py
│   │   ├── experiment.py
│   │   ├── logger.py
│   │   ├── metrics.py
│   │   ├── optimizer.py
│   │   └── training.py
│   └── visualization
│       ├── plot_cifar.py
│       ├── plot_confusion_matrix.py
│       └── plot_isic.py
├── tests
│   └── __init__.py
└── tox.ini

19 directories, 62 files
