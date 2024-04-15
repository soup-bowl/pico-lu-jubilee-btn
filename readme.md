# London Underground Jubilee Line button project
![Screenshot_20210828_143149](https://user-images.githubusercontent.com/11209477/131219652-f51a6f8e-2a31-42a7-83b5-52b0ee1ea1aa.png)
Currently designed for the **Raspberry Pi Pico** running **MicroPython**. **This will change as I need radio communications**.

This is very much experimental, and is based upon custom wiring. Your mileage might vary.

## Pin Connections
Following the [Pico schematics](https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf), in this setup the following is assumed:
```
Pin 27 - GP21 | Tube button, connected to GND on pin 18.
Pin 29 - GP22 | Tube LED Mosfet gate (pass 9V battery supply).
```

![](https://github.com/soup-bowl/pico-lu-jubilee-btn/assets/11209477/11cd4aa1-8f4a-4cb9-9f23-0ba0062e9474)


For the most part this project [follows this instructables guide](https://www.instructables.com/Hacking-a-London-Underground-Jubilee-Line-Door-But/).
