# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator
import datetime
 
def create_graph(csv_temp_path, csv_light_path, sensor_plot_path):
    # Read in the csv file that contains time,greenhouse temp,outside temp
    temps = pd.read_csv(csv_temp_path)
    # Get the time for the temperature readings
    temp_time = temps[temps.columns[0]]
    temp_time = temp_time.apply(lambda x : datetime.datetime.fromtimestamp(x))
    # Get the greenhouse temperatures
    greenhouse_temps = temps[temps.columns[1]]
    # Get the outside temperatures
    outside_temps = temps[temps.columns[2]]
    # Get the barrel temperatures
    barrel1_temps = temps[temps.columns[3]]
    barrel2_temps = temps[temps.columns[4]]
    barrel3_temps = temps[temps.columns[5]]

    # Get the light sensor data
    light_data = pd.read_csv(csv_light_path)
    light_time = light_data[light_data.columns[0]]
    light_time = light_time.apply(lambda x : datetime.datetime.fromtimestamp(x))
    light_readings = light_data[light_data.columns[1]]

    # Set the plot labels
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax2.plot(temp_time, greenhouse_temps, 'g-', label = 'Greenhouse')
    ax2.plot(temp_time, outside_temps, 'c-', label = 'Outside')
    ax2.plot(temp_time, barrel1_temps, 'b-', label = 'Barrel1')
    ax2.plot(temp_time, barrel2_temps, 'm-', label = 'Barrel2')
    ax2.plot(temp_time, barrel3_temps, 'r-', label = 'Barrel3')
    ax1.plot(light_time, light_readings, 'y', label = 'Light', linestyle='dotted')
    ax1.set_xlabel('Dates')
    ax2.set_ylabel('Temperature(°F)')
    ax1.set_ylabel('Light Reading')
    ax1.set_ylim([0, 2000])
    ax1.invert_yaxis()
    # Set the size of the plot
    fig.set_figwidth(18)
    fig.set_figheight(7)
    # Set the legend location
    ax1.legend(loc='upper left')
    ax2.legend(loc='lower left')
    # Set the date/time format
    date = datetime.datetime.today().strftime("%b %Y")
    plt.title(label='Greenhouse Sensors\n' + date, fontsize = 20)
    # Save the plot to disk
    plt.savefig(sensor_plot_path, bbox_inches="tight")

def create_html(sensor_plot_name):
    # Create a very basic html that includes the location of the plot on disk
    html = """<!DOCTYPE html>
    <html>
       <head>
          <title>Greenhouse Sensors</title>
       </head>
       <body>
          <img src=\"""" + sensor_plot_name + """\" alt=\"Greenhouse Sensors\">
       </body>
    </html>
    """
    # Write the html to a file on disk
    f_out = open('/var/www/html/index.html', 'w')
    f_out.write(html)
    f_out.close()
