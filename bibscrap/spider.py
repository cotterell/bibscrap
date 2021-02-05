"""A collection of scrapy-based spiders for manuscript hosting services."""
import scrapy
import typing
import logging
import re
from bibscrap.models import Manuscript
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.link import Link


class PageHandler():

    logger = logging.getLogger(__qualname__)

    @classmethod
    def link_extractor(cls) -> LinkExtractor:
        ...

    @classmethod
    def parse_title(cls, response) -> str:
        ...

    @classmethod
    def parse_authors(cls, response) -> typing.List[str]:
        ...

    @classmethod
    def parse_doi(cls, response) -> str:
        ...

    @classmethod
    def parse_abstract(cls, response) -> str:
        ...

    @classmethod
    def parse_reference_links(cls, response) -> typing.List[Link]:
        ...

    @classmethod
    def parse(cls, response):
        cls.logger.info(f'parsing {response.url}')
        manuscript = Manuscript(
            url=response.url,
            title=cls.parse_title(response),
            authors=cls.parse_authors(response),
            doi=cls.parse_doi(response),
            abstract=cls.parse_abstract(response))
        yield manuscript.dict()

        for reference_link in cls.parse_reference_links(response):
            yield response.follow(reference_link)


class AcmdlHandler(PageHandler):

    @classmethod
    def parse_title(cls, response):
        return response.css('.citation__title::text').get(default=None)

    @classmethod
    def parse_authors(cls, response):
        return response.css('.loa__author-name > span::text').getall()

    @classmethod
    def parse_doi(cls, response):
        return response.css('.issue-item__doi::attr(href)').get(default=None)

    @classmethod
    def parse_abstract(cls, response):
        abstract_parts = response.css('.abstractSection *::text').getall()
        abstract = '\n\n'.join(abstract_parts)
        return abstract

    @classmethod
    def parse_reference_links(cls, response):
        reference_links = []
        references = response.css('.references__note::text').getall()
        for reference in references:
            links = re.findall(r'(https?://\S+)', reference)
            reference_links.extend(links)
        reference_links = map(Link, reference_links)
        print(list(reference_links))
        return reference_links

    @classmethod
    def link_extractor(cls) -> LinkExtractor:
        return LinkExtractor(
            allow_domains='dl.acm.org',
            allow='/doi/',
            deny=[
                '/doi/pdf/',
                '/doi/epdf/',
                '/doi/proceedings/',
            ])


class ManuscriptSpider(CrawlSpider):
    """Spider.

    Notes
       TODO, write.
    """
    name = __qualname__
    start_urls = ['https://dl.acm.org/doi/10.1145/3372782.3408120']
    rules = [
        Rule(AcmdlHandler.link_extractor(), callback=AcmdlHandler.parse),
    ]


    def parse(self, response):
        raise Exception()


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(ManuscriptSpider)
    process.start()
    print(dir(process))
