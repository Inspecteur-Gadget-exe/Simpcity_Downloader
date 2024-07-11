# Simpcity_Downloader

---------------------------------------------------------------------------------------

<h2>"jpg4 folder"</h2>

<h3>You only have to execute "get_and_download.py" in this folder</h3>  

- **get_and_download.py**  
Prompt the user to enter the URL in the console and then copy the page source code.  
The source code is saved in a file named "source_code.txt".  
  
Retrieve all links starting with "https://jpg4.su/img/", excluding the link present multiple times in the code: "https://jpg4.su/img/YnBxSZe".  
Store these links in the file "output_jpg4.txt".  
  
Next, use the "subprocess" module to execute the following script.  
  
At the end of the script, delete the files "source_code.txt" and "output_jpg4.txt".  

- **download.py**  
  
For each link in the file "output_jpg4.txt", navigate to the website and download the image associated with the link "https://simp6.host.church".  
Store the downloaded images in the "images" directory.  

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
    
<h2>"saint2 folder"</h2>  

<h3>You only have to execute "1_source_code_copy.py" in this folder</h3>  

  
- **1_source_code_copy.py**  
Prompt the user to enter the URL in the console and then copy the page source code.  
  
- **1_source_code.txt**  
Create a file that contains the source code of the page :  
Exemple : https://simpcity.su/threads/sydney-sweeney.10961/page-41  
  
- **2_source_code_copy.py**  
Place all links starting with https://saint2.su/embed/ found in the previously copied source code into a directory named "urls".  
  
- **3_output_links.py**  
Copy the source code of all pages found in the "urls" directory and store them in the "sources" directory.  
Modify the URLs in the "sources" directory and move them to the file "3_modified_link.txt".
For the moment, I've only worked with 2 video hosts  
1) Old URL: https://saint2.su/d/  
2) New URL 1: https://simp2.saint2.su/api/download.php?file=  
3) New URL 2: https://papi2.saint2.su/api/download.php?file=  
  
- **4_download_modified_link.txt**  
Download the videos listed in the file "3_modified_link.txt".
  
---------------------------------------------------------------------------------------
