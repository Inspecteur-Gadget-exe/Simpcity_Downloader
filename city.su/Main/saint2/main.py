import re
import os
import requests
import shutil

def save_webpage_source(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"The source code of {url} has been saved in {filename}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the page: {e}")

def clean_link(link):
    link = re.sub(r'</?[^>]+>', '', link)  # Remove HTML tags
    link = re.sub(r'\s', '', link)  # Remove any whitespace
    return link.strip()

def extract_embed_links(input_file, output_file):
    pattern = r'https://saint2\.su/embed/[^\s">]+'

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    links = re.findall(pattern, content)
    cleaned_links = list(set(clean_link(link) for link in links))  # Remove duplicates and clean links

    with open(output_file, 'w', encoding='utf-8') as file:
        for link in cleaned_links:
            file.write(link + '\n')

    print(f"Extracted {len(cleaned_links)} unique embed links from {input_file}")

def extract_download_links(input_file, output_file):
    pattern = r'https://saint2\.su/d/[^\s">]+'

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    links = re.findall(pattern, content)
    cleaned_links = list(set(clean_link(link) for link in links))  # Remove duplicates and clean links

    with open(output_file, 'w', encoding='utf-8') as file:
        for link in cleaned_links:
            file.write(link + '\n')

    print(f"Extracted {len(cleaned_links)} unique download links from {input_file}")

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

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

def download_videos(link_file, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(link_file, 'r', encoding='utf-8') as file:
        links = file.readlines()

    counter = 1  # Initialize a counter for file naming

    for link in links:
        link = link.strip()
        if link:
            try:
                modified_link_1, modified_link_2 = modify_link(link)
                for modified_link in [modified_link_1, modified_link_2]:
                    print(f"Trying to download from: {modified_link}")
                    response = requests.get(modified_link)
                    if response.status_code == 200:
                        file_name = f'video_{counter}.mp4'  # Use the counter for naming
                        file_path = os.path.join(output_directory, file_name)
                        with open(file_path, 'wb') as video_file:
                            video_file.write(response.content)
                        print(f"Downloaded: {modified_link} -> {file_path}")
                        counter += 1  # Increment the counter after each successful download
                        break  # Stop trying alternative links once the download is successful
                    else:
                        print(f"Error downloading {modified_link}, status: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error retrieving {link}: {e}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))

    url = input("Please enter the URL of the first page to save: ")
    last_page_url = input("Please enter the URL of the last page: ")

    base_url = url.rsplit('/', 1)[0]
    
    if 'page-' in url:
        first_page_number = int(url.rsplit('-', 1)[-1])
    else:
        first_page_number = 1

    last_page_number = int(last_page_url.rsplit('-', 1)[-1])

    source_dir = os.path.join(script_directory, 'sources')
    embed_links_dir = os.path.join(script_directory, 'embed_links')
    download_links_dir = os.path.join(script_directory, 'download_links')
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(embed_links_dir, exist_ok=True)
    os.makedirs(download_links_dir, exist_ok=True)

    for i in range(first_page_number, last_page_number + 1):
        page_url = f"{base_url}/page-{i}" if i > 1 else url
        source_filename = os.path.join(source_dir, f'source_code_page_{i}.txt')
        
        save_webpage_source(page_url, source_filename)

        embed_output_file = os.path.join(embed_links_dir, f'embed_links_page_{i}.txt')
        extract_embed_links(source_filename, embed_output_file)

    for embed_links_file in os.listdir(embed_links_dir):
        embed_links_path = os.path.join(embed_links_dir, embed_links_file)
        with open(embed_links_path, 'r', encoding='utf-8') as file:
            embed_links = file.readlines()

        for embed_link in embed_links:
            embed_link = embed_link.strip()
            if embed_link:
                source_filename = os.path.join(source_dir, f'source_code_embed_{os.path.basename(embed_link)}.txt')
                save_webpage_source(embed_link, source_filename)
                download_output_file = os.path.join(download_links_dir, f'download_links_{os.path.basename(embed_link)}.txt')
                extract_download_links(source_filename, download_output_file)

    combined_download_links_file = os.path.join(script_directory, 'combined_download_links.txt')
    with open(combined_download_links_file, 'w', encoding='utf-8') as combined_file:
        for download_links_file in os.listdir(download_links_dir):
            download_links_path = os.path.join(download_links_dir, download_links_file)
            with open(download_links_path, 'r', encoding='utf-8') as file:
                combined_file.write(file.read())

    output_directory = os.path.join(script_directory, 'Videos/')
    download_videos(combined_download_links_file, output_directory)

    try:
        shutil.rmtree(embed_links_dir)
        print(f"Deleted {embed_links_dir} successfully.")
    except OSError as e:
        print(f"Error deleting {embed_links_dir}: {e}")

    try:
        shutil.rmtree(download_links_dir)
        print(f"Deleted {download_links_dir} successfully.")
    except OSError as e:
        print(f"Error deleting {download_links_dir}: {e}")

    try:
        shutil.rmtree(source_dir)
        print(f"Deleted {source_dir} successfully.")
    except OSError as e:
        print(f"Error deleting {source_dir}: {e}")

    # Delete the combined download links file
    try:
        os.remove(combined_download_links_file)
        print(f"Deleted {combined_download_links_file} successfully.")
    except OSError as e:
        print(f"Error deleting {combined_download_links_file}: {e}")
