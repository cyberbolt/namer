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
-e M_USERNAME=username_to_access_mongo \
-e M_PASSWORD=password_to_access_mongo \
-p 5000:5000 \
bzamilov/namer:latest
```
The app will run locally inside docker container namer, you may access it by http://localhost:5000

## Install app + db containers
1. There is docker-compose.yml in ./tools dir, so it is possible to run container for database and app from one place. You have to get image of app from docker hub as described in Install from docker image.
2. Create a place to store database data
```
mkdir -p ~/docker-data/mongodb
```
2. Run docker-compose tool with predefined environment variables
```
M_HOST=mongodb_host_address \
M_PORT=27017_or_else \
M_USERNAME=username_to_access_mongo \
M_PASSWORD=password_to_access_mongo \
docker-compose up -d
```

## Cloud upload
1. Here is used app deployment with terraform to AWS cloud.
2. You need to create a key pair to communicate with AWS
```
ssh-keygen -t rsa -f my_key
```
3. The content of my\_key should be passed into env variable with single quotes. Public key from my\_key.pub should be passed into env variable with single quotes too. Public key should be a pair of private key if you not create it now but choosed to use other pair instead.
4. Run deploy command to deploy two instances to AWS - app and database
```
TF_VAR_aws_key='my_key_content' \
TF_VAR_aws_pub_key='my_key.pub_content' \
TF_VAR_aws_region=aws_region_you_have_access_to \
TF_VAR_aws_access_key_id=access_key_id_to_aws \
TF_VAR_aws_secret_access_key=access_key_to_aws \
TF_VAR_aws_m_username=db_user \
TF_VAR_aws_m_password=db_password \
terraform apply
```