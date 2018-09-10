#!/usr/bin/python
import requests 
page=requests.get('https://www.instagram.com/sooraj.s__/')
print(page.status_code)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
soup.find_all(class_="")
txt=[soup.get_text() for m in soup]
print(txt[0])
newfile=open('text.txt','w')
newfile.write(txt[0])
newfile.close()
