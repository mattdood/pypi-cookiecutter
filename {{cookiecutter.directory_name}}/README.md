# {{cookiecutter.project_slug}}
{{cookiecutter.description}}

<img src="https://img.shields.io/github/issues/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}"
    target="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/issues"
    alt="Badge for GitHub issues."/>
<img src="https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}"
    target="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/forks"
    alt="Badge for GitHub forks."/>
<img src="https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}"
    alt="Badge for GitHub stars."/>
<img src="https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}"
    target="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/raw/master/LICENSE"
    alt="Badge for GitHub license, MIT."/>
<img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repository_name}}"
    target="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repository_name}}"
    alt="Badge for sharable Twitter link."/>
[![Pytest](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/{{cookiecutter.project_slug}}.svg)](https://badge.fury.io/py/{{cookiecutter.project_slug}})

## Installation
To install {{cookiecutter.project_name}} run the following:
```
pip install {{cookiecutter.project_slug}}
```

## Features
*

## Usage


## Running tests
[Pytest](https://pytest.org) is used as the test runner. To install and run tests
use the `requirements-dev.txt` and execute with `pytest`.

**Note:** Use a virtual environment. The steps to create one are left to the user,
there are many packages that accomplish this.

```bash
pip install -r requirements-dev.txt
pytest
```

## Linting code
The project utilizes [Pre-Commit](https://pre-commit.com) to execute linting. This
ensures code quality is solid, and is used both in the CI and the `requirements-dev.txt`
for local execution.

The following hooks are used inside Pre-Commit:
* trailing-whitespace
* check-yaml
* isort
* flake8

To run Pre-Commit, use the following:

```bash
pre-commit run --all-files
```

