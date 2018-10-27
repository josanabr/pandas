FROM josanabr/pandas

MAINTAINER John Sanabria 

RUN apt-get update && apt-get install build-essential python3-pip python3-dev -y

RUN pip3 install pandas numpy

RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install python3-matplotlib
