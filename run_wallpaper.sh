#!/bin/sh

# Export the DISPLAY variable
export DISPLAY=:0

# Export the DBUS_SESSION_BUS_ADDRESS
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"

# Change to the directory containing the Python script
cd /home/siwhyatt/Pictures/Wallpapers

# Run the Python script
/usr/bin/python3 ./set_wallpaper.py
