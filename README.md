# ClearCode internship task 2019: Web Scraper
## Description:
This project contains function site_map(url) that takes url as an input and returns site map in form of dictionary. This dictionary keys are all links that belongs to initial url domain (those links lead to subsites of initial url). Values are dictionaries containing title of the website and set of links that this website includes. Eg.:
```
intial url: 'http://0.0.0.0:8000/'
output:
{
    'http://0.0.0.0:8000': {
        'title': 'Index',
        'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
    },
    'http://0.0.0.0:8000/site.html': {
        'title': 'The Site',
        'links': {'http://0.0.0.0:8000/site/subsite.html'}
    },
    'http://0.0.0.0:8000/example.html': {
        'title': 'No links here',
        'links': set()
    },
    'http://0.0.0.0:8000/site/subsite.html': {
        'title': 'Looping',
        'links': {'http://0.0.0.0:8000/site/other_site.html', 'http://0.0.0.0:8000'}
    },
    'http://0.0.0.0:8000/site/other_site.html': {
        'title': 'Looped',
        'links': {'http://0.0.0.0:8000/site/subsite.html'}
    }
}
```    

## QuickStart
1) Clone project on your machine.
2) Create and activate virtual environment and install required packages.
3) In terminal navigate to directory containing WebScraper.py.
4) Run python3.7 console. Import "site_map" function from "WebScraper" module, and all required modules listed in "requirements.txt"
5) Run site_map('<url/to/website/of/your/choice>'). CAUTION! I do not recommend to pass some link-rich page as an argument. It takes quite a lot time to process such a page (eg. processing http://www.regionymlawa.pl/ with 486 in-domain links takes approximately 10 min). So if you want spend only few seconds to see results check something like "https://warbler.pl/" (4 in-domain links).

## SlowStart
This checklist assumes that you are using Ubuntu 16.04 or higher, and have python3.7, git, pip and some stuff for creating virtual environments installed. And you can use it a little.
1) Navigate to directory you want to place project in:
    ```
    $ cd path/to/directory/of/your/choice
    ```
2) Clone project on your machine:
    ```
    $ git clone https://github.com/AndrzejSzeszko/ClearCode_WebCrawler.git
    ```
3) Create and activate new virtual environment using tool and location of your choice. Remember to use python3.7 as an interpreter.  You can skip this step if you don't care about python packages conflicts (OK, I know you do)
4) Navigate to directory "example/" (placed in the same directory as WebCrawler.py), and run example webpage delivered by ClearCode:
    ```
    (env)$ cd path/to/directory/containing/mentioned/directory/
    (env)$ python3.7 -m http.server
    ```
   Do not close this terminal window! Open new one and:
5) Navigate to directory containing WebCrawler.py:
    ```
    (env)$ cd path/to/directory/containing/mentioned/file
    ```
6) Chosen location should also have "requirements.txt" contained. Install required modules using pip:
    ```
    (env)$ pip install -r requirements.txt
    ```
7) Run python3.7 console. Import required modules:
    ```
    (env)$ python3.7
    >>> import requests
    >>> from bs4 import BeautifulSoup
    >>> from pprint import pprint
    >>> import re
    >>> from WebCrawler import site_map
    ```
8) Run site_map('http://0.0.0.0:8000/') to crawl test website served in point No 4):
    ```
    >>> site_map('http://0.0.0.0:8000/')
    ```
9) Output exact to the one from the beginning of this README should appear.
10) Crawl some other website:
    ```
    >>> site_map('http://www.regionymlawa.pl/')
    ```
    Just in 10 minutes you will see results ;) Go grab some coffee.
 