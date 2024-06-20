import requests
import os
from set_wallpaper import set_gnome_wallpaper

image_folder = "Downloads"

def download_nasa_apod(image_folder):
    # Bwng Image of the Day URL
    url = "https://api.nasa.gov/planetary/apod?api_key=gi9vbuqnAwKfDRDHCqcoaviKvPwFx3RLfixRPekX"

    try:
        # Send an HTTP GET request to the NASA API
        response = requests.get(url)
        print(response.raise_for_status())
        
        # Parse the JSON response
        data = response.json()
        
        if data['media_type'] != "video":
            # Get the relative image URL
            image_url = data['hdurl']
            
            # Send an HTTP GET request to download the image
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Read the image data
            image_data = image_response.content
            
            # Create a folder if it doesn't exist
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
                
            # Generate a user-friendly and unique filename
            title = data['title']
            image_filename = os.path.join(image_folder, f"{title}.jpg")
            
            
            # Save the image to the specified folder
            with open(image_filename, 'wb') as image_file:
                image_file.write(image_data)
            
            return image_filename

        else:
            video_url = data['url']
            print(f'No image today, view video: {video_url}')
            return None

    except Exception as e:
        print("Error:", e)
        return None


def main():
    for f in os.listdir(image_folder):
        os.remove(os.path.join(image_folder, f))

    # Download the Nasa Image of the Day and get the image filename
    image_filename = download_nasa_apod(image_folder)

    if image_filename:
        print(f"Image downloaded and saved to: {image_filename}")
    else:
        print("Failed to download the image.")

    set_gnome_wallpaper(r'"' + os. getcwd() + "/"+ image_filename + '"')


if __name__ == "__main__":
    main()

    
