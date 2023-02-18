# Setting up poetry and create poetry application.

```sh
pyenv version 3.8.0
which python
# /Users/taro/.pyenv/shims/python
```
#### Install poetry
```sh
sudo pip install poetry
```
```
poetry -V
poetry config --list
```
#### Create package
```sh
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
#Virtualenv
#Python:         3.10.5
#Implementation: CPython
#Path:           NA

#System
#Platform: linux
#OS:       posix
#Python:   /usr
```
#### Add packages(If you don't have an environment yet, create virtual environment)
```sh
poetry add fire 
```
```sh
poetry env info
#Virtualenv
#Python:         3.10.5
#Implementation: CPython
#Path:           /home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10
#Valid:          True
#...

poetry shell
which python
#/home/mike/.cache/pypoetry/virtualenvs/fire-sample-pkg-9Hcw8gMH-py3.10/bin/python
```

## Using Docker
https://github.com/DharmaDoll/Poetry_CLl_sample/tree/main/fire_sample_pkg

## Packaging
new→build→publishの3コマンドでプロジェクト作成からPyPIに登録までできる
`poetry build` コマンドを実行すると pyproject.toml の [tool.poetry] セクションの name に設定されている名前と同じPythonファイルまたはパッケージ、あるいは src ディレクトリを探し、ビルドを行います。 buildコマンドでパッケージをビルドする際にpyproject.tomlの内容に基づいてsetup.pyを自動生成してくれます。dist/以下にtar.gzとwhlファイルが作成されます。
```sh
poetry build
# Building fire_sample_pkg (0.1.0)
#   - Building sdist
#   - Built fire_sample_pkg-0.1.0.tar.gz
#   - Building wheel
#   - Built fire_sample_pkg-0.1.0-py3-none-any.whl
```

生成されたsetup.pyを確認 setup.py/setup.cfg/MANIFEST.in はもう書かなくて良い？！install_requiresやconsole_scriptsなんかもpyproject.tomlに基づいて自動的に設定してくれる。また、setup.cfgやMANIFEST.inに書いていたような内容もpyproject.tomlがその役目を負ってくれているのでもう書く必要はありません。
```sh
cd dist/
tar zxvf fire_sample_pkg-0.1.0.tar.gz
# tar -xvf *.tar.gz '*/setup.py'
# tar -xvf dist/*.tar.gz --wildcards --no-anchored '*/setup.py' --strip=1

cd fire_sample_pkg-0.1.0
#とかでglobalに入れれる
pip install .
# python setup.py install
```
See also..　https://kk6.hateblo.jp/entry/2018/12/20/124151#PyPI%E3%81%B8%E3%81%AE%E5%85%AC%E9%96%8B

## Upload PyPI
パッケージを公開する `publish` コマンドはデフォルトではPyPIへのアップロードになっています。練習の場合PyPIではなくTestPyPIのほうにアップロードできるように設定しましょう。まずリポジトリの設定から。そもそもTestPyPIにアカウント登録していない場合はまずそちらを済ませておいてください。
https://pypi.org/account/login/?next=%2Fmanage%2Fprojects%2F

```sh
# repositories.XXX のXXXの部分に好きな名前を指定して、URLを紐づけます。
poetry config repositories.xxxtestxxx https://test.pypi.org/legacy/
# TestPyPIへのアップロードは https://test.pypi.org/legacy のほうじゃないとダメです。https://test.pypi.org/simple だと失敗します。（実は記事執筆時点の最新版のPoetryだと成功してる風な出力になりますが実際にはアップロードできてなくて、試しにtwineでアップロードしてみると405エラーになります。）
```
See Also..  https://kk6.hateblo.jp/entry/2018/12/20/124151#TestPyPIへアップロードできるようにする
