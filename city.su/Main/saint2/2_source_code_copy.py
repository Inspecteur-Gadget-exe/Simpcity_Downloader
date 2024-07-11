import requests
import os
import re
import subprocess

def save_webpage_source(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"The source code of {url} has been saved in {filename}.")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the page: {e}")

def extract_urls(filename, url_pattern, output_dir):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    os.makedirs(output_dir, exist_ok=True)
    
    urls = re.findall(url_pattern, content)
    for idx, url in enumerate(urls):
        output_file = os.path.join(output_dir, f'url_{idx + 1}.txt')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(url)
        print(f"URL saved to {output_file}")

# Script usage
script_directory = os.path.dirname(os.path.abspath(__file__))
source_filename = os.path.join(script_directory, '1_source_code.txt')  # Source code file from script 1
output_directory = os.path.join(script_directory, 'urls')  # Directory to save URLs

url_pattern = r'https://saint2\.su/embed/[^\s"]+'  # Pattern to match URLs

extract_urls(source_filename, url_pattern, output_directory)

# Command to run the next script
# Replace 'download_jpg4.py' with the relative path of the script to run
script_to_run = os.path.join(script_directory, '3_output_links.py')
command = ["python", script_to_run]

# Execute the external program
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Output of the external program:\n{result.stdout.decode()}")
except subprocess.CalledProcessError as e:
    print(f"Error during the execution of the external program:\n{e.stderr.decode()}")
