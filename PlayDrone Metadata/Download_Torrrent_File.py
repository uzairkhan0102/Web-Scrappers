import requests
import urllib2
from BeautifulSoup import BeautifulSoup





def trade_spider(max_links):
    page = 2
    count = 0
    pre = 'https://archive.org'
    while page <= max_links:
        if page == 1:
            url='https://archive.org/details/playdrone-metadata'
        else:
            url='https://archive.org/details/playdrone-metadata?&sort=-downloads&page=' +str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div', {'class': 'item-ttl C C2'}):
            for implink in link.findAll('a'):
                href = implink.get('href')
                compurl = pre+str(href)
                count =count +1
                try:
                    get_torrent(compurl,count)
                except Exception as e:
                    print ""
                
        page +=1
        


        
def get_torrent(torrent_url,count):
    source_code = requests.get(torrent_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for torrent in soup.findAll('a', {'class': 'format-summary download-pill'}):    
        href = torrent.get('href')
        comptorrent  = 'https://archive.org' + str(href)
        print comptorrent
        
        down_torrent(comptorrent,count)


def down_torrent (url,count):
    torrent_name = "torrent"+str(count)+'.torrent' 
    with open(str(torrent_name), "wb") as T:
        T.write(urllib2.urlopen(url).read())
        print "downloaded " + str(torrent_name)
        
    


trade_spider(2)






