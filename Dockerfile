FROM resin/rpi-raspbian:jessie

RUN apt-get update -qy && apt-get install -y \
    python \
    python-rpi.gpio

RUN apt-get install -y libraspberrypi-bin

RUN apt-get install python-blinkt

RUN apt-get install python-psutil

WORKDIR /root/
COPY scripts	scripts
WORKDIR /root/scripts

ENV Mode="Mixed"
ENV Brightness="0.05"
ENV Interval="0.05"
ENV Smooth="True"
ENV Orientation="L2R"

STOPSIGNAL SIGTERM

ENTRYPOINT ["python", "./cpu_info.py"]
