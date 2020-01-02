FROM alpine:3.9

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/main' >> /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/community' >> /etc/apk/repositories

RUN apk add --update --no-cache mongodb mongodb-tools python py-pip

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY data/data.json /src
COPY app.py /src
COPY buzz /src/buzz
COPY run.sh /src

VOLUME /data/db

ENTRYPOINT [ "/src/run.sh" ]

CMD [ "mongod" ]