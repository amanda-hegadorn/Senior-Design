import csv
import time
import MCP4725
import smbus2

# Initialize the DAC
dac = MCP4725.MCP4725(smbus2.SMBus(1), 0x62, smbus2)

# Specify the file name
fileName = 'data_2024-02-14.csv'

# Open and read the CSV file
with open(fileName, mode='r') as file:
    csvReader = csv.DictReader(file)
    currenttime_ms=0
    for row in csvReader:
        # Extract the voltage (mV) value from the CSV
        lasttime_ms=currenttime_ms
        currenttime_ms=float(row["Time (ms)"])
        voltage_mV = float(row['Voltage (mV)'])
        
        # Convert mV to V for the DAC calculation
        voltage_V = voltage_mV / 1000.0
        
        # Assuming your DAC output range is 0 to 5V, calculate the DAC value
        # Adjust the formula according to your DAC's resolution and voltage range if necessary
        dac_value = int((voltage_V / 5.0) * 4095)
        
        # Clamp the DAC value to the valid range [0, 4095] just in case
        dac_value = max(0, min(4095, dac_value))
        
        # Write the value to the DAC
        dac.write(dac_value)
        
        print(f"Setting DAC value to: {dac_value}, which corresponds to Analog Voltage: {voltage_V:.2f} V")
        
        # Delay to simulate real-time data playback, adjust as needed
        time.sleep((currenttime_ms-lasttime_ms)/1000)  # Adjust this delay to match the sampling rate of your original data if needed


#########################################################################

# import time
# import smbus2
# import MCP4725
# import csv

# dac = MCP4725.MCP4725(smbus2.SMBus(1), 0x62,smbus2)

# fileName='data_2024-02-14.csv'

# while True:
#     for x in range(0,4097,150):
#         print(x)
#         dac.write(x)

#         voltage = x/4096.0*5.0
#         print("\nAnalogVolt: %.2f\n" % voltage)
#         time.sleep(0.0001)
