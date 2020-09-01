import RPi.GPIO as gpio
import time
from datetime import datetime


 
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
 
pin = [11, 15, 16, 18]
for i in range(4):
    gpio.setup(pin[i], gpio.OUT)
 
forward_sq = ['0011', '1001', '1100', '0110']

 
def forward(steps, delay):
    for i in range(steps):
        for step in forward_sq:
            set_motor(step)
            time.sleep(delay)
 

 
def set_motor(step):
    for i in range(4):
        gpio.output(pin[i], step[i] == '1')
 
while True:
    a = time.strftime("%H:%M:%S")
    if (a == "12" or a == "09:19:40"):
        
        set_motor('0000')
        forward(480, 0.005)
    

    
        
        




