I pulled these instructions and code from: https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

Wiring diagram for the DS18B20 TEMPERATURE SENSOR can be found at the circuitbasics website.

I will be using the ssh method to read the sensor, though I plan on modifying the code so that I will be able to display it in a graph. 
These are the instructions for setting up the Raspberry PI that are found in the website:

"ENABLE THE ONE-WIRE INTERFACE
We’ll need to enable the One-Wire interface before the Pi can receive data from the sensor. Once you’ve connected the DS18B20, power up your Pi and log in, then follow these steps to enable the One-Wire interface:

1. At the command prompt, enter sudo nano /boot/config.txt, then add this to the bottom of the file:

dtoverlay=w1-gpio

2. Exit Nano, and reboot the Pi with sudo reboot

3. Log in to the Pi again, and at the command prompt enter sudo modprobe w1-gpio

4. Then enter sudo modprobe w1-therm

5. Change directories to the /sys/bus/w1/devices directory by entering cd /sys/bus/w1/devices

6. Now enter ls to list the devices:

In my case, 28-000006637696 w1_bus_master1 is displayed.

7. Now enter cd 28-XXXXXXXXXXXX (change the X’s to your own address)

For example, in my case I would enter cd 28-000006637696

8. Enter cat w1_slave which will show the raw temperature reading output by the sensor:

Here the temperature reading is t=28625, which means a temperature of 28.625 degrees Celsius.

9. Enter cd to return to the root directory

That’s all that’s required to set up the one wire interface. Now you can run one of the programs below to output the temperature to an SSH terminal or to an LCD…"

I used the following website to setup the light resistor and MCP3008: https://littlebirdelectronics.com.au/guides/13/use-analogue-sensors-with-raspberry-pi
