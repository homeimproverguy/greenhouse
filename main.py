# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import temp_sensor
import grapher
import time
import light_sensor

def exec_temp():
    while True:
            # Set paths
            base_path = '/var/www/html/'
            sensor_plot_name = 'sensor_plot.png'
            sensor_plot_path = base_path + sensor_plot_name
            csv_temp_path = base_path + 'temp_readings.csv'
            csv_light_path = base_path + 'light_readings.csv'

            # Get the time of the reading
            current_time = time.time()
            # Collect and write temperature data to file
            temp_sensor.write_temp(csv_temp_path, current_time)
            # Collect and write light intensity data to file
            light_sensor.write_light(csv_light_path, current_time)
            # Create a plot and save to file
            grapher.create_graph(csv_temp_path, csv_light_path, sensor_plot_path)
            # Create html of the plot
            grapher.create_html(sensor_plot_name)
            time.sleep(900)

def main():
    exec_temp()

if __name__ == "__main__":
    main()
