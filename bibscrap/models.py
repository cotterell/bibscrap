
class Manuscript():

    def __init__(self, url, title, authors=[], doi=None, abstract=None):
        self.url = url
        self.title = title
        self.authors = authors
        self.doi = doi
        self.abstract = abstract

    def dict(self):
        return vars(self)
