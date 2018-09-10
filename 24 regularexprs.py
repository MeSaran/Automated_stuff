#!/usr/bin/python
import re
def isPhonenum(phno):
	mail=re.compile(r'[a-zA-Z0-9.]+@[a-zA-Z.]+(\.[a-zA-Z]{2,4})')
	rsltmail=mail.search(phno)
	rsltmail2=mail.findall(phno) 
	phnum=re.compile(r'\d{3}-\d{3}-\d{4}')
	rslt=phnum.search(phno)
	rslt2=phnum.findall(phno)
	print('Number found: '+rslt.group())
	print(str(rslt2))
	print('Mail id: ',end='')	
	print(rsltmail)
	print(rsltmail2)
print('Enter some text and a ph no in this pattern, ***-***-****: ')
ph=input()
isPhonenum(ph)
#print(isPhonenum(ph))
