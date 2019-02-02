#!/usr/bin/env python

import os
import time
import psutil
from subprocess import PIPE, Popen
import blinkt

mode = os.environ['Mode']
if mode not in ['Mixed', 'Temp', 'Load']:
    raise ValueError('Mode not recognized.')
brightness = float(os.environ['Brightness'])
interval = float(os.environ['Interval'])

blinkt.set_clear_on_exit()
blinkt.set_brightness(brightness)


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
    for x in range(blinkt.NUM_PIXELS):
        r, g, b = 0, 0, 0
        if temp > 0:
            r = 255
        if load > 0:
            b = 255

        blinkt.set_pixel(x, r, g, b)
        temp -= 1
        load -= 1

    blinkt.show()


while True:
    temp = 0
    load = 0
    if mode in ['Mixed', 'Temp']:
        temp = get_cpu_temperature() / 100
    if mode in ['Mixed', 'Load']:
        load = psutil.cpu_percent() / 100.0
    show_graph(temp, load)
    time.sleep(interval)
