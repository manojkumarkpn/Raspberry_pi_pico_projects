# Raspberry Pi Pico Projects

# 01. Blink
* Hello world program to blink on board LED of Raspberry Pi Pico

# 02. 02_Interface_8x8_LED
* Fetch Current temperature from onboard temperature sensor and display on MAX7219 8x8 LED Dot Matrix Display
* Hardwares required : Raspberry pi pico board, MAX7219 8x8 LED Dot Matrix Display Module
* Clone micropython-max7219 library from https://github.com/mcauser/micropython-max7219
* Upload max7219.py and main.py to your pico board
* Connections

|MAX7219|Pico Name|Pico GPIO|Pico PIN|
|-|-|-|-|
|VCC|VBUS||40|
|GND|GND||38|
|DIN|MOSI (SPI0 TX)|GP7|10|
|CS|SPI0 CSn|GP5|7|
|CLK|SCK|GP6|9|

# 03_stepper_28BYJ-48_ULN2003
* Interface 28BYJ-48 stepper motor with ULN2003 driver module
