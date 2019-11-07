FROM python:3.6-alpine as base

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install

FROM base as app
COPY app app
COPY tools tools
COPY manage.py ./

FROM app as test
COPY test test
RUN ["pipenv", "run", "python", "manage.py", "autotests"]

FROM app
COPY test test
ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD ["runserver"]