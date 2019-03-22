FROM balenalib/rpi-raspbian

RUN apt-get update -qy && apt-get install -y \
    python \
    python-rpi.gpio \
    -y libraspberrypi-bin \
    python-blinkt \
    python-ledshim \
    python-psutil

WORKDIR /root/
COPY scripts	scripts
WORKDIR /root/scripts

ENV Mode="Mixed"
ENV Brightness=""
ENV Interval="0.05"
ENV Smooth="True"
ENV Direction="LTR"
ENV Device="Blinkt"
ENV Marker=""
ENV Segmented=""

STOPSIGNAL SIGTERM

ENTRYPOINT ["python", "./cpu_info.py"]
