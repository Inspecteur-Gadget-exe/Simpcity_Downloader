import os
import requests
import shutil

# Filename containing URLs
input_file = 'city.su/Main/saint2/3_modified_link.txt'
source_code_file = 'city.su/Main/saint2/1_source_code.txt'

# Directory where videos will be stored
output_directory = 'city.su/Main/saint2/videos'

# Subdirectories to delete
urls_directory = 'city.su/Main/saint2/urls'
sources_directory = 'city.su/Main/saint2/sources'

# Create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read URLs from the file
with open(input_file, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Download and save content for each URL
for i, url in enumerate(urls, start=1):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(output_directory, f'file_{i}.mp4')
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Content downloaded and saved to {file_name}")
    else:
        print(f"Error downloading {url}, status: {response.status_code}")

# Remove the "urls" and "sources" subdirectories
try:
    shutil.rmtree(urls_directory)
    print(f"The subdirectory '{urls_directory}' has been removed.")
except FileNotFoundError:
    print(f"The subdirectory '{urls_directory}' does not exist.")
except Exception as e:
    print(f"Error while removing the subdirectory '{urls_directory}': {e}")

try:
    shutil.rmtree(sources_directory)
    print(f"The subdirectory '{sources_directory}' has been removed.")
except FileNotFoundError:
    print(f"The subdirectory '{sources_directory}' does not exist.")
except Exception as e:
    print(f"Error while removing the subdirectory '{sources_directory}': {e}")

# Remove the files "1_source_code.txt" and "3_modified_link.txt"
files_to_delete = [input_file, source_code_file]

for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error while deleting the file '{file_path}': {e}")
