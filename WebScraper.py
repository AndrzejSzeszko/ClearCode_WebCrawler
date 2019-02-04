#!/usr/bin/python3.7
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re


def site_map(url):

    def create_map(current_url):
        site = requests.get(current_url).text
        soup = BeautifulSoup(site, 'lxml')
        title = soup.find('title').text
        links = soup.find_all('a')
        links = set(link['href'] for link in links if link['href'].startswith(domain) or link['href'].startswith('/'))
        links = set(link if link.startswith(domain) else f'{domain}{link}' for link in links)
        result[current_url] = {'title': title, 'links': links}
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
