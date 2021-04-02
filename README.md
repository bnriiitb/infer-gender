# Infer Gender
---

Infers gender from the indian first name or full name.



## Installation
---
### Using pip
[![PyPi Version](https://badge.fury.io/py/infer-gender.svg)](https://pypi.org/project/infer-gender/)

You can install using the pip package manager by running
```sh
pip install infer-gender
```

Alternatively, you could install the latest version directly from Github:
```sh
pip install https://github.com/bnriiitb/infer-gender/infer-gender/archive/master.zip
```

### Using conda

You can install using the conda package manager by running
```sh
conda install -c conda-forge infer-gender
```
### From source

Download the source code by cloning the repository or by pressing 'Download ZIP' on this page.

Install by navigating to the proper directory and running:
```sh
python setup.py install
```


## Usage
---

```python

from infer_gender import GenderPredictor
gp = GenderPredictor()

sample_names = ['katrina kaif','narendra modi','naga budigam','james bond','samantha']
predicted_genders = gp.predict_gender(sample_names)

for name,pred_gender in zip(sample_names,predicted_genders):
    print('{} --> {}'.format(name,pred_gender))
```

```text
katrina kaif --> Female
narendra modi --> Male
naga budigam --> Male
james bond --> Male
samantha --> Female

```
