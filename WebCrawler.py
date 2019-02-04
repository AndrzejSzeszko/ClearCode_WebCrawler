#!/usr/bin/python3.7
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re


def site_map(url):

    def create_map(current_url):
        site = requests.get(current_url).text
        soup = BeautifulSoup(site, 'html.parser')
        title = soup.find('title').text if soup.find('title') else None
        links = soup.find_all('a')
        #  extract href values from <a>'s, discard ones which href's value is empty and discard duplicates
        links = set(link.get('href') for link in links if link.get('href'))
        #  screen out hrefs that do not lead to current domian's pages
        links = set(link for link in links if link.startswith(domain) or link.startswith('/'))
        #  prepend current domain to links that do not have it specified explicitly
        links = set(link if link.startswith(domain) else f'{domain}{link}' for link in links)
        links = set(link[:-1] if link.endswith('/') else link for link in links)
        result[current_url] = {'title': title, 'links': links}
        print(f'Links added: {len(result)}', end='\r')
        for link in links:
            if result.get(link):  # if key of given link already exist in result dict
                pass
            else:
                create_map(current_url=link)

    url = url[:-1] if url.endswith('/') else url
    domain = re.match(r'^https?://[^/]+', url).group()
    result = {}
    create_map(url)

    return result


if __name__ == '__main__':
    pprint(site_map('http://0.0.0.0:8000/'))
