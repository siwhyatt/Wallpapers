import requests
import os
from dotenv import load_dotenv


def download_nasa_apod(image_folder):

    # Get the directory of the current file
    module_dir = os.path.dirname(os.path.abspath(__file__))
    # Path to the .env file
    dotenv_path = os.path.join(module_dir, '.env')
    # Load the .env file
    load_dotenv(dotenv_path=dotenv_path)

    url = str(os.getenv('URL'))

    try:
        # Send an HTTP GET request to the NASA API
        response = requests.get(url)
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

