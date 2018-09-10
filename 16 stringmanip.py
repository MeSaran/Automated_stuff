#!/usr/bin/python
spam='Hello world, Wass up'
print('sentence: '+spam)
print('Upper case: '+spam.upper())
print('Lower case:'+spam.lower())
while True:
	age=input('Enter your age')
	if age.isdecimal():
		break
	print('Please enter a decimal value')
