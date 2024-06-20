import requests
#from PIL import Image
import os
#import datetime
from set_wallpaper import set_gnome_wallpaper

image_folder = "Downloads"

def download_bing_image(image_folder):
    # Bing Image of the Day URL
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

    try:
        # Send an HTTP GET request to the Bing API
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Get the relative image URL
        image_url = data['images'][0]['url']
        
        # Construct the full image URL
        full_image_url = f"https://www.bing.com{image_url}"
        
        # Send an HTTP GET request to download the image
        image_response = requests.get(full_image_url)
        image_response.raise_for_status()
        
        # Read the image data
        image_data = image_response.content
        
        # Create a folder if it doesn't exist
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            
        # Generate a user-friendly and unique filename
        title = data['images'][0]['title']
        image_filename = os.path.join(image_folder, f"{title}.jpg")
        
        
        # Save the image to the specified folder
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_data)
        
        return image_filename

    except Exception as e:
        print("Error:", e)
        return None


def main():
    for f in os.listdir(image_folder):
        os.remove(os.path.join(image_folder, f))

    # Download the Bing Image of the Day and get the image filename
    image_filename = download_bing_image(image_folder)

    if image_filename:
        print(f"Image downloaded and saved to: {image_filename}")
    else:
        print("Failed to download the image.")

    set_gnome_wallpaper(r'"' + os. getcwd() + "/"+ image_filename + '"')


if __name__ == "__main__":
    main()

    
