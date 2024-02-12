import ADS1115
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd
import smbus2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# are we saving data right now
save_data = False

# Initialize the ADS1115 ADC
ads = ADS1115.ADS1115()
ads.setADCConfig(sps=860)

# Number of data points
x_len = 30
y_range = [0, 5000]

# Create figure for plotting
fig, ax = plt.subplots()
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a line, which we will update with new data
line, = ax.plot(xs, ys)
start_time = time.time()
# Define a function for the animation

#create pandas object
data={"Time":[],"Voltage (mV)":[]}

def my_callback(channel):
    if GPIO.event_detected(channel):
        if(save_data):
            df = pandas.DataFrame.from_dict(data)
            df.to_csv("data_{datetime.date.today()}.csv")
            print("Saved data")
        if(not save_data):
            print("starting to save data")
        save_data= not save_data

GPIO.add_event_detect(11, GPIO.RISING, callback=my_callback)  # add rising edge detection on a channel

def animate(i, ys):
    # Read voltage from ADS1115
    volt = ads.readADC()
    x_val=start_time-time.time()
    #print(time.time())
    #print("{:.0f} mV measured on AN0".format(volt))

    # Add y to list
    ys.append(volt)
    if(save_data):
        data["Time"].append(x_val)
        data["Voltage (mV)"].append(volt)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    #print(i)
    return line,

# Set up plot to call animate() function periodically (every 1 ms, this is probably limiting our sampling frequency as well)
ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=.01, blit=True)
plt.show()



    
    
    
    

