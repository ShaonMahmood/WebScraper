# base image
FROM python:3.10-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# install dependencies first to use cache

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

# copy rest of the code

COPY . .

CMD [ "python3", "./start_script.py" ]