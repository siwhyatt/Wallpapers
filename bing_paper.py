from wallpaper import DeleteDownloads, DownloadAndSetBackgroundImage, SetAsFavourite
from bing_img import download_bing_image

image_folder = "/home/siwhyatt/Pictures/Wallpapers/Downloads/"
destination_folder = "/home/siwhyatt/Pictures/Wallpapers/Favourites/"
change_background = True


def main(image_folder, destination_folder, download_bing_image):
    # Delete images in downloads folder
    DeleteDownloads(image_folder)
    # Download image of the day from Bing    
    DownloadAndSetBackgroundImage(download_bing_image, image_folder)
    # Prompt to add to favourites
    SetAsFavourite(image_folder, destination_folder)


if __name__ == "__main__":
    main(image_folder, destination_folder, download_bing_image)
