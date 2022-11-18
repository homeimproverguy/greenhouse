# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import temp_sensor
import grapher
import time

def exec_temp():
    while True:
        #try: 
            csv_path = '/var/www/html/temp_readings.csv'
            temp_sensor.write_temp(csv_path)
            grapher.create_graph(csv_path)
            grapher.create_html(csv_path)
        #except:
            # Do nothing, just restart the loop
         #   pass
            time.sleep(900)

def main():
    exec_temp()

if __name__ == "__main__":
    main()
