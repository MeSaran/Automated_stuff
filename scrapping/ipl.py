#!/usr/bin/python
import requests
page=requests.get('https://www.gsmarena.com/nokia_x6-9178.php')
print(page.status_code)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
#print(soup)
results=soup.find_all('table', attrs={'cellspacing':'0'})
print(len(results))
first_result=results[-2]
list(first_result)
print(len(first_result))
lst=[]
for rslt in first_result:
	#print('hello')	
	#print(i)
	a=first_result.find('td',class_='ttl').get_text()
	b=first_result.find('td',class_='nfo').get_text()
	lst.append((a,b))
print(lst)
#print(first_result.find('td',class_='nfo'))


