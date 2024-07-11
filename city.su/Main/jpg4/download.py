import requests
from bs4 import BeautifulSoup
import os
import re

def download_images(link_file, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read links from the file
    with open(link_file, 'r', encoding='utf-8') as file:
        links = file.readlines()
    
    # For each link, download the image
    for link in links:
        link = link.strip()
        if link:
            try:
                response = requests.get(link)
                response.raise_for_status()
                
                # Parse the HTML content to find the image
                soup = BeautifulSoup(response.text, 'html.parser')
                image_tag = soup.find('img', src=re.compile(r'^https://simp6\.host\.church'))
                
                if image_tag:
                    image_url = image_tag['src']
                    
                    # Download the image
                    image_response = requests.get(image_url)
                    image_response.raise_for_status()
                    
                    # Filename based on the image URL
                    image_name = os.path.basename(image_url)
                    image_path = os.path.join(output_directory, image_name)
                    
                    # Save the image
                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_response.content)
                    
                    print(f"Downloaded: {image_url} -> {image_path}")
                else:
                    print(f"No image found for the link: {link}")
            except requests.RequestException as e:
                print(f"Error retrieving {link}: {e}")

# Example usage
if __name__ == "__main__":
    # Get the absolute path of the currently executing script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Build paths relative to the script directory
    link_file = os.path.join(script_directory, 'output_jpg4.txt')
    output_directory = os.path.join(script_directory, 'images/')

    # Call the function with the relative paths
    download_images(link_file, output_directory)