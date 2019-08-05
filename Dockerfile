FROM python:3.6-alpine as base

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install

FROM base as app
COPY app app
COPY test test
COPY tools tools
COPY manage.py ./
ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD["runserver"]