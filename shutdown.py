#!/usr/bin/env python3

import gpiozero
import os

gpiozero.Button(21).wait_for_press()

os.system("sudo poweroff")

