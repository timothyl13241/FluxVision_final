#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from evdev import uinput, ecodes as e
import time

def skip_video(PinNr):
    global prev_inp

    inp = GPIO.input(PinNr)
    if (not prev_inp) and inp:

        #turn off LED
        GPIO.output(13, False)

        #simulate keystroke "o", which tells omxplayer to skip to the next video (easier than using dbus!)
        with uinput.UInput() as ui:
            ui.write(e.EV_KEY, e.KEY_O, 1)
            ui.syn()

        #disable button for 1 second
        time.sleep(1.0)

        #turn on LED
        GPIO.output(13, True)

    prev_inp = inp

try:
    while True:
        skip_video(21)
except KeyboardInterrupt:
    GPIO.cleanup()