FROM python:3.10-slim-buster
WORKDIR /code
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
COPY poetry.lock utils.py main.py pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
EXPOSE 80
