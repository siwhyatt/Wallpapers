import os
from typing import Callable

from bing_img import *
from set_wallpaper import *
from favourites import *


image_folder = "/home/siwhyatt/Pictures/Wallpapers/Downloads/"
destination_folder = "/home/siwhyatt/Pictures/Wallpapers/Favourites/"
change_background = True

def DeleteDownloads() -> None:
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
        # set_gnome_wallpaper(r'"' + os. getcwd() + "/"+ image_filename + '"')
    else:
        print("Failed to download the image.")


def SetAsFavourite() -> bool:
    # Get user input whether to save as favourite
    favourite = input("Save as favourite? Y/N:")

    if favourite.upper() == "Y":
        save_to_favourites(image_folder, destination_folder)
        return True
    else:
        print("Image will be deleted on next run")
        return False


def main():
    # Delete images in downloads folder
    DeleteDownloads()
    # Download image of the day from Bing    
    DownloadAndSetBackgroundImage(download_bing_image, image_folder)
    # Prompt to add to favourites
    SetAsFavourite()


if __name__ == "__main__":
    main()    
    
