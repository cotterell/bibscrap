# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class IeeexploreSpider(scrapy.Spider):
    name = 'ieeexplore'
    allowed_domains = ['ieee.org', 'doi.org']
    start_urls = ['https://ieeexplore.ieee.org/document/5581052']

    #def __init__(self, doi='', **kwargs):
    #    self.start_urls = [f'https://dx.doi.org/{doi}']  # py36
    #    super().__init__(**kwargs)  # python3


    def parse(self, response):
        #self.log(self.domain)
        hxs = scrapy.Selector(response)
        titles = hxs.xpath('/html/body/div[4]/div/div/div/div[5]/div/xpl-root/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[1]/div/div/h1/span/text()')
        print(titles.extract())

 import json

#how to import json?
#user put in doi as a parameter, then we import json of the website using query + api key + &doi=
#then work the parse json data

 with open('data.json') as json_file:
        data = json.load(json_file)
        
        print("Title: ", data['title'])
        print("Authors: ", data['authors')
        print("Abstract:", data['abstract'])
