# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re


url = "https://www.xe.com/symbols.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

result = soup.findAll('tr')
for i in result:
	print(i.findAll('td')[2])
