# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.yelp.com/biz/herndon-centennial-golf-course-herndon']
    start_urls = ['http://www.yelp.com/biz/herndon-centennial-golf-course-herndon/']

    def parse(self, response):

    	# TODO Second page wont scrape BUT only has one post so idc

    	# first original scrape
    	#self.scrape(response)

    	url = response.xpath('//*[@id="super-container"]/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[3]/a/@href').extract_first()
    	yield scrapy.Request(url=url, callback=self.parse)
    	self.scrape(response)

    def scrape(self, response):
    	posts = response.xpath('.//*[@class="review-content"]')

        print '\n\n#################### - STARTING SPIDER - ####################\n\n'
        count = 1

        for post in posts:
        	#text = response.xpath('.//*[@class="review-content"]/p/text()').extract()[i]
        	#prints off <p> until the frist break <br> 
        	text = post.xpath('.//p[@lang="en"]//text()').extract_first()

        	print '\nPost #' + str(count)
        	print text + '\n'
        	count += 1

        #next_page_url = response.xpath('//*[@id="super-container"]/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[3]/a/@href').extract_first()
     	#absolute_next_page_url = response.urljoin(next_page_url)
     	#yield scrapy.Request(absolute_next_page_url)

        print '\n\n##################### - ENDING SPIDER - #####################\n\n'