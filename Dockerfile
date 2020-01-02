FROM mongo

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install --no-install-recommends -y python3 python3-pip

COPY requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

COPY data/data.json /src
COPY app.py /src
COPY buzz /src/buzz
COPY run.sh /src

CMD [ "/src/run.sh" ]
