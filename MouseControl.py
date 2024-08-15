import os
import tempfile
import random
import time
os.environ['TMPDIR'] = '/path/to/custom/tempdir'
tempfile.tempdir = '/path/to/custom/tempdir'

from pynput.mouse import Button, Controller

mouse = Controller()

num1 = 10
num2 = 20
# print("The current mouse position is {0}".format(mouse.position))
mouse.position = (num1,num2)

for i in range(100):
    
    mouse.position = (num1,num2)

    num1 = random.randint(0,2560)
    num2 = random.randint(0,1600)
    
    mouse.move = (num1,num2)
    time.sleep(0.1)