# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import temp_sensor
import grapher
import time
import light_sensor

def exec_temp():
    while True:
        #try: 
            base_path = '/var/www/html/'
            csv_temp_path = base_path + 'temp_readings.csv'
            csv_light_path = base_path + 'light_readings.csv'
            # Get the time of the reading
            current_time = time.time()
            temp_sensor.write_temp(csv_temp_path, current_time)
            light_sensor.write_light(csv_light_path, current_time)
            grapher.create_graph(csv_temp_path, csv_light_path)
            grapher.create_html(csv_temp_path)
        #except:
            # Do nothing, just restart the loop
         #   pass
            time.sleep(900)

def main():
    exec_temp()

if __name__ == "__main__":
    main()
