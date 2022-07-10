FROM python:3.8-buster

COPY fire_sample_pkg/ /opt/app/fire_sample_pkg
COPY ./pyproject.toml /opt/app

WORKDIR /opt/app

RUN pip install poetry && poetry install

# CMD python -v
ENTRYPOINT ["poetry", "run", "mycli"]
# ENTRYPOINT poetry run mycli #これだとdocker run の時、引数受け付けなかった
# この辺わかりやすい。https://github.com/taro/shellscripts/tree/master/Dockerfiles

# $ docker build --no-cache -t mycli .
# $ docker run --rm  -it mycli sub2 run -h