# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import os
import glob
import time
import base64
import pandas as pd
from matplotlib import pyplot as plt
import datetime
 
# Add the one wire module to the kernel
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Set the location of where to find one wire data
base_dir = '/sys/bus/w1/devices/'
device_folder_greenhouse = glob.glob(base_dir + '28-3c23f6499d8c')[0]
device_file_greenhouse = device_folder_greenhouse + '/w1_slave'
#device_folder_outside = glob.glob(base_dir + '28*')[0]
#device_file_outside = device_folder + '/w1_save'

def __create_graph(csv_path):
    ns = 1000000000
    # Read in the csv file that contains time,greenhouse temp,outside temp
    temps = pd.read_csv(csv_path)
    # Get the column names (time,greenhouse,outside)
    column_names = list(temps.columns)
    # Get the time for the temperature readings
    time = temps[temps.columns[0]]
    time = time.apply(lambda x : datetime.datetime.fromtimestamp(x/ns))
    # Get the greenhouse temperatures
    greenhouse_temps = temps[temps.columns[1]]
    # Get the outside temperatures
    outside_temps = temps[temps.columns[2]]
    # Set the size of the plot
    f = plt.figure()
    f.set_figwidth(18)
    f.set_figheight(7)
    # Add the time, greenhouse, and outside temperatures to the plot
    plt.plot(time, greenhouse_temps, color = 'g', linestyle = 'dashed',
             marker = 'o',label = "Greenhouse")
    plt.plot(time, outside_temps, color = 'b', linestyle = 'solid',
             marker = 'o',label = "Outside")
    # Set the angle at which the x labels will be displayed
    plt.xticks(rotation = 80)
    # Set the x axis title
    plt.xlabel('Dates')
    # Set the y axis title
    plt.ylabel('Temperature(°F)')
    # Set the plot title
    plt.title('Greenhouse vs Outside', fontsize = 20)
    # Set the plot legend
    plt.legend()
    # Save the plot to disk
    plt.savefig(csv_path[:-3]+'png', bbox_inches="tight")

def __create_html(csv_path):
    # Create a very basic html that includes the location of the plot on disk
    html = """<!DOCTYPE html>
    <html>
       <head>
          <title>Greenhouse Vs Outside Temperatures</title>
       </head>
       <body>
          <img src=\"""" + './temp_readings.png' + """\" alt=\"Greenhouse vs outside temperatures graph\">
       </body>
    </html>
    """
    # Write the html to a file on disk
    f_out = open('/var/www/html/index.html', 'w')
    f_out.write(html)
    f_out.close()
 
def __read_temp_raw(device_file):
    # Read from the temperature sensor
    f_in = open(device_file, 'r')
    lines = f_in.readlines()
    f_in.close()
    # Return what was read from the sensor
    return lines
 
def __read_temp(device_file):
    # Get the sensor reading
    lines = __read_temp_raw(device_file)
    # Filter out temperature (which is in Celsius)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = __read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        # Convert from Celsius to Farenheit
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

def __write_temp(csv_path):
    # Get the time of the reading
    current_time = time.time_ns()
    # Read from the greenhouse sensor
    greenhouse_temp = __read_temp(device_file_greenhouse)
    # Read from the outside sensor (which presently does not exist)
    outside = '30'
    # Write the readings to the csv file in the format of time,greenhouse,outside
    f_out = open(csv_path, 'a')
    f_out.write(str(current_time) + ',' + str(round(greenhouse_temp)) + ',' + outside + '\n')
    f_out.close()

def exec_temp():
    while True:
        csv_path = '/var/www/html/temp_readings.csv'
        __write_temp(csv_path)
        __create_graph(csv_path)
        __create_html(csv_path)
        time.sleep(900)

def main():
    exec_temp()

if __name__ == "__main__":
    main()
