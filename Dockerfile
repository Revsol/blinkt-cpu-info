FROM balenalib/rpi-raspbian

RUN apt-get update -qy && apt-get install -y \
    python \
    python-rpi.gpio \
    -y libraspberrypi-bin \
    python-blinkt \
    python-psutil

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
