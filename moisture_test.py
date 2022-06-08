import time

from board import SCL,SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
i2c_bus = busio.I2C(SCL,SDA)
ss = Seesaw(i2c_bus, addr=0x36)
while True:
    try:
        Check = i2c_bus.scan()
        if not bool(Check):
            print("sensor disconected")
        else:
            touch = ss.moisture_read()
            print(touch)
    except ValueError:
        print("sensor disconected")
    time.sleep(1)        
        
