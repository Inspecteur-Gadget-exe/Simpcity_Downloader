import re
import os
import requests

def save_webpage_source(url, filename):
    try:
        # Perform a GET request to obtain the page source
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Open a file in write mode
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the page content to the file
            file.write(response.text)

        print(f"The source code of {url} has been saved in {filename}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the page: {e}")

def extract_links(input_file, output_file):
    # Regular expression to find links starting with "https://cyberdrop.me/e/" and exclude quotes
    pattern = r'https://cyberdrop\.me/e/\S+?(?="|\s|$)'

    # Read the content of the input file with 'utf-8' encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all matching links
    links = re.findall(pattern, content)

    # Modify the links
    modified_links = [link.replace("https://cyberdrop.me/e/", "https://k1.cyberdrop.ch/api/file/d/") for link in links]

    # Write the found and modified links to the output file with 'utf-8' encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in modified_links:
            file.write(link + '\n')

def download_videos(link_file, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read links from the file
    with open(link_file, 'r', encoding='utf-8') as file:
        links = file.readlines()

    # For each link, download the file and save as mp4
    for link in links:
        link = link.strip()
        if link:
            try:
                response = requests.get(link)
                response.raise_for_status()

                # Filename based on the video URL, but save as .mp4
                original_name = os.path.basename(link)
                video_name = os.path.splitext(original_name)[0] + '.mp4'
                video_path = os.path.join(output_directory, video_name)

                # Save the video
                with open(video_path, 'wb') as video_file:
                    video_file.write(response.content)

                print(f"Downloaded: {link} -> {video_path}")
            except requests.RequestException as e:
                print(f"Error retrieving {link}: {e}")

if __name__ == "__main__":
    # Get the absolute path of the currently executing script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Ask the user to input the URL and the last page number
    url = input("Please enter the URL of the first page to save: ")
    last_page_url = input("Please enter the URL of the last page: ")

    # Extract the base URL and the range of pages
    base_url = url.rsplit('/', 1)[0]
    
    # Determine the first page number
    if 'page-' in url:
        first_page_number = int(url.rsplit('-', 1)[-1])
    else:
        first_page_number = 1

    # Extract the last page number
    last_page_number = int(last_page_url.rsplit('-', 1)[-1])

    # Create directories for storing source code and extracted links
    source_dir = os.path.join(script_directory, 'sources')
    links_dir = os.path.join(script_directory, 'links')
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(links_dir, exist_ok=True)

    for i in range(first_page_number, last_page_number + 1):
        page_url = f"{base_url}/page-{i}" if i > 1 else url
        source_filename = os.path.join(source_dir, f'source_code_page_{i}.txt')
        
        # Save the webpage source
        save_webpage_source(page_url, source_filename)

        # Build paths relative to the script directory
        output_file = os.path.join(links_dir, f'output_cyberdrop_page_{i}.txt')

        # Extract links from the saved source code
        extract_links(source_filename, output_file)

    # Directory to save downloaded videos
    output_directory = os.path.join(script_directory, 'Videos/')
    
    # Download videos from the extracted links
    for i in range(first_page_number, last_page_number + 1):
        link_file = os.path.join(links_dir, f'output_cyberdrop_page_{i}.txt')
        download_videos(link_file, output_directory)
        print(f"All videos from page {i} have been downloaded.")

    # Delete the directories after processing
    try:
        for file in os.listdir(links_dir):
            os.remove(os.path.join(links_dir, file))
        os.rmdir(links_dir)
        print(f"Deleted {links_dir} successfully.")
    except OSError as e:
        print(f"Error deleting {links_dir}: {e}")

    try:
        for file in os.listdir(source_dir):
            os.remove(os.path.join(source_dir, file))
        os.rmdir(source_dir)
        print(f"Deleted {source_dir} successfully.")
    except OSError as e:
        print(f"Error deleting {source_dir}: {e}")
