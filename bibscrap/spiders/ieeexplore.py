# -*- coding: utf-8 -*-
import scrapy
import json, urllib.request
import ssl
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

class IeeexploreSpider(scrapy.Spider):
    name = 'ieee'
    allowed_domains = ['ieee.org']
    #doi_shneiderman = '10.1109/TTS.2020.2992669'
    
    def __init__(self, doi='', **kwargs):
        super().__init__(**kwargs)
        self.get_ieee_paper(doi)

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

    def concat(iterable):  
        out = ''
        for item in iterable:
            out += item
        return out


    def clean_reference(entry):
        reference = concat(c for c in entry if c not in ['\n', '\t'])  #adding up the strings and omitting \n and \t in each entry/article      
        period = reference.find('.')
        reference = reference[period+1:]                             # omit order number and first period
        return reference


    def ieee_references(ar_number):
        url = f'https://ieeexplore.ieee.org/xpl/dwnldReferences?arnumber={ar_number}'
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.get_text()   
        #pprint(concat(c for c in text if c not in ['\n', '\t']))
        entries= text.split('\t    \t\t\t\n')                        #splitting the articles and putting them into a list
        entries= entries[1:]                                         # omit "View References"
        return [clean_reference(entry) for entry in entries]         #cleaning each reference and put them into a list

    def get_ieee_paper(self, doi):
        data = self.get_ieee_paper_dict(doi)

        article_data = data['articles']
        title = article_data[0]["title"]

        authors_data = article_data[0]['authors']['authors']
        #authors_full_name = ''
        #for i in authors_data:
            #authors_full_name += i['full_name'] +', '

        authors_full_names = [i['full_name'] for i in authors_data]
        authors_full_names = ', '.join(authors_full_names)

        abstract = article_data[0]['abstract']

        article_number = article_data[0]['article_number']
        references = ieee_references(article_number)
        references = ', '.join(references)

        final_data = [{
            'DOI': doi,
            'Title': title,
            'Author(s)': authors_full_names,
            'Abstract': abstract,
            'Reference(s)': references,
        }]
        df = pd.DataFrame(final_data, columns = ['DOI', 'Title', 'Author(s)', 'Abstract', 'Reference(s)'])
        
        df.to_csv('ieee.csv')

