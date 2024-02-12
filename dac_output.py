import time
import pandas as pd
import Adafruit_MCP4725
import smbus2
import pi_MCP4725


dac = pi_MCP4725.MCP4725(smbus2.SMBus(1), 0x62,smbus2)
while True:

    for x in range(0,4097,150):

        
        print(x)

        dac.write(x)


        voltage = x/4096.0*5.0

        print("\nAnalogVolt: %.2f\n" % voltage)

        time.sleep(0.001)
