# London Underground Jubilee Line button project
Currently designed for the **Raspberry Pi Pico** running **MicroPython**. **This will change as I need radio communications**.

This is very much experimental, and is based upon custom wiring. Your mileage might vary.

## Pin Connections
Following the [Pico schematics](https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf), in this setup the following is assumed:
```
Pin 27 - GP21 | Tube button, connected to GND on pin 18.
Pin 29 - GP22 | Tube LED Mosfet gate (pass 9V battery supply).
```

For the most part this project [follows this instructables guide](https://www.instructables.com/Hacking-a-London-Underground-Jubilee-Line-Door-But/).
