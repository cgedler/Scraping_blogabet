# Created on : Feb 5, 2024, 7:19:30 PM
# Author     : Christopher Gedler


import requests
from bs4 import BeautifulSoup


def getStatusConnectionCode(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        page = requests.get(url, headers=headers)
    except Exception as e:
        print ("Exception when obtaining the Status Code: ", e)
    return page.status_code

def getHtmlDocument(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
    except Exception as e:
        print ("Exception when obtaining the Status Code: ", e)
    return soup