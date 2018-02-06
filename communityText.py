# -*- coding:utf-8 -*-
import urllib.request as req
from bs4 import element
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

FMKOREA_SELECTOR = '#bd_capture > div.rd_body.clear > article > div'
PPOMPPU_SELECTOR = 'body > div > div.contents > div.container > div > table:nth-of-type(5) > tr:nth-of-type(1) > td > table > tbody > tr > td > table > tr > td'
HUMORUNIV_SELECTR = '#cnts'
RULIWEB_SELECTOR = '#board_read > div > div.board_main > div.board_main_view > div.view_content'
MLBPARK_SELECTOR = '#container > div.contents > div.left_cont > div.view_context'


def getSoup(url):
    headered = req.Request(url, headers=header)
    html = req.urlopen(headered)
    soup = BeautifulSoup(html, 'lxml')
    
    return soup


def c1(url):
    text = ''
    soup = getSoup(url)
    tag = soup.select_one(FMKOREA_SELECTOR)
    
    if tag is not None:
        for child in tag.descendants:
            if type(child) is element.NavigableString and child.find_parent('video') is None:
                text += child + ' '
        
        text = ' '.join(text.split())    
    
    return text


def c2(url):
    text = ''
    soup = getSoup(url)
    tag = soup.select_one(PPOMPPU_SELECTOR)
    
    if tag is not None:
        for doc in tag.descendants:
            if type(doc) is element.NavigableString:
                text += doc.strip() + ' '
        
        text = ' '.join(text.split())
    
    return text


def c3(url):
    text = ''
    soup = getSoup(url)
    tag = soup.select_one(HUMORUNIV_SELECTR)
    
    if tag is not None:
        for elem in tag.descendants:
            if type(elem) is element.NavigableString and elem.find_parent('img') is None and elem.find_parent('script') is None:
                text += elem.strip() + ' '
    
        text = ' '.join(text.split())
    
    return text


def c4(url):
    text = ''
    soup = getSoup(url)
    tag = soup.select_one(RULIWEB_SELECTOR)
    
    if tag is not None:
        for doc in tag.descendants:
            if type(doc) is element.NavigableString:
                text += doc.strip() + ' '
    
        text = ' '.join(text.split())
    else:
        text = None
    
    return text


def c5(url):
    text = ''
    soup = getSoup(url)
    tag = soup.select_one(MLBPARK_SELECTOR)
    
    if tag is not None:
        for doc in tag.descendants:
            if type(doc) is element.NavigableString:
                text += doc.strip() + ' '
    
        text = ' '.join(text.split())
    
    return text
