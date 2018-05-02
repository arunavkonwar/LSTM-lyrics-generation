# https://stackoverflow.com/questions/30631480/using-python-to-visit-a-link-and-print-data/30631564

from pyquery import PyQuery as pq
from lxml import etree
import requests
from bs4 import BeautifulSoup
import csv

# this visits the website
response = requests.get('http://www.metrolyrics.com/taylor-swift-lyrics.html')

# this separates the different types of content
doc = pq(response.content)

# this finds the titles in the content
titles = doc('.title')


# this visits each title, then prints each verse
for title in titles:
	# this visits each title
	f = open("test.txt", "a+")
	#response_title = requests.get(title)
	response_title = requests.get(title.attrib['href'])

	# this separates the content
	doc2 = pq(response_title.content)
	# this finds the song lyrics
	verse = doc2('.verse')
	# this prints the song lyrics
	print verse.text()

	f.write(verse.text().encode('utf-8').strip())
	
	f.close()




