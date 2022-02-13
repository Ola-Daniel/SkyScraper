from bs4 import BeautifulSoup
import html5lib
import requests
import csv


URL = input('Please input a valid URL: ')
scheme = "https://"
if scheme in URL:
    URL = URL
else:
    URL = scheme + URL
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())


