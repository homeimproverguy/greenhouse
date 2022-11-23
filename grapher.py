# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator
import datetime
 
def create_graph(csv_temp_path, csv_light_path):
    # Read in the csv file that contains time,greenhouse temp,outside temp
    temps = pd.read_csv(csv_temp_path)
    # Get the column names (time,greenhouse,outside)
    column_names = list(temps.columns)
    # Get the time for the temperature readings
    temp_time = temps[temps.columns[0]]
    temp_time = temp_time.apply(lambda x : datetime.datetime.fromtimestamp(x))
    # Get the greenhouse temperatures
    greenhouse_temps = temps[temps.columns[1]]
    # Get the outside temperatures
    outside_temps = temps[temps.columns[2]]
    # Get the barrel1 temperatures
    barrel1_temps = temps[temps.columns[3]]
    # Set the size of the plot
    barrel2_temps = temps[temps.columns[4]]
    # Set the size of the plot
    barrel3_temps = temps[temps.columns[5]]

    light_data = pd.read_csv(csv_light_path)
    light_col_names = list(light_data.columns)
    light_time = light_data[light_data.columns[0]]
    light_time = light_time.apply(lambda x : datetime.datetime.fromtimestamp(x))
    light_readings = light_data[light_data.columns[1]]

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

    fig.set_figwidth(18)
    fig.set_figheight(7)
    ax1.legend(loc='upper left')
    ax2.legend(loc='lower left')

    # Set the angle at which the x labels will be displayed
    plt.xticks(rotation = 80)
    # Set the x axis title
    #plt.xlabel('Dates')
    # Set the y axis title
    #plt.ylabel('Temperature(°F)')
    # Set the plot title
    date = datetime.datetime.today().strftime("%b %Y")
    plt.title(label='Greenhouse Sensors\n' + date, fontsize = 20)
    # Set the plot legend
    #plt.legend()
    # Show the month and year on the x axis
    #months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
    #monthsFmt = DateFormatter("%b '%y")
    #ax = plt.gca()
    #ax.xaxis.set_major_locator(months)
    #ax.xaxis.set_major_formatter(monthsFmt)
    #ax.xaxis.set_major_locator(DayLocator(interval=1))
    #ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    #plt.grid(axis='y', which='both')
    # Include y axis tick marks on the right side of the plot
    #plt.tick_params(labelright=True)
    # Save the plot to disk
    plt.savefig(csv_temp_path[:-3]+'png', bbox_inches="tight")

def create_html(csv_temp_path):
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
