#!/usr/bin/python
import time
input()
print('started')
start=time.time()
end=start
lap=1
try:
	while True:
		input()
		laptime=round(time.time()-end,2)
		tottime=round(time.time()-start,2)
		print('Lap %s: %s %s'%(lap,tottime,laptime))		
		lap+=1
		last=time.time()
except KeyboardInterrupt:
	print('\nDone')
