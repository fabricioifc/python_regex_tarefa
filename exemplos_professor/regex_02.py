# coding: utf-8
import re
import requests

response = requests.get('http://ads.fraiburgo.ifc.edu.br')

if response.status_code == 200:
	texto = response.content.decode('utf-8')
	links = re.findall(r'<a href="(.*?)".*>(.*)</a>', texto)
	for url in links:
		print(url)