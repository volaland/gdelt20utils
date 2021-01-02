FROM python:3.8-slim-buster

LABEL name="GDELT20 Utils"

RUN mkdir -p /usr/src/gdelt20_util

WORKDIR /usr/src/gdelt20_util

COPY . /usr/src/gdelt20_util


RUN pip install --upgrade pip && \
    pip install -r requirements/requirements.txt

ENTRYPOINT ["python", "manage.py"]
