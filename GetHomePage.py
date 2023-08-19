from requests import Session
import requests
import pandas as pd
from lxml import html
import time
from pymongo import MongoClient
import random
import pymongo
import json
import logging
import requests
import GettingDocID
import re
from bs4 import BeautifulSoup as bs
import requests

cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'shbid': '"18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"',
    'shbts': '"1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"',
    'csrftoken': '2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM',
    'ds_user_id': '14816613506',
    'sessionid': '14816613506%3AdtYo2Rtqv52izx%3A27%3AAYdXYfpo3-M5yNFAcmdvfRQ7VDb5JBCSyoqL6UZpgg',
    'rur': '"RVA\\05414816613506\\0541718172456:01f7651f656acafbfdbfb47c8f10d86d1d977c71bedac35c15fe179e4dee9247294051e0"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.instagram.com/keshavi_chhetri_official/',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"; shbts="1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"; csrftoken=2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM; ds_user_id=14816613506; sessionid=14816613506%3AdtYo2Rtqv52izx%3A27%3AAYdXYfpo3-M5yNFAcmdvfRQ7VDb5JBCSyoqL6UZpgg; rur="RVA\\05414816613506\\0541718172456:01f7651f656acafbfdbfb47c8f10d86d1d977c71bedac35c15fe179e4dee9247294051e0"',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def GetHome(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    code_ = re.findall('\,"liveQueryFetchWithWWWInitial"\:\{"r"\:\["(.*?)",',response.text)
    soup = bs(response.text,features="lxml")
    AllHref = soup.findAll("link",{"rel":"preload"})
    if AllHref.__len__() == 17:
        return AllHref[2].get("href")