#!/usr/bin/env python

import signal
import os
import time
import psutil
from subprocess import PIPE, Popen
import sys
import math


device = os.environ['Device'].lower()
if device not in ['blinkt', 'shim']:
    raise ValueError('Device not recognized.')
if device == "shim":
    import ledshim as output_device
else:
    import blinkt as output_device

mode = os.environ['Mode'].lower()
if mode not in ['mixed', 'temp', 'load']:
    raise ValueError('Mode not recognized.')
brightness_parameter = os.environ['Brightness'].strip()
if brightness_parameter and not brightness_parameter == "":
    brightness = min(float(brightness_parameter), 1)
else:
    if device == 'shim':
        brightness = 1
    else:
        brightness = 0.05
interval = max(float(os.environ['Interval']), 0)
smooth = os.environ['Smooth'].lower() == "true"
marker_parameter = os.environ['Marker'].lower().strip()
if marker_parameter in ['true', 'false']:
    marker = marker_parameter == "true"
else:
    marker = device == "shim"
segmented_parameter = os.environ['Segmented'].lower().strip()
if segmented_parameter in ['true', 'false']:
    segmented = segmented_parameter == "true"
else:
    segmented = device == "shim"
direction = os.environ['Direction']

output_device.set_brightness(brightness)
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
    segment_pixels_count = output_device.NUM_PIXELS / 4
    temp = temp / 80 * output_device.NUM_PIXELS
    if isinstance(load, list):
        load = [x / 100 * segment_pixels_count for x in load]
    else:
        load = load / 100 * output_device.NUM_PIXELS
    pixels = range(output_device.NUM_PIXELS)
    current = 0
    if direction.lower() == "rtl":
        pixels = reversed(pixels)
    for x in pixels:
        r, g, b = 0, 0, 0
        if temp > 0:
            r = get_value(temp)
            temp -= 1
        if isinstance(load, list):
            segment_index = math.trunc(x / segment_pixels_count)
            if load[segment_index] > 0:
                b = get_value(load[segment_index])
                load[segment_index] -= 1
        else:
            if load > 0:
                b = get_value(load)
                load -= 1

        # show the marker, if it's not the last pixel and if it's the last pixel of the segment.
        if marker and current + 1 != output_device.NUM_PIXELS and (current +1) % segment_pixels_count == 0:
            g = 255
        output_device.set_pixel(x, r, g, b)
        current += 1

    output_device.show()


def get_value(value):
    max_value = 255
    if smooth and value <= 1:
        return max_value * value
    else:
        return max_value


def show_info():
    temp = 0
    load = 0
    if mode in ['mixed', 'temp']:
        temp = get_cpu_temperature()
    if mode in ['mixed', 'load']:
        if segmented:
            load = psutil.cpu_percent(percpu=segmented)
        else:
            load = psutil.cpu_percent()
    show_graph(temp, load)


if __name__ == '__main__':
    while True:
        if running:
            show_info()
            time.sleep(interval)
        else:
            break
    # shut off pixels and exit
    output_device.clear()
    output_device.show()



