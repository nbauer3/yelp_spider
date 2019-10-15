# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.yelp.com/biz/herndon-centennial-golf-course-herndon']
    start_urls = ['http://www.yelp.com/biz/herndon-centennial-golf-course-herndon/']

    def parse(self, response):
    	posts = response.xpath('.//*[@class="review-content"]')

        print '\n\n#################### - STARTING SPIDER - ####################\n\n'
        count = 1

        for post in posts:
        	#text = response.xpath('.//*[@class="review-content"]/p/text()').extract()[i]
        	text = post.xpath('.//p[@lang="en"]//text()').extract_first()

        	print '\nPost #' + str(count)
        	print text + '\n'
        	count += 1
        print '\n\n##################### - ENDING SPIDER - #####################\n\n'