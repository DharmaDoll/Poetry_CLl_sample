# Poetry_CLl_sample

# Setting up python environment and initializing packages and dockerize
```sh
# Install poetry
pyenv version 3.8.0
which python
# /Users/taro/.pyenv/shims/python

sudo pip install poetry
poetry -V
poetry config --list

#Create package
poetry new fire_sample_pkg
tree fire_sample_pkg
# fire_sample_pkg
# ├── README.rst
# ├── fire_sample_pkg
# │   └── __init__.py
# ├── pyproject.toml
# └── tests
#     ├── __init__.py
#     └── test_fire_sample_pkg.py
cd fire_sample_pkg
poetry env info
# Virtualenv
# Python:         3.8.0
# Implementation: CPython
# Path:           NA

# System
# Platform: darwin
# OS:       posix
# Python:   /Users/taro/.pyenv/versions/3.8.0
poetry add fire #If you don't have an environment yet, create virtual environment.
poetry env list
# fire-sample-pkg-LmRj2E63-py3.8 (Activated)

poetry shell
# Spawning shell within /Users/taro/Library/Caches/pypoetry/virtualenvs/fire-sample-pkg-LmRj2E63-py3.8
which python
# /Users/taro/Library/Caches/pypoetry/virtualenvs/fire-sample-pkg-LmRj2E63-py3.8/bin/python
# (fire-sample-pkg-LmRj2E63-py3.8)
```

