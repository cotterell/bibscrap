# -*- coding: utf-8 -*-
import scrapy
import urllib
import json, urllib.request
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from pprint import pprint
from . import bibscrapspider

class Ieee(bibscrapspider.BibscrapSpider, scrapy.Spider):
    name = 'ieee'
    allowed_domains = ['ieee.org']
    _current_key = 0
    
    def __init__(self, doi='', **kwargs):
        super().__init__(**kwargs)
        self.get_all_papers(doi)
    
    def get_api_key(self):
        global _current_key
        _current_key = 0
        api_keys = ['3r88q7n22u429vtenyjjrhks', 'buqr39fvze48b4htc4q3xthu']
        api_key = api_keys[_current_key % len(api_keys)]
        _current_key += 1
        return api_key
    
    def get_ieee_paper_dict(self, doi=None, article_title=None):
        api_key = self.get_api_key()
        if article_title == None: 
            url = f'https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey={api_key}&doi={doi}'
        else:
            url = f'https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey={api_key}&article_title={quote(article_title)}'
        context_ssl = ssl._create_unverified_context()

        try:
            with urllib.request.urlopen(url, context = context_ssl) as url:
                data = json.loads(url.read().decode())
                return data
        except Exception as e: 
            print(e)

        return {}
    
    def concat(self, iterable):  
        out = ''
        for item in iterable:
            out += item
        return out

    def clean_reference(self, entry):
        reference = self.concat(c for c in entry if c not in ['\n', '\t'])  #adding up the strings and omitting \n and \t in each entry/article      
        period = reference.find('.')
        reference = reference[period+1:]                             # omit order number and first period
        return reference
    
    def get_article_name_from_ref(self, entry):
        begin_quo = entry.find('"') 
        article_name = ''
        if begin_quo == -1:
            article_name = 'None'
        else:
            end_quo = entry.find('"', begin_quo+1)
            article_name = entry[begin_quo+1: end_quo]
        return article_name
    
    def get_doi(self, references):
        doi = []
        for entry in references:
            article_name = self.get_article_name_from_ref(entry)
            if article_name == 'None' or entry.find('IEEE') == -1:    #relying solely on total_records waste the number of available calls for each api
                pass
            else:
                data = self.get_ieee_paper_dict(article_title = article_name)
                try:
                    if data["total_records"] == 1:
                        article_data = data["articles"]
                        doi.append(article_data[0]["doi"])
                except Exception as e:
                    print(e)
        return doi
    
    def get_title(self, entry):
        if type(entry) is dict:
            article_data = entry['articles']
            article_name = article_data[0]["title"]      #originally named title
        else: 
            begin_quo = entry.find('"') 
            article_name = ''
            if begin_quo == -1:
                article_name = 'None'
            else:
                end_quo = entry.find('"', begin_quo+1)
                article_name = entry[begin_quo+1: end_quo]
        return article_name
    
    
    def get_authors(self, data):                       #data is a dict
        article_data = data['articles']
        
        authors_data = article_data[0]['authors']['authors']
        #authors_full_name = ''
        #for i in authors_data:
            #authors_full_name += i['full_name'] +', '

        authors_full_names = [i['full_name'] for i in authors_data]
        authors_full_names = ', '.join(authors_full_names)
        return authors_full_names
    
    def get_abstract(self, data):
        article_data = data['articles']
        abstract = article_data[0]['abstract']
        return abstract
    
    def get_references(self, doi):   
        url = f'https://ieeexplore.ieee.org/xpl/dwnldReferences?arnumber={doi}'
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
        references = [self.clean_reference(entry) for entry in entries]         #cleaning each reference and put them into a list
        return references
    
    def get_paper(self, doi):
        try: 
            data = self.get_ieee_paper_dict(doi)
            title = self.get_title(data)
            authors = self.get_authors(data)
            abstract = self.get_abstract(data)
            references = self.get_references(doi)

            final_data = [{
                    'DOI': doi,
                    'Title': title,
                    'Author(s)': authors,
                    'Abstract': abstract,
                    'Reference(s)': references,
                    'Referenced by': 'None'
                }]
            return final_data
    
        except Exception as e:
            print(e)
    
    def get_all_papers(self, doi):
        data = self.get_paper(doi)
        #print(data)
        references = self.get_references(doi)
        references_doi = self.get_doi(references)
        #print(references_doi)
        for item in references_doi:
            ref_paper_data = self.get_paper(item)
            ref_paper_data[0]['Referenced by'] = data[0]['DOI']
            try:
                data.extend(ref_paper_data)
            except Exception as e:
                print(e)
        df = pd.DataFrame(data, columns = ['DOI', 'Title', 'Author(s)', 'Abstract', 'Reference(s)', 'Referenced by'])
        #return df
        df.to_csv('ieee.csv')

    #print(get_doi_from_ref('Radiative "decay" of non radiative surface plasmons excited by light'))
    #get_all_papers('10.1109/SMC.2018.00641')
    #data = get_ieee_paper_dict('TDG4839435')
    #print(data['total_records'])
