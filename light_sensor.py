from gpiozero import MCP3008

def read_light():
        return MCP3008(channel=0, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)

def write_light(csv_path, current_time):
    # Read from the outside sensor
    light_reading = read_light()
    # Write the readings to the csv file in the format of time,greenhouse,outside
    f_out = open(csv_path, 'a')
    f_out.write(str(current_time) + ',' + str(round(light_reading.value*10000)) + '\n')
    f_out.close()
