import os
import shutil
from typing import Callable

from set_wallpaper import *


image_folder = "~/Pictures/Wallpapers/Downloads/"
destination_folder = "~/Pictures/Wallpapers/Favourites/"
change_background = True

def DeleteDownloads(image_folder) -> None:
    # Delete previous downloads
    print("Deleting old images")
    if len(os.listdir(image_folder)) > 0:
        for f in os.listdir(image_folder):
            os.remove(os.path.join(image_folder, f))
            print(f"{os.path.join(image_folder, f)} removed")
    else:
        print("Downloads folder is empty")

def DownloadAndSetBackgroundImage(ImgFunc: Callable, image_folder: str) -> None:
    # Download the Image of the Day and get the image filename
    print("Attempting to download image")
    image_filename = ImgFunc(image_folder)

    if image_filename:
        print(f"Image downloaded and saved to: {image_filename}")
        set_gnome_wallpaper(r'"' + image_filename + '"')
    else:
        print("Failed to download the image.")


def save_to_favourites(source_folder, destination_folder):

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('Copied to favourites:', file_name)


def SetAsFavourite(image_folder, destination_folder) -> bool:
    # Get user input whether to save as favourite
    favourite = input("Save as favourite? Y/N:")

    if favourite.upper() == "Y":
        save_to_favourites(image_folder, destination_folder)
        return True
    else:
        print("Image will be deleted on next run")
        return False
