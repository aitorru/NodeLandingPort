FROM node:latest

EXPOSE 80
EXPOSE 3000

RUN git clone https://github.com/aitorru/NodeLandingPort.git

ENTRYPOINT DEBUG=myapp:* npm start