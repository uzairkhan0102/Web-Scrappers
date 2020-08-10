import urllib
import urllib2
import requests
import os
import re
from bs4 import BeautifulSoup
import csv


url = "https://www.unilever.nl/"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')


href = []
for all_links in soup.findAll('a'):
    href.append(all_links.get('href'))

counter = len(href)
print counter

def trade_spider(page_url, count):

    source_code = requests.get(page_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    
    fh = open("Hello"+str(count)+".csv", "a")

    fh.write ('\n All Headings \n')

    for head1 in soup.findAll('h1'):
        headings1 = head1.get_text()
        headings1 = headings1.encode('utf8')
        fh = open("Hello"+str(count)+".csv", "a")
        fh.write(headings1+'\n')
        #print headings1

    for head2 in soup.findAll('h2'):
        headings2 = head2.get_text()
        headings2 = headings2.encode('utf8')
        fh = open("Hello"+str(count)+".csv", "a")
        fh.write(headings2+'\n')
        #print headings2

    for head3 in soup.findAll('h3'):
        headings3 = head3.get_text()
        headings3 = headings3.encode('utf8')
        fh = open("Hello"+str(count)+".csv", "a")
        fh.write(headings3+'\n')
        #print headings3
        

    fh = open("Hello"+str(count)+".csv", "a")
    fh.write('\n All Paragraphs \n')
    for link in soup.findAll('p'):
        text = link.get_text()
        text = text.encode('utf8')
        fh = open("Hello"+str(count)+".csv", "a")
        #fh.write('\n'+text+'\n')
        fh.write(text+'\n')
        #print text

    fh = open("Hello"+str(count)+".csv", "a")
    fh.write('\n All Links \n')
    for links in soup.findAll('li'):
        link_text = links.get_text()
        link_text = link_text.encode('utf8')
        fh = open("Hello"+str(count)+".csv", "a")
        fh.write(link_text+'\n')
        #f.write(headings1)
        #print link_text
    


i = 1
while i <= counter:
    
    if i==1:
        trade_spider(url, i)
    else:
        if 'https:/' in href[i]:
            print "Not added"
        else:
            url_upd = url+str(href[i])
            print url_upd
            trade_spider(url_upd, i)

    i = i+1


