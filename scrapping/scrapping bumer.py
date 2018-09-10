#!/usr/bin/python
import requests,csv
page=requests.get('https://www.bloomberg.com/quote/SPX:IND')
print("status:",int(page.status_code))
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
#print(soup)
rslt=soup.find('div',attrs={'class':'price-container down'}).get_text()
print(rslt)
from datetime import datetime
with open('index.csv','a') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow([rslt,datetime.now()])


