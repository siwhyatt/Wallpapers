import os
from typing import Callable

from bing_img import *
from set_wallpaper import *
from favourites import *


image_folder = "Downloads/"
destination_folder = "Favourites/"
change_background = True

def DeleteDownloads() -> None:
    # Delete previous downloads
    for f in os.listdir(image_folder):
        os.remove(os.path.join(image_folder, f))

def DownloadAndSetBackgroundImage(ImgFunc: Callable, image_folder: str) -> None:
    # Download the Image of the Day and get the image filename
    image_filename = ImgFunc(image_folder)

    if image_filename:
        print(f"Image downloaded and saved to: {image_filename}")
        set_gnome_wallpaper(r'"' + os. getcwd() + "/"+ image_filename + '"')
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

    # while change_background == True:
    #     time.sleep(3600)
    #     set_random_wallpaper(destination_folder)
    #

if __name__ == "__main__":
    main()    
    
