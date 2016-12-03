import RPi.GPIO as gpio
import time
import random

class Input:
    def wait_for_input(self):
        raise NotImplementedError()

class Output:
    colors = ['RED', 'GREEN', 'YELLOW', 'BLUE']

    def cleanup(self):
        raise NotImplementedError()

    def blink(self, color):
        raise NotImplementedError()

    def blink_all(self):
        raise NotImplementedError()

    def blink_sequence(self, sequence):
        for color in sequence:
            self.blink(color)

    def choose_random_color(self):
        return random.choice(self.colors)

class GPIO(Input, Output):
    pins = {
        'buttons': {
            'RED': 13,
            'GREEN': 19,
            'YELLOW': 21,
            'BLUE': 23
        },
        'leds': {
            'RED': 32,
            'GREEN': 36,
            'YELLOW': 37, # TODO: Put back to pin 38; Technical difficulties forced us to move it
            'BLUE': 40
        }
    }

    def __init__(self):
        gpio.setmode(gpio.BOARD)

        for p in self.pins['buttons']:
            gpio.setup(self.pins['buttons'][p], gpio.IN, pull_up_down = gpio.PUD_DOWN)
        for p in self.pins['leds']:
            gpio.setup(self.pins['leds'][p], gpio.OUT)

    def cleanup(self):
        gpio.cleanup()

    def blink(self, color):
        leds = self.pins['leds']

        if color in self.colors:
            gpio.output(leds[color], True)
            time.sleep(1)
            gpio.output(leds[color], False)
        else:
            raise ValueError('Unknown Color Provided')

    def blink_all(self):
        leds = self.pins['leds']

        for color in leds:
            gpio.output(leds[color], True)
        time.sleep(1)
        for color in leds:
            gpio.output(leds[color], False)

    def wait_for_input(self):
        buttons = self.pins['buttons']

        while True:
            if (gpio.input(buttons['RED'])):
                self.blink('RED')
                return 'RED'
            elif (gpio.input(buttons['GREEN'])):
                self.blink('GREEN')
                return 'GREEN'
            elif (gpio.input(buttons['YELLOW'])):
                self.blink('YELLOW')
                return 'YELLOW'
            elif (gpio.input(buttons['BLUE'])):
                self.blink('BLUE')
                return 'BLUE'

            time.sleep(0.1)

class Screen(Input, Output):

    def cleanup(self):
        pass # Intentionally left blank

    def blink(self, color):
        if color in self.colors:
            print color
        else:
            raise ValueError('Unknown Color Provided')

    def blink_all(self):
        print
        print ', '.join(self.colors)

    def blink_sequence(self, sequence):
        print
        for color in sequence:
            self.blink(color)
            if len(sequence) > 1:
                time.sleep(1)

    def wait_for_input(self):
        return raw_input()
