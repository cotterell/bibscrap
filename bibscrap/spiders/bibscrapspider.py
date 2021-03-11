import abc
from abc import ABC, abstractmethod

class BibscrapSpider(metaclass=abc.ABCMeta):
    
    @abstractmethod
    def get_doi(self):
        pass
    
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_authors(self):
        pass
    
    @abstractmethod
    def get_abstract(self):
        pass
    
    @abstractmethod
    def get_references(self):
        pass
    
    @abstractmethod
    def get_paper(self):
        pass
    
    @abstractmethod
    def get_all_papers(self):
        pass
