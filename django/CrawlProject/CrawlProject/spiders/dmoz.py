import scrapy

class DmozSpider(scrapy.Spider):
	"""docstring for DmozSpider"""
	name = 'dmoz'
	allowed_domains = ['dmoz.org']
	status_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
		

	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)

