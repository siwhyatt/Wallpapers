# Ubuntu-Wallpaper-Changer

Python scripts to download images from Bing or Nasa and set as background image

To use as is, clone repository into Pictures/Wallpaper and create folders Donwloads and Favourites (UK English spelling)
Alternatively create the directory structure you wish and edit the file paths accordingly.

bing_paper.py will download Bing image of the day and set as background image
nasa_paper.py will donload Nasa POD and set as background image - you will need to generate a free api key, save your url in a .env file and ensure you have the python-dotenv module installed
wallpaper.py contains helper functions for downloading and managing saved images - you will need to create and/or define Download and Favourites folders
set_wallpaper.py will randomly set wallpaper to an image saved in the favourites folder
