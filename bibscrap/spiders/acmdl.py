# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os.path
from os import path
from . import bibscrapspider

class AcmdlSpider(bibscrapspider.BibscrapSpider, scrapy.Spider):
    name = 'acmdl'
    # allowed_domains = ['acm.org']
    # start_urls = ['http://dl.acm.org/doi/10.1145/2666652.2666656']


    def __init__(self, doi='', **kwargs):
        self.start_urls = [f'https://dl.acm.org/doi/{doi}']
        super().__init__(**kwargs)  # python
        global doiRef
        doiRef = doi

    #This method is the default callback of start_urls, which process the downloaded response and then returns a request to scrape the doi extracted from the reference
    def parse(self, response):
        global finalData
        finalData = self.get_paper(response)
        doiList = self.doi_from_ref(response)
        if len(doiList) > 0:
            doiRef = doiList[0]
            return scrapy.Request(f'https://dl.acm.org/doi/{doiList[0]}', callback = self.parse_2)
   
    #This method is the specified callback to process the dowloaded response from the article in reference
    def parse_2(self, response):
        data = self.get_paper(response)
        finalData.extend(data)
        self. get_all_papers(finalData)

    #This method take the response downloaded and return a list of dois extracted from the reference part of the article
    def doi_from_ref(self, response):
        referenceLinks = self.get_reference_links(response)
        doi = [i[5:] for i in referenceLinks if i.startswith('/doi/')]
        return doi

    #This method take the response downloaded and return the title of the article
    def get_title(self, response):
        title = response.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[2]/h1/text()'
            ).extract()
        return title

    #This method take the response downloaded and return a list of authors of the article
    def get_authors(self, response):
        authors = response.xpath(
            '/html/body/div[1]/div/main/div[2]/article/div[1]/div[2]/div/div[3]/div/ul/li/a/span/div/span/span/text()'
            ).getall()
        authors = ', '.join(authors)
        return authors

    #This method take the response downloaded and return the abstract of the article
    def get_abstract(self, response):
        #abstract = response.xpath(
        #    '/html/body/div[1]/div/main/div[2]/article/div[2]/div[2]/div[2]/div[1]/div/div[2]/p/text()'
        #    ).extract(
        abstract= response.xpath('//*[@id="pb-page-content"]/div/main/div[2]/article/div[2]/div[2]/div[2]/div[1]/div/div[2]/p/text()[1]').extract()
        return abstract

    #This method take the response downloaded and return a list of references of the article
    def get_references(self, response):
        referenceTitles = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/text()'
            ).getall()
        return referenceTitles

    #This method take the response dowloaded and return a list of links to the articles in the reference
    def get_reference_links(self, response):
        referenceLinks = response.xpath(
            '/html/body/div/div/main/div[2]/article/div[2]/div[2]/div[2]/div[3]/ol/li/span/span/a/@href'
            ).getall()
        return referenceLinks

    #This method take the response downloaded and return the doi of the article
    def get_doi(self):
        pass

    def get_all_papers(self, response):
        doiList = self.doi_from_ref(response)

    #This method take the response and return a list of extracted data
    def get_paper(self, response):
        #self.start_urls = [f'https://dl.acm.org/doi/{doi}']
        #response = parse(self)
        title = self.get_title(response)
        authors = self.get_authors(response)
        abstract = self.get_abstract(response)
        references = self.get_references(response)
        referenceLinks = self.get_reference_links(response)
        doiList = self.doi_from_ref(response)

        data = [{
            'DOI': doiRef,
            'Title': title,
            'Author(s)': authors,
            'Abstract': abstract,
            'Reference(s)': references,
            'ACMDL Reference Links': referenceLinks,
            'List of doi': doiList
        }]
        return data

    #This method take the list of data extracted and turn it to csv
    def get_all_papers(self, data):
        df = pd.DataFrame(data, columns = ['DOI', 'Title', 'Author(s)', 'Abstract', 'Reference(s)', 'ACMDL Reference Links', 'List of doi'])

        if (path.exists('data.csv') == False):
            df.to_csv('data.csv')
            print(df)
        else:
            df.to_csv('data.csv', mode = 'a', header = False)
