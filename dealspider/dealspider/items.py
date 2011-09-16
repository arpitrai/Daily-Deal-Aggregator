from scrapy.item import Item, Field

class DealspiderItem(Item):
	title = Field()
	price = Field()
	description = Field()
	image = Field()
