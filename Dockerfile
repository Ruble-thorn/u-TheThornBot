FROM python:3.11
ENV POETRY_VERSION=1.5.1
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /þbot
COPY poetry.lock pyproject.toml /þbot/
RUN poetry install --no-interaction --no-ansi
COPY . /þbot/
CMD poetry install && poetry run python index.py
