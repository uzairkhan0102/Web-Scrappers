#libraries we need tu login and extract data
import re
import config
import requests
from bs4 import BeautifulSoup
import urllib2
import urllib
from robobrowser import RoboBrowser


#Lgoin
talha = RoboBrowser(parser='html.parser')
talha.open("http://visual.ic.uff.br/dmi/")
form = talha.get_form()
#user_id 
form['usuario'] = "talha1621"
#submit form 
talha.submit_form(form)
src = str(talha.parsed())
#values for how much user data you want to extract
#print  "Enter Starting ID: "
page = 1
max_links = 2
count = 0

#main loop to extract data after login
while page <= max_links:
    
    #goto these pages alteratively after login
    talha.open("http://visual.ic.uff.br/dmi/prontuario/details.php?id=" +str(page))
    src1 = str(talha.parsed())
    
    #loop to get user id and user age
    #goto this tag "div" having 'class' "description"
    
    for implink in talha.find_all('div', {'class': 'descripcion1'}):
        
        #find all "p" tags in above div
        desc = implink.find_all('p')
        
        #loop to find user id and age in specific "p" having 'class' "titulo2"
        for image in implink.find_all('p', {'class': 'titulo2'}):
            #get user ID
            href = image.string
            descd = desc[2].string
            print href
            
            #get user age
            age = descd.find(' ')
            age = descd[age+1:age+3]
            print age

    #loop to find user daignosis
    #go to "div" tag having 'class' "visitauser"
    for diag in talha.find_all('div', {'class': 'visitauser'}):
        #in the above "div" go to "p" tag having 'class' "view-diagnostico" 
        for pat in diag.find_all('p', {'class': 'view-diagnostico'}):
            
            #get the text present in "span" tag
            daignosis = pat.find('span').get_text()
            print daignosis

    #loop to get the static-frontal image of the patient
    #goto "div" tag having 'class' "iamgem"
    i = 0
    for img in talha.find_all('div', {'class': 'imagem'}):

     #in above div, goto the "a" tag having 'title' "Static - Frontal"
        for cl in img.find_all('a', {'title': 'Static - Frontal'}):

            #in "a" tag, get the "href"
            patient = cl.get('href')
            
            #modify the link according to our desire
            patient = patient[3:len(patient)]
            count = count+1
            link =  "http://visual.ic.uff.br/dmi/"+patient
            print link
            #get the image present in the link
            urllib.urlretrieve(link, str(daignosis)+"_"+str(age)+"_"
                               +str(href[4:])+"_"+str('S')+".jpg" )
        

        
        #in above div, goto the "a" tag having 'title' "Dinamic - Frontal"
        for cl in img.find_all('a', {'title': 'Dinamic - Frontal'}):

            
            #in "a" tag, get the "href"
            patient = cl.get('href')
            #modify the link according to our desire
            patient = patient[3:len(patient)]
            count = count+1
            link =  "http://visual.ic.uff.br/dmi/"+patient

            
            
            #get the image present in the link
            urllib.urlretrieve(link, str(daignosis)+"_"+str(age)+
                               "_"+str(href[4:])+"_"+str('D')+str(i-5)+".jpg" )
            print link
        i = i+1
        
    page = page+1
