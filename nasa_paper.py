from wallpaper import DeleteDownloads, DownloadAndSetBackgroundImage, SetAsFavourite
from nasa_img import download_nasa_apod

image_folder = "/home/siwhyatt/Pictures/Wallpapers/Downloads/"
destination_folder = "/home/siwhyatt/Pictures/Wallpapers/Favourites/"
change_background = True


def main(image_folder, destination_folder, download_nasa_apod):
    # Delete images in downloads folder
    DeleteDownloads(image_folder)
    # Download image of the day from Bing    
    DownloadAndSetBackgroundImage(download_nasa_apod, image_folder)
    # Prompt to add to favourites
    SetAsFavourite(image_folder, destination_folder)


if __name__ == "__main__":
    main(image_folder, destination_folder, download_nasa_apod)

