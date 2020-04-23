FROM node:latest

EXPOSE 80
EXPOSE 3000

RUN git clone https://github.com/aitorru/NodeLandingPort.git NodeLandingPort -b master

WORKDIR /NodeLandingPort/

ENTRYPOINT python3 update.py