# bibscrap
#### A tool to scrape bibliographies from conference archives
------
### Functional Requirements

Given some [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier), `bibscrap` will insert the `title`, `author(s)`, `abstract`, `references`, and `date` into some tabular format (database or [Pandas](https://pandas.pydata.org/docs/))

------
### Contributors
- Aidan Killer
- My Nguyen
- Sree Datla
- Matthew Pooser
- Dr. Michael Cotterell

------------------------
### Installation

```
$ git clone https://github.com/cotterell/bibscrap.git
```

------------------------
### Execution

As of right now, the spider will have to be manually executed.

ACMDL
```
$ scrapy crawl -a doi=<DOI> acmdl
```

IEEEXplore
```
$ scrapy crawl -a doi=<DOI> ieee
```

Where [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) is some identifier for a particular study.
