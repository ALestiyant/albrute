import os, subprocess

try:
	import requests,mechanize,concurrent.futures,rich
except:os.system("pip uninstall requests -y;pip install requests && pip uninstall bs4 -y;pip install bs4 && pip uninstall mechanize -y;pip install mechanize && pip uninstall concurrent.futures -y;pip install concurrent.futures && pip uninstall rich -y;pip install rich")

try:
	notif = open(os.devnull, "w")
	notification = subprocess.call(["dpkg","-s","play-audio"],stdout=notif,stderr=subprocess.STDOUT)
	notif.close()
	if notification !=0:
		os.system('pkg install play-audio' )
except FileNotFoundError:
	os.system('pkg install play-audio' )
	os.system('pkg install espeak -y')
from assets.meta import data
data()