# Simpcity_Downloader

- 1_source_code_copy.py
Prompt the user to enter the URL in the console and then copy the page source code.

- 1_source_code.txt
Create a file that contains the source code of the page :
Exemple : https://simpcity.su/threads/sydney-sweeney.10961/page-41

- 2_source_code_copy.py
Place all links starting with https://saint2.su/embed/ found in the previously copied source code into a directory named "urls".

- 3_output_links.py
Copy the source code of all pages found in the "urls" directory and store them in the "sources" directory.
Modify the URLs in the "sources" directory and move them to the file "3_modified_link.txt".
    Old URL: https://saint2.su/d/
    New URL 1: https://simp2.saint2.su/api/download.php?file=
    New URL 2: https://papi2.saint2.su/api/download.php?file=
For the moment, I've only worked with 2 video hosts

- 4_download_modified_link.txt
Download the videos listed in the file "3_modified_link.txt".
