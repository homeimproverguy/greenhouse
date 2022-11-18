# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import os
import glob
import time
 
# Add the one wire module to the kernel
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Set the location of where to find one wire data
base_dir = '/sys/bus/w1/devices/'
device_folder_greenhouse = glob.glob(base_dir + '28-3c23f6499d8c')[0]
device_file_greenhouse = device_folder_greenhouse + '/w1_slave'

device_folder_outside = glob.glob(base_dir + '28-3ca6f649db80')[0]
device_file_outside = device_folder_outside + '/w1_slave'

device_folder_barrel1 = glob.glob(base_dir + '28-3c1ff6494742')[0]
device_file_barrel1 = device_folder_barrel1 + '/w1_slave'

def read_temp_raw(device_file):
    # Read from the temperature sensor
    f_in = open(device_file, 'r')
    lines = f_in.readlines()
    f_in.close()
    # Return what was read from the sensor
    return lines
 
def read_temp(device_file):
    # Get the sensor reading
    lines = read_temp_raw(device_file)
    # Filter out temperature (which is in Celsius)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        # Convert from Celsius to Farenheit
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

def write_temp(csv_path):
    # Get the time of the reading
    current_time = time.time()
    # Read from the greenhouse sensor
    greenhouse_temp = read_temp(device_file_greenhouse)
    # Read from the outside sensor
    outside_temp = read_temp(device_file_outside)
    # Read from barrel1 sensor
    barrel1_temp = read_temp(device_file_barrel1)
    # Write the readings to the csv file in the format of time,greenhouse,outside
    f_out = open(csv_path, 'a')
    f_out.write(str(current_time) + ',' + str(round(greenhouse_temp)) + ',' + str(round(outside_temp)) + ',' + str(round(barrel1_temp)) +'\n')
    f_out.close()
