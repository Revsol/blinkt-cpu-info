# CPU Temperature and Load shown with Pimoroni Blinkt!

![Blinkt!](https://raw.githubusercontent.com/Revsol/blinkt-cpu-info/master/cluster-mixed.gif)

# Usage
The following command runs the CPU-Info Docker container:
```bash
docker run -d \
    --name blinkt-cpu-info \
    --privileged \
    --restart=unless-stopped \
    -e Mode=Mixed \
    -e Brightness=0.05 \
    -e Interval=0.05 \
    -e Smooth=True \
    -e Orientation=L2R \
    cisecke/blinkt-cpu-info
```

Privileged mode is needed to access the GPIO Header.

# Parameters
When running the client, the following parameters are available
* ```-e Mode=Mixed``` The Mode can be chosen between ```Mixed```(Default), ```Temp``` and ```Load```.
    * ```-e Mode=Temp``` shows the temperature in red, it is divided in 10°C steps. As example 4 red LEDs means 40°C
    * ```-e Mode=Load``` shows the CPU Load in blue, it is divided by 8(LED count) and represents 12.5%. As example 4 blue LEDs mean 50% CPU Load.
    * ```-e Mode=Mixed``` combines the other 2 modes and mixes the colors as purple.
* ```-e Brightness=0.05``` sets the brightness of the LEDs from 0.0 to 1.0 (default around 0.05).
* ```-e Interval=0.05``` sets the interval in which the values are updated (default around 0.05).
* ```-e Smooth=True``` smoothens the colors of the LEDs, set ```False``` to deactivate (default True).
* ```-e Orientation=L2R``` sets the orientation of the LEDs to Left-2-Right (L2R) or Right-2-Left (R2L) (default L2R).

All parameters are optional and the default values are used if they are omitted.

# Future
* Make the docker image smaller.
* Show Network usage.
* Add docker-compose file.

# Changelog:
* 23-02-2019: Orientation added and base image changed to ```balenalib/rpi-raspbian```

# More Info
* https://github.com/revsol/blinkt-cpu-info
* For issues, suggestions or questions just create an Issue on Github.
* Thanks to [Pimoroni](https://shop.pimoroni.com/) for their great toys.
* https://shop.pimoroni.com/products/blinkt