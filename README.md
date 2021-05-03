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

After cloning the repository, a user may use bibscrap by typing in the following command:

```
$ python bibscrap-main.py --doi <DOI>  
```

By minimum, the DOI must be specified for the driver to work, where [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) is some identifier for a particular study.
Additionally, the help menu for the driver can be found by typing the following command:

```
$ python bibscrap-main.py --h
```
