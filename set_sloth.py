import subprocess
import os.path
from sys import argv
import os
import fnmatch
import random

def set_gnome_wallpaper(picture_path):
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(picture_path), shell=True)
    ##os.system('feh --bg-scale ' + picture_path)

if __name__ == '__main__': 
    path = '/home/siwhyatt/Pictures/Wallpapers/Favourites/PygmySloth.jpg'
    set_gnome_wallpaper(path)
    print('Wallpaper Set!')