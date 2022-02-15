# Python program to scrape websites and save content from website
from bs4 import BeautifulSoup
import html5lib
import requests
import csv
import os

search_id = "up"
#    TEST_URL = "nairaland.com"
URL = input('Please input a URL: ')
#  inplement feature that allows script to take a file containing multiple urls or a single url
scheme = "https://"
if scheme in URL:
    URL = URL
else:
    URL = scheme + URL
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
result = soup.find(id=search_id)
print(result)



