# -*- coding: utf-8 -*-

# for windows
import winsound

duration = 1000  # miliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)

# for linux/mac
import os

duration = 1  # second
freq = 440  # Hz
os.system('play --no-show-progress --null --channels 1 synth $s sine $f % (duration, freq)')


import requests


def get_info():
    pass


def manage():
    get_info()



if __name__ == '__main__':
    manage()
