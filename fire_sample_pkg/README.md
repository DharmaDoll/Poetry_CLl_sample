## Build and run
```sh
docker build --no-cache -t mycli .
docker run --rm -it mycli sub2 run -h
```


## Deploy to local(virtual environment)

### Add setting to pyproject.toml
```toml
[tool.poetry.scripts]
mycli = "fire_sample_pkg.fire_sample:main"
```

```sh
which python
#/usr/bin/python

# Install to virtual env
poetry install

poetry shell
#Spawning shell within /home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10
#. /home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10/bin/activate

which python
#/home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10/bin/python

which mycli
#/home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10/bin/mycli
#こんな感じのコードで bin/配下にmycliファイルが作られてる。　
# from fire_sample_pkg.fire_sample import main
```

## How to install global environment
