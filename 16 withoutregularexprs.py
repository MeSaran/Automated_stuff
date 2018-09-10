#!/usr/bin/python
def isPhonenum(phno):
	if len(phno) != 12:		
		return False
	for i in range(0,3):
		if not phno[i].isdecimal():
			return False
	if phno[3]!='-':
		return False
	for i in range(4,7):
		if not phno[i].isdecimal():
			return False
	if phno[7] != '-':
		return False
	for i in range(8,12):
		if not phno[i].isdecimal():
			return False
	return True
print('Enter some text and a ph no in this pattern, ***-***-****: ')
ph=input()
for i in range(len(ph)):
	chunk=ph[i:i+12]
	print('text'+chunk)
	if isPhonenum(chunk):
		print('Phone no found!!!')
#print(isPhonenum(ph))
