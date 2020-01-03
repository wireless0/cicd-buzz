FROM python:3-alpine

COPY requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

COPY webapp /opt/webapp/

CMD [ "python", "/opt/webapp/app.py" ]
