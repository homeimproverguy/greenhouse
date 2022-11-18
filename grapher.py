# https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator
import datetime
 
def create_graph(csv_path):
    # Read in the csv file that contains time,greenhouse temp,outside temp
    temps = pd.read_csv(csv_path)
    # Get the column names (time,greenhouse,outside)
    column_names = list(temps.columns)
    # Get the time for the temperature readings
    time = temps[temps.columns[0]]
    time = time.apply(lambda x : datetime.datetime.fromtimestamp(x))
    # Get the greenhouse temperatures
    greenhouse_temps = temps[temps.columns[1]]
    # Get the outside temperatures
    outside_temps = temps[temps.columns[2]]
    # Get the barrel1 temperatures
    barrel1_temps = temps[temps.columns[3]]
    # Set the size of the plot
    f = plt.figure()
    f.set_figwidth(18)
    f.set_figheight(7)
    # Add the time, greenhouse, and outside temperatures to the plot
    plt.plot(time, greenhouse_temps, color = 'g', linestyle = 'solid',
             marker = 'o',label = "Greenhouse")
    plt.plot(time, outside_temps, color = 'y', linestyle = 'solid',
             marker = 'o',label = "Outside")
    plt.plot(time, barrel1_temps, color = 'b', linestyle = 'solid',
             marker = 'o',label = "Barrel1")
    # Set the angle at which the x labels will be displayed
    plt.xticks(rotation = 80)
    # Set the x axis title
    plt.xlabel('Dates')
    # Set the y axis title
    plt.ylabel('Temperature(°F)')
    # Set the plot title
    date = datetime.datetime.today().strftime("%b %Y")
    plt.title(label='Greenhouse vs Outside Temperatures\n' + date, fontsize = 20)
    # Set the plot legend
    plt.legend()
    # Show the month and year on the x axis
    #months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
    #monthsFmt = DateFormatter("%b '%y")
    ax = plt.gca()
    #ax.xaxis.set_major_locator(months)
    #ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_major_locator(DayLocator(interval=1))
    ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    plt.grid(axis='y', which='both')
    # Include y axis tick marks on the right side of the plot
    plt.tick_params(labelright=True)
    # Save the plot to disk
    plt.savefig(csv_path[:-3]+'png', bbox_inches="tight")

def create_html(csv_path):
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
