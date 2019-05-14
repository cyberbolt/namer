[![Build Status](https://travis-ci.com/cyberbolt/namer.svg?token=sMYf9vsMSRRGjZKJ1mpo&branch=master)](https://travis-ci.com/cyberbolt/namer)

# Namer
Service/sandbox to polish devops techniques

## Prerequisites
- This app uses mongoDb as storage, so you need to have somewhere a working instance of it that app may communicate with db.
- For local installation Pyhton 3.6 or later version is required
- For installation using docker image the docker required

## Local installation
1. Install pipenv for managing python virtual environments.
```
$ pip install pipenv
```
2. Update virtual environment with required for app packages.
```
$ pipenv install
```
3. You have to define environment variables M\_DB for db name, M\_HOST for address of mongoDb instance, M\_PORT for port of mongoDb instance is running at.
4. Run app
```
pipenv run python manage.py runserver
```
The app will run locally, you may access it by http://localhost:5000

## Install from docker image
1. Get the image from docker hub
```
# docker pull bzamilov/namer:latest
```
2. Run container with image
```
# docker run --name namer -d \
-e M_DB=db_name_for_app \
-e M_HOST=mongodb_host_address \
-e M_PORT=27017_or_else \
-p 5000:5000 \
bzamilov/namer:latest
```
The app will run locally inside docker container namer, you may access it by http://localhost:5000

## Cloud upload
To be defined later
