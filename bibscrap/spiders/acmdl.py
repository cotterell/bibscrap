# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os.path
from os import path

class AcmdlSpider(scrapy.Spider):
    name = 'acmdl'
    # allowed_domains = ['acm.org']
    # start_urls = ['http://dl.acm.org/doi/10.1145/2666652.2666656']

    def __init__(self, doi='', **kwargs):
        self.start_urls = [f'https://dl.acm.org/doi/{doi}']  # py36
        # self.start_urls = [f'http://dl.acm.org/doi/{doi}']
        super().__init__(**kwargs)  # python
        global doiRef
        doiRef = doi

    def parse(self, response):
        sel = scrapy.Selector(response)

        title = sel.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[2]/h1/text()'
            ).extract()

        authors = response.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[3]/div/ul/li/a/span/div/span/span/text()'
            ).getall()

        abstract = sel.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[2]/div[2]/div[2]/div[1]/div/div[2]/p/text()'
            ).extract()

        referenceTitles = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/text()'
            ).getall()

        referenceLinks = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/span/a/@href'
            ).getall()

        data = {
            'DOI': [doiRef],
            'Title': title,
            'Authors': authors,
            'Abstract': [abstract],
            'Reference Titles': referenceTitles,
            'Reference Links': referenceLinks
        }
        
        df = pd.DataFrame(list(data.items()))

        if (path.exists('acmdl.csv') == False): 
            df.to_csv('acmdl.csv')
            print(df)
        else:
            df.to_csv('acmdl.csv', mode = 'a', header = False)
