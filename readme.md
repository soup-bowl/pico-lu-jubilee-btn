# London Underground Jubilee Line button project
This is very much experimental, and is based upon custom wiring. Your mileage might vary.

## Dependencies
```
sudo apt install python3-rpi.gpio python3-gpiozero
```

## Pin Connections
In this setup, the following is assumed (board, not Broadcom SOC):
```
06 | Ground.
07 | Tube button. 
17 | Tube button.
22 | Tube LED (Mosfet).
```
