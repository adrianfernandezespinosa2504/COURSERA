# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:35:45 2026

@author: Adrian
"""

import requests
from bs4 import BeautifulSoup
import os

# Step 1: Send an HTTP request to the webpage
url = 'https://etsi.us.es'  # Replace with the actual URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print('Failed to retrieve the webpage.')
    exit()

# Step 2: Find the document link
document_link = soup.find('a', {'class': 'download-link'})['href']

# Print the document link to verify
print('Document link found:', document_link)

# Handle relative URLs
base_url = 'https://etsi.us.es'  # The base URL of the website
full_url = os.path.join(base_url, document_link)

print('Full URL:', full_url)

# Step 3: Download the document
document_response = requests.get(full_url)

# Check if the document request was successful
if document_response.status_code == 200:
    # Save the document to a file
    with open('report.pdf', 'wb') as file:
        file.write(document_response.content)
    print('Document downloaded successfully.')
else:
    print('Failed to download the document. Status code:', document_response.status_code)