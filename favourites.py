import os
import shutil


source_folder = "Downloads/"
destination_folder = "Favourites/"


def save_to_favourites(source_folder, destination_folder):

    source_folder = source_folder
    destination_folder = destination_folder

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('Copied to favourites:', file_name)


def main():
    save_to_favourites(source_folder, destination_folder)


if __name__ == "__main__":
    main()
    
