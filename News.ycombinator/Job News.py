# -*- coding: cp1252 -*-
import requests
import re
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/jobs"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')


for head1 in soup.findAll('a', {'class': 'storylink'}):
    headings1 = head1.get_text()
    #headings1 = headings1.encode('utf8')
    #fh = open("Hello.csv", "a")
    #fh.write(headings1+'\n')
    
    name = re.split('; |, | [ iI]s|\(|–',headings1)
    pos = re.split('; |[Ll]ooking|[Ff]or|[ iI]s|[Hh]iring',headings1)
    #print pos[0]
    print name [0]
    #print headings1
    #print code [0]

for span in soup.findAll('span', {'class': 'sitebit comhead'}):
    span_text = span.get_text()
    #headings1 = headings1.encode('utf8')
    #fh = open("Hello.csv", "a")
    #fh.write(headings1+'\n')
    #print span_text
    
