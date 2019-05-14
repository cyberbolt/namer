FROM python:3.7-alpine

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY app app
COPY manage.py boot.sh ./
RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]
