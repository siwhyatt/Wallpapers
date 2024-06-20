import subprocess
import os.path
import os
import fnmatch
import random

def set_gnome_wallpaper(picture_path):
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(picture_path), shell=True)
    ##os.system('feh --bg-scale ' + picture_path)
    
def get_files(path,ext='*.'):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, ext):
            matches.append(os.path.join(root, filename))
    return matches

def set_random_wallpaper(destination_folder):
    path = f'/home/siwhyatt/Pictures/Wallpapers/{destination_folder}'
    imageExts = ['*.jpeg','*.jpg','*.JPG','*.png','*.PNG']
    files = []
    for ext in imageExts:
        files += get_files(path,ext)
    index = random.randint(0,len(files)-1)
    set_gnome_wallpaper(r'"' + files[index] + '"')
    print('Wallpaper Set!')

if __name__ == '__main__': 
    
    destination_folder = "Favourites"
    
    set_random_wallpaper(destination_folder)

