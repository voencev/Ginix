#from machine import deepsleep
import time
UTC_OFFSET = 3

import os
import sys

import network
wifi = network.WLAN(network.STA_IF)

with open('/bin/shell.py') as shell:
    exec(shell.read())
#deepsleep()