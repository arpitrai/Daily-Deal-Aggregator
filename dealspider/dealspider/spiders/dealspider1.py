from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from dealspider.items import DealspiderItem

import os, sys
sys.path.append('C:/apps/testdeals')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from deals.models import Deal, DealForm

class DealSpider1_BigDeal(BaseSpider):
	name = 'www.bigdeal.sg'
	start_urls = [
			'http://www.bigdeal.sg',
			]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
		price =  hxs.select('/html/body/div/div/div/div/div/div/div/div/p/strong/text()').extract()
		#description = hxs.select('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div/p[6]/span/text()').extract()
		url = ['http://www.bigdeal.sg',]	

		deal = Deal(title=title[2].encode('ascii', 'ignore').strip(), price=price[0].strip(), url=url[0].strip())
		deal.save()

class DealSpider2_GroupOn(BaseSpider):
	name = 'www.groupon.sg'
	start_urls = [
			'http://www.groupon.sg',
			]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('/html/body/div/div[9]/div/div/div/div/h1/a/text()').extract()
		price = hxs.select('/html/body/div/div[9]/div/div/div/div[2]/form/div/span/span/text()').extract()
		#description = hxs.select('/html/body/div/div[9]/div/div[3]/div[2]/div[2]/p[2]/text()').extract()
		url = ['http://www.groupon.sg/',]

		deal = Deal(title=title[0].encode('ascii', 'ignore').strip(), price=price[0].strip(), url=url[0].strip())
		deal.save()

class DealSpider3_ShiokDeal(BaseSpider):
	name = 'www.shiokdeal.com'
	start_urls = [
			'http://www.shiokdeal.com',
			]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/h1/text()').extract()
		price = hxs.select('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/p/strong/text()').extract()
		#description = hxs.select('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div/p[2]/text()').extract()
		url = ['http://www.shiokdeal.com/',]
				
		deal = Deal(title=title[0].encode('ascii', 'ignore').strip(), price=price[0].strip(), url=url[0].strip())
		deal.save()


class DealSpider4_AllDealsAsia(BaseSpider):
	name = 'www.alldealsasia.com'
	start_urls = [
			'http://www.alldealsasia.com',
			]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('/html/body/div[@id="ext-wrapper"]/div[@id="wrapper"]/div[@id="main"]/div[@class="content-wrap"]/h1/text()').extract()
		price = hxs.select('/html/body/div[@id="ext-wrapper"]/div[@id="wrapper"]/div[@id="main"]/div[@class="content-wrap"]/div[2]/div[@class="deal-wrap"]/div[@class="d-wi"]/div[@class="d-price"]/div[@class="d-price-value"]/text()').extract()
		#description = hxs.select('/html/body/div[@id="ext-wrapper"]/div[@id="wrapper"]/div[@id="main"]/div[@class="content-wrap"]/div[2]/div[@class="deal-wrap"]/div[@class="d-desc"]/div[[2]/div[1]/div[1]/p/text()').extract()
		url = ['http://www.alldealsasia.com',]
				
		deal = Deal(title=title[0].encode('ascii', 'ignore').strip(), price=price[0].strip(), url=url[0].strip())
		deal.save()


class DealSpider5_VoucherWow(BaseSpider):
	name = 'www.voucherwow.com'
	start_urls = [
			'http://www.voucherwow.com/cities/singapore',
			]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title =hxs.select('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/a/h2/span/text()').extract()
		price = hxs.select('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/div/p/text()').extract()
		#description = hxs.select('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/a/h2/span/text()').extract()
		url = hxs.select('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/a/@href').extract()
				
		deal = Deal(title=title[0].encode('ascii', 'ignore').strip(), price=price[0].strip(), url= 'http://www.voucherwow.com' + url[0].strip())
		deal.save()


class DealSpider6_DealComSg(BaseSpider):
	name = 'www.deal.com.sg'
	start_urls = [
			'http://www.deal.com.sg/deals/singapore',
			]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('/html/body/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/a/text()').extract()
		price = hxs.select('/html/body/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/span[2]/text()').extract()
		#description = hxs.select('/html/body/div/div[2]/div/div[3]/div/div[2]/div/div/p[13]/text()').extract()
		url = hxs.select('/html/body/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/a/@href').extract()
				
		deal = Deal(title=title[0].encode('ascii', 'ignore').strip(), price=price[0].strip(), url=url[0].strip())
		deal.save()
