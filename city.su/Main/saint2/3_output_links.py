import os
import re
import requests
import subprocess

def modify_link(link):
    old_prefix = "https://saint2.su/d/"
    new_prefix_1 = "https://simp2.saint2.su/api/download.php?file="
    new_prefix_2 = "https://papi2.saint2.su/api/download.php?file="
    
    if link.startswith(old_prefix):
        modified_link_1 = link.replace(old_prefix, new_prefix_1).rstrip('=')
        modified_link_2 = link.replace(old_prefix, new_prefix_2).rstrip('=')
        
        modified_link_1 = modified_link_1.strip("'").strip(",")
        modified_link_2 = modified_link_2.strip("'").strip(",")
        
        return modified_link_1, modified_link_2
    else:
        raise ValueError("The link does not start with the expected prefix.")

def save_webpage_source(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"The source code of {url} has been saved in {filename}.")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the page: {e}")

def process_url_files(input_dir, source_dir, output_file):
    url_files = [f for f in os.listdir(input_dir) if f.startswith('url_') and f.endswith('.txt')]
    
    os.makedirs(source_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as output:
        for url_file in url_files:
            input_path = os.path.join(input_dir, url_file)
            with open(input_path, 'r', encoding='utf-8') as file:
                url = file.read().strip()
                
            source_filename = os.path.join(source_dir, f'source_{url_file}')
            save_webpage_source(url, source_filename)
            
            with open(source_filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            links = re.findall(r'https://saint2\.su/d/[^\s"]+', content)
            for link in links:
                try:
                    modified_link_1, modified_link_2 = modify_link(link)
                    output.write(modified_link_1 + '\n')
                    output.write(modified_link_2 + '\n')
                    print(f"Processed {link} to {modified_link_1} and {modified_link_2}")
                except ValueError as e:
                    print(f"Error: {e}")

# Script usage
script_directory = os.path.dirname(os.path.abspath(__file__))
url_directory = os.path.join(script_directory, 'urls')  # Directory where URL files are stored
source_directory = os.path.join(script_directory, 'sources')  # Directory to save webpage sources
output_file = os.path.join(script_directory, '3_modified_link.txt')  # File to save modified links

process_url_files(url_directory, source_directory, output_file)

# Command to run the next script
# Replace 'download_jpg4.py' with the relative path of the script to run
script_to_run = os.path.join(script_directory, '4_download_modified_link.py')
command = ["python", script_to_run]

# Execute the external program
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Output of the external program:\n{result.stdout.decode()}")
except subprocess.CalledProcessError as e:
    print(f"Error during the execution of the external program:\n{e.stderr.decode()}")
