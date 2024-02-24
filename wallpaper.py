import time

from bing_img import *
from set_wallpaper import *
from favourites import *

if __name__ == "__main__":
    # Specify the folder where you want to save the Bing images
    
    image_folder = "Downloads"
    destination_folder = "Favourites"
    change_background = True

    # Delete previous downloads
    for f in os.listdir(image_folder):
        os.remove(os.path.join(image_folder, f))

    # Download the Bing Image of the Day and get the image filename
    image_filename = download_bing_image(image_folder)

    if image_filename:
        print(f"Image downloaded and saved to: {image_filename}")
    else:
        print("Failed to download the image.")

    set_gnome_wallpaper(r'"' + os. getcwd() + "/"+ image_filename + '"')

    favourite = input("Save as favourite? Y/N:")

    if favourite == "Y" or "y":
        save_to_favourites(image_folder, destination_folder)

    else:
        print("Image will be deleted on next run")


    while change_background == True:
        time.sleep(3600)
        set_random_wallpaper(destination_folder)


    


