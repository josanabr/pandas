FROM josanabr/flask

MAINTAINER John Sanabria 

RUN apt-get update && apt-get install build-essential python3-pip python3-dev -y

RUN pip3 install pandas numpy

