# Simone

Simon, built for the Raspberry Pi.

## About

![Simon Game](https://cloud.githubusercontent.com/assets/13719429/21077790/1c89934a-bf25-11e6-806d-6c318639b686.jpg)

[Simon](https://en.wikipedia.org/wiki/Simon_(game)) is an electronic memory game based on a series of blinking colored lights. A player must correctly match the series, and in doing so, the series becomes longer and more complex. The player continues until they incorrectly match the sequence.

Simone is a recreation of Simon built for the Raspberry Pi. The game can be played both through a Console and through the Raspberry Pi GPIO (with additional hardware).

## Authors

[Bill Dybas](https://github.com/billdybas) & [Robert McLaughlin](https://github.com/robmcl4)

## Prerequisites

### Software

You must have [Python 2.7](https://www.python.org/downloads/) and the [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) package installed. These come installed by default on [Raspbian](https://www.raspberrypi.org/downloads/raspbian/).

### Hardware

You must have 4 LEDs (we used red, yellow, green, and blue), 4 resistors, 4 push-buttons, and a way of connecting them together and to the Pi GPIO (wire, solder, breadboard, etc.).

Suggested GPIO pin configuration has been defined in `simone_io.py`.

![Simone Game Hardware](https://cloud.githubusercontent.com/assets/13719429/21077762/21146210-bf24-11e6-97dc-a19ae275b0a2.JPG)

## Installation & Usage

1. Clone this repository & `cd` into it.
2. Run `main.py` as defined below

`python main.py game_mode`

Where `game_mode` is `0` for Raspberry Pi GPIO mode and `1` for Console mode.

## Gameplay

The game starts once the Python file is executed - the first color will blink. Match the color within 3 seconds or else the game will timeout. If an incorrect input is entered or the game times out, all four colors will blink at once. If the game was a high score, each color will blink once before all blinking at once. To start another round, simply provide any input to the system - it will then blink the first color.

## License

See the LICENSE file for more details.
