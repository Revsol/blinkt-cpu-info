#!/usr/bin/env python

import signal
import os
import time
import psutil
from subprocess import PIPE, Popen
import blinkt
import sys

mode = os.environ['Mode']
if mode not in ['Mixed', 'Temp', 'Load']:
    raise ValueError('Mode not recognized.')
brightness = min(float(os.environ['Brightness']), 1)
interval = max(float(os.environ['Interval']), 0)
smooth = os.environ['Smooth'].lower() == "true"
orientation = os.environ['Orientation']

blinkt.set_brightness(brightness)
running = True


def sigterm(x, y):
    global running
    running = False


# Register the signal to the handler
signal.signal(signal.SIGTERM, sigterm)


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode()

    pos_start = output.index('=') + 1
    pos_end = output.rindex("'")

    temp = float(output[pos_start:pos_end])

    return temp


def show_graph(temp, load):
    temp *= blinkt.NUM_PIXELS
    load *= blinkt.NUM_PIXELS
    leds = range(blinkt.NUM_PIXELS)
    if orientation.lower() == "r2l":
        leds = reversed(leds)
    for x in leds:
        r, g, b = 0, 0, 0
        if temp > 0:
            r = get_value(temp)
        if load > 0:
            b = get_value(load)

        blinkt.set_pixel(x, r, g, b)
        temp -= 1
        load -= 1

    blinkt.show()


def get_value(value):
    max_value = 255
    if smooth and value <= 1:
        return max_value * value
    else:
        return max_value


def show_info():
    temp = 0
    load = 0
    if mode in ['Mixed', 'Temp']:
        temp = get_cpu_temperature() / 100.0
    if mode in ['Mixed', 'Load']:
        load = psutil.cpu_percent() / 100.0
    show_graph(temp, load)


if __name__ == '__main__':
    while True:
        if running:
            show_info()
            time.sleep(interval)
        else:
            break
    # shut off blinkt and exit
    blinkt.clear()
    blinkt.show()



