#pip install requests
#pip install html5lib
#pip install bs4

import requests
from bs4 import BeautifulSoup as bs  #For parsing
import csv

# Accessing html

URL = "https://www.passiton.com/inspirational-quotes"   
response= requests.get(URL) 

#parsing html content           
        
soup = bs(response.content,'html5lib')  #html5lib : Specifying the HTML parser we want to use.
#print(soup.prettify)    #it gives the visual representation of the parse tree created from the raw HTML content.

#Searching and navigating through the parse tree

quotes=[]  # a list to store quotes
table = soup.find('div', attrs = {'id':'all_quotes'})
for row in table.findAll('div',attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    print(row)