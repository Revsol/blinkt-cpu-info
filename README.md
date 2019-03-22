# CPU Temperature and Load shown with Pimoroni Blinkt and/or LED SHIM for Raspberry Pi.

![Blinkt!](https://raw.githubusercontent.com/Revsol/blinkt-cpu-info/master/cluster-mixed.gif)

# Usage
The following commands runs the CPU-Info Docker container.  
* The short command for all that can't await it:
    ```bash
    docker run -d \
    --name blinkt-cpu-info \
    --privileged \
    --restart=unless-stopped \
    -e Device=Blinkt \
    cisecke/blinkt-cpu-info
    ```
* The complete command with all arguments:
    ```bash
    docker run -d \
    --name blinkt-cpu-info \
    --privileged \
    --restart=unless-stopped \
    -e Mode=Mixed \
    -e Brightness=0.05 \
    -e Interval=0.05 \
    -e Smooth=True \
    -e Direction=LTR \
    -e Device=Blinkt \
    -e Marker=False \
    -e Segmented=False \
    cisecke/blinkt-cpu-info
    ```

> **Privileged mode is needed to access the GPIO Header.**

# Parameters
When running the client, the following parameters are available
* ```-e Mode=Mixed``` The Mode can be chosen between ```Mixed```(default), ```Temp``` and ```Load```.
    * ```-e Mode=Temp``` shows the temperature in red, it is divided in 10°C steps. As example for Blinkt 4 red LEDs means 40°C.
    * ```-e Mode=Load``` shows the CPU Load in blue, it is divided by the device LED count (Blinkt has 8 and SHIM has 28). As example for Blinkt 4 blue LEDs mean 50% CPU Load.
    * ```-e Mode=Mixed``` combines the other 2 modes and mixes the colors as purple.
* ```-e Brightness=0.05``` sets the brightness of the LEDs from 0.0 to 1.0 (default 0.05 for BLINKT and 1.0 for LED SHIM).
* ```-e Interval=0.05``` sets the interval in which the values are updated (default 0.05).
* ```-e Smooth=True``` smoothens the colors of the LEDs, set ```False``` to deactivate (default True).
* ```-e Direction=LTR``` sets the orientation of the LEDs to left-to-right (```LTR```) or right-to-left (```RTL```) (default LTR).
* ```-e Device=Blinkt``` The Device can be chosen between ```Blinkt``` (default) and ```Shim```
    * ```-e Device=Blinkt``` sets the output device to [Blinkt](https://shop.pimoroni.com/products/blinkt).
    * ```-e Device=Shim``` sets the output device to [LED SHIM](https://shop.pimoroni.com/products/led-shim).
* ```-e Marker=True``` shows 3 markers on the device for a better segment recognition, especially useful for the LED SHIM with it's 28 LEDs (default False for Blinkt and True for LED SHIM).
* ```-e Segmented=True``` shows the load of all 4 CPU Cores separated (default False for Blinkt and True for LED SHIM).

All parameters are optional and the values are case-insensitive, the default values are used if they are omitted.  
If LED SHIM is used as Device, a higher Brightness than the Blinkt value should be used because Blinkt is much brighter than LED SHIM.

# Future
* Make the docker image smaller.
* Add docker-compose file.

# Changelog:
* 16-03-2019:
    * ```Device``` introduced to change the output device between [Blinkt](https://shop.pimoroni.com/products/blinkt) and [LED SHIM](https://shop.pimoroni.com/products/led-shim)
    * ```Marker``` introduced
    * ```Orientation``` renamed to ```Direction```
    * ```L2R``` and ```R2L``` renamed
* 23-02-2019: Orientation added and base image changed to ```balenalib/rpi-raspbian```

# More Info
* https://github.com/revsol/blinkt-cpu-info
* For issues, suggestions or questions just create an Issue on Github.
* Thanks to [Pimoroni](https://shop.pimoroni.com/) for their great toys.
* https://shop.pimoroni.com/products/blinkt
* https://shop.pimoroni.com/products/led-shim