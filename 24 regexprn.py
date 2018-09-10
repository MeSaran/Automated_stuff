#!/usr/bin/python
import re
def isPhoneno(num):
	#phexrp=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	try:	
		indphnexpp=re.compile(r'\d\d-\d{10}')
		indrslt=indphnexpp.findall(num)
		print(indrslt)
	#result=phexrp.search(num)
	#print('phone no is: '+result.group())
	except AttributeError as error:
		print ('in valid no')
	#print('Indian no: +'+tuple(indrslt.groups()))
phno=input('Enter the messsage with a phone in it')
isPhoneno(phno)
