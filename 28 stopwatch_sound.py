#/usr/bin/python
import time,subprocess
timeleft=5
while timeleft>0:
	print('Show begins in: '+str(timeleft))
	time.sleep(1)
	timeleft-=1
vlcc='/usr/bin/vlc'
snd='/home/saran/Downloads/Up (2009)/Up.2009.720p.BluRay.x264.YIFY.mp4'
subprocess.call([vlcc,snd])
	
