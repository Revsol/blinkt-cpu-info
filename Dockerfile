FROM resin/rpi-raspbian:jessie

RUN apt-get update -qy && apt-get install -y \
    python \
    python-rpi.gpio
	

RUN apt-get install -y libraspberrypi-bin

# RUN apt-get install -y gcc python-dev python-pip

# RUN pip install psutil

RUN apt-get install python-blinkt

RUN apt-get install python-psutil

# Cancel out any Entrypoint already set in the base image.
ENTRYPOINT []	

# WORKDIR /root/

# COPY library	library
# WORKDIR /root/library
# RUN python setup.py install

WORKDIR /root/
COPY scripts	scripts
WORKDIR /root/scripts

ENV Mode="Mixed"
ENV Brightness="0.05"
ENV Interval="0.05"

CMD ["python", "cpu_info.py"]
