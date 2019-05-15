import requests
from bs4 import BeautifulSoup
res = requests.get('http://jandan.net/ooxx')
html = BeautifulSoup(res.text,"html.parser")
comments = html.find_all('img')

print comments
for index, each in enumerate(comments):
	with open('{}.jpg'.format(index), 'wb') as jpg:
		jpg.write(requests.get(each.attrs['src'], stream=True).content)