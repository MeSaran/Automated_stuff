#!/usr/bin/python
import requests,pprint,bs4

page=requests.get('https://dataquestio.github.io/web-scraping-pages/simple.html')
print(page)
print(page.status_code) #print status code
#print(page.content) #print the content of the page

#from bs4 import BeautifulSoup
#soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
#html=list(soup.children)[2]

#print(list(html.children))


#seond

#page2=requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')
#print(page2.status_code)

#from bs4 import BeautifulSoup
#soup1=BeautifulSoup(page2.content,'html.parser')
#print(list(soup1.children))
#print('find all ')
#print(soup1.find_all('p',class_='outer-text'))
#txt=[soup1.get_text() for e in soup1]
#print (txt[0])


#third
print('SCMS Site')
page3=requests.get('http://scmsgroup.org/sstm/objectives')
print(page3.status_code)

from bs4 import BeautifulSoup
soup2=BeautifulSoup(page3.content,'html.parser')
soup2.find_all('p',class_='head-h3')
txt=[soup2.get_text() for e in soup2]
print(txt[0])
