import requests
import os
import subprocess

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

# Ask the user to input the URL
url = input("Please enter the URL of the page to save: ")

# Determine the script directory to save the file
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, '1_source_code.txt')  # Filename to save the source code

save_webpage_source(url, filename)

# Command to run the next script
# Replace 'download_jpg4.py' with the relative path of the script to run
script_to_run = os.path.join(script_directory, '2_source_code_copy.py')
command = ["python", script_to_run]

# Execute the external program
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Output of the external program:\n{result.stdout.decode()}")
except subprocess.CalledProcessError as e:
    print(f"Error during the execution of the external program:\n{e.stderr.decode()}")
