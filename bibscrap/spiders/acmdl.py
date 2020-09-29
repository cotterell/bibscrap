# -*- coding: utf-8 -*-
import scrapy


class AcmdlSpider(scrapy.Spider):
    name = 'acmdl'
    # allowed_domains = ['acm.org']
    # start_urls = ['http://dl.acm.org/doi/10.1145/2666652.2666656']

    def __init__(self, doi='', **kwargs):
        self.start_urls = [f'https://dl.acm.org/doi/{doi}']  # py36
        # self.start_urls = [f'http://dl.acm.org/doi/{doi}']
        super().__init__(**kwargs)  # python

    def parse(self, response):
        sel = scrapy.Selector(response)

        title = sel.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[2]/h1/text()').extract()

        authors = response.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[3]/div/ul/li/a/span/div/span/span/text()').getall()

        abstract = sel.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[2]/div[2]/div[2]/div[1]/div/div[2]/p/text()').extract()

        print('**************')
        print(f'TITLE: {title}')
        print('***************')
        print(f'AUTHORS: {authors}')
        print('***************')
        print(f'ABSTRACT: {abstract}')
        print('***************')
        print('REFERENCES: ')
        print()

        referenceTitles = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/text()').getall()

        referenceLinks = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/span/a/@href').getall()
            
        referenceDictionary = {}
        for i in range(len(referenceTitles)):
            x = referenceTitles[i]
            y = referenceLinks[i]
            print(f"Reference title: {x}, Link: {y}")
            print()
            referenceDictionary.update({x:y})
        
        #print(referenceDictionary)
