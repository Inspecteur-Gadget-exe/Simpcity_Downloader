import re
import subprocess
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

# Function to extract links from input_file and save them to output_file
def extract_links(input_file, output_file):
    # Regular expression to find links starting with "https://jpg4.su/" and exclude quotes
    pattern = r'https://jpg4\.su/img/\S+?(?="|\s|$)'
    
    # Read the content of the input file with 'utf-8' encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all matching links
    links = re.findall(pattern, content)
    
    # Filter out unwanted links
    links = [link for link in links if link != "https://jpg4.su/img/YnBxSZe"]
    
    # Write the found links to the output file with 'utf-8' encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

# Ask the user to input the URL
url = input("Please enter the URL of the page to save: ")

# Determine the script directory to save the file
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, 'source_code.txt')  # Filename to save the source code

save_webpage_source(url, filename)

if __name__ == "__main__":

    # Get the absolute path of the currently executing script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Build paths relative to the script directory
    input_file = os.path.join(script_directory, 'source_code.txt')
    output_file = os.path.join(script_directory, 'output_jpg4.txt')

    # Call the function with the relative paths
    extract_links(input_file, output_file)

    # Command to run the next script
    # Replace 'download.py' with the relative path of the script to run
    script_to_run = os.path.join(script_directory, 'download.py')
    command = ["python", script_to_run]

    # Execute the external program
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Output of the external program:\n{result.stdout.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error during the execution of the external program:\n{e.stderr.decode()}")

    # Delete the output file after running the external program
    try:
        os.remove(output_file)
        print(f"Deleted {output_file} successfully.")
    except OSError as e:
        print(f"Error deleting {output_file}: {e}")
    try:
        os.remove(input_file)
        print(f"Deleted {input_file} successfully.")
    except OSError as e:
        print(f"Error deleting {input_file}: {e}")
