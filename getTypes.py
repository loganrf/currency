# This script pulls in an html table of currency types and then parses it into a csv file
# Data imported includes country/currency name, code, and unicode symbol
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

def parseCode(codeString):
	
	findIndex = codeString.find(',')
	if(findIndex!=-1):
		indices = [findIndex]
		while(findIndex!=-1):
			findIndex = codeString.find(',',indices[-1]+1)
			if(findIndex!=-1):
				indices+=[findIndex]

		codes = []
		startIndex = 0
		for i in range(len(indices)):
			codes+=[codeString[startIndex:indices[i]]]
			startIndex = indices[i]+1
		codes+=[codeString[startIndex:]]

		rstr = ''
		for i in codes:
			rstr+=chr(int(i))

		return rstr

	else:
		return chr(int(codeString))

#This is a general scraping script to be used with an arbitrary html table of values
url = ""
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

result = soup.findAll('tr')

numResults = len(result)-10

countryName = []
codes = []
uni = []

for i in range(numResults):
	#Change indices as necessary for your source document
	countryName+=[result[i+1].findAll('td')[0].text]
	codes+=[result[i+1].findAll('td')[1].text]
	uni+=[result[i+1].findAll('td')[5].text]

for i in uni:
	if(i!=''):
		print(parseCode(i))


outputFile = open('currencyData.csv','w+')

i = len(countryName)

for j in range(i):
	if(uni[j]!=''):
		outputFile.write(countryName[j]+';'+codes[j]+';'+parseCode(uni[j])+'\n')
	else:
		outputFile.write(countryName[j]+';'+codes[j]+';NONE\n')

outputFile.close()
