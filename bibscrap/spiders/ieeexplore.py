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

 import json, urllib.request

#how to import json?
#user put in doi as a parameter, then we import json of the website using query + api key + &doi=
#then work the parse json data
#there is a limit to how many call a day when using api key, might have to register for some more api keys

 with urllib.request.urlopen("https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey=3r88q7n22u429vtenyjjrhks&doi=10.1109/TTS.2020.2992669") as url:
    data = json.loads(url.read().decode())
       
    for i in data['article']:
        print("Title: ", data['title'])
            
        for j in data['authors']:
            print("Authors: ", data['authors'])
            
        print("Abstract:", data['abstract'])
