# PyPI Cookiecutter
A cookiecutter project to generate projects slated to become PyPI packages. The
generated CI ensures that the package is ready to deploy to both the
[test.pypi.org](https://test.pypi.org) and the regular [pypi.org](https://pypi.org)
indexes.

The project is generated using some inputs, it is recommended to generate
a project from a virtualenvironment to avoid having Cookiecutter installed
globally.

**Note:** The template will generate a containing folder for the project,
if you execute this from within a folder it will be nested.

## Usage
To create a project run the following:

```
pip install -r requirements.txt
cd <your parent folder location>
cookecutter https://github.com/mattdood/pypi-cookiecutter.git
```

## Generated content
* GitHub CI for PyPI releases, tests, and linting
    * **Note:** The project requires GitHub secrets to be added for PyPI access.
* Readme with badges and project usage steps
* MIT license
* Requirements files for local dev and regular installation
* Pytest setup (conftest and tests directory)
* [Pre-Commit](https://pre-commit.com) setup with flake8, isort, etc. for
linting
* `setup.py` and `pyproject.toml` for PyPI package release
* A comprehensive `.gitignore`

## Example run
```
cookiecutter https://github.com/mattdood/pypi-cookiecutter

directory_name [sample]:
project_name [sample]:
project_slug [sample
author_name [Matthew Wimberly]:
author_email [matthew.wimb@gmail.com]:
description [A sample project build.]:
github_username [mattdood]:
repository_name [sample]:
min_python_version [3.6]:


cd sample/
tree .
    .
    ├── assets
    ├── conftest.py
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── sample
    │   └── __init__.py
    ├── setup.py
    └── test
        └── __init__.py

    3 directories, 9 files
```

