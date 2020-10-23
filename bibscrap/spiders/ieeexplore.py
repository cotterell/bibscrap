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
import pandas as pd


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
    
    article_data = data['articles']
    title = article_data[0]["title"]
    
    authors_data = article_data[0]['authors']['authors']
    authors_full_name = ''
    for i in authors_data:
        authors_full_name += i['full_name'] +', '
    
    abstract = article_data[0]['abstract']
    
    final_data = [{
        'DOI': doi,
        'Title': title,
        'Authors': authors_full_name,
        'Abstract': abstract,
    }]
    return final_data

def convert_to_dataframe(data):
    df = pd.DataFrame(data, columns = ['DOI', 'Title', 'Authors', 'Abstract'])
    return df

