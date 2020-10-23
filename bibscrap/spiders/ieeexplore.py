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
import ssl


doi_shneiderman = '10.1109/TTS.2020.2992669'

def get_ieee_paper_dict(doi):
    api_key = '3r88q7n22u429vtenyjjrhks'
    url = f'https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey={api_key}&doi={doi}'
    context_ssl = ssl._create_unverified_context()
    
    try:
        with urllib.request.urlopen(url, context = context_ssl) as url:
            data = json.loads(url.read().decode())
            return data
    except Exception as e: 
        print(e)
    
    return {}

def get_ieee_paper(doi):
    data = get_ieee_paper_dict(doi)
    for i in data['articles']:
        print("Title:", i['title'])
        print("")
        
        authors = i['authors']
        print("Authors: ", end='') 
        for j in authors['authors']:
            print(j['full_name'], end=', ')
            
        print("")
        print("")
        print("Abstract:", i['abstract'])
            

                  
