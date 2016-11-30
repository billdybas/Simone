import RPi.GPIO as gpio
import time

class Output:
    def blink(self, color):
        pass

    def blinkSequence(self, sequence):
        for color in sequence:
            self.blink(color)

class GPIO(Output):
    pins = {
        'buttons': { # TODO: Add pull-down GPIO pins
            'RED': -1,
            'GREEN': -1,
            'YELLOW': -1,
            'WHITE': -1
        },
        'leds': { # TODO: Add output pins for the LEDs
            'RED': -1,
            'GREEN': -1,
            'YELLOW': -1,
            'WHITE': -1
        }
    }

    def __init__(self):
        gpio.setmode(gpio.BOARD)

        for p in self.pins.buttons:
            gpio.setup(self.pins.buttons[p], gpio.IN, pull_up_down = gpio.PUD_DOWN)
        for p in self.pins.leds:
            gpio.setup(self.pins.leds[p], gpio.OUT)

    def blink(self, color):
        leds = self.pins.leds

        if color in leds:
            gpio.output(leds[color], True)
            time.sleep(1)
            gpio.output(leds[color], False)
        else:
            raise ValueError('Unknown Color Provided')

class Screen(Output):
    colors = ['RED', 'GREEN', 'YELLOW', 'WHITE']

    def blink(self, color):
        if color in self.colors:
            print color
        else:
            raise ValueError('Unknown Color Provided')
