FROM mongo:latest

WORKDIR /usr/src/db/

COPY ./db/mongod.conf /etc/

EXPOSE 27017

CMD ["mongod"]