import requests
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



all_cursor = []





def CrawlingCursor(cursor,page):

    cookies = {
        'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
        'datr': 'xKmkYzg_H2hB218oV81-7V7g',
        'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
        'ig_nrcb': '1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'shbid': '"16489\\05414816613506\\0541718183157:01f78423e95aebfda20f2b631032b72e8937638fdc5a420ca4e7327b8da2a349fcd45866"',
        'shbts': '"1686647157\\05414816613506\\0541718183157:01f796dbfe56bdc11597d892cba4fe5dddbd8c5b3f1a909eb815de68a7351699d21b2cec"',
        'csrftoken': '2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM',
        'ds_user_id': '14816613506',
        'sessionid': '14816613506%3AdtYo2Rtqv52izx%3A27%3AAYeq17yY5CMDLpO6_m9WAeM-aR2h7B9l1DRtK3yUSg',
        'rur': '"PRN\\05414816613506\\0541718260138:01f78eff81e4ba497e6d350667e9d66c2f2b24b659155fd8f92455772fa9350f1d11ede8"',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRFToken': '2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '129477',
        'X-IG-WWW-Claim': 'hmac.AR1qYgzflBqc55DVe0II_XRzbTQkUNQvy_nKNGcUgeIgPocV',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/virat.kohli/following/',
        # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="16489\\05414816613506\\0541718183157:01f78423e95aebfda20f2b631032b72e8937638fdc5a420ca4e7327b8da2a349fcd45866"; shbts="1686647157\\05414816613506\\0541718183157:01f796dbfe56bdc11597d892cba4fe5dddbd8c5b3f1a909eb815de68a7351699d21b2cec"; csrftoken=2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM; ds_user_id=14816613506; sessionid=14816613506%3AdtYo2Rtqv52izx%3A27%3AAYeq17yY5CMDLpO6_m9WAeM-aR2h7B9l1DRtK3yUSg; rur="PRN\\05414816613506\\0541718260138:01f78eff81e4ba497e6d350667e9d66c2f2b24b659155fd8f92455772fa9350f1d11ede8"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'count': '12',
        'max_id': '{}'.format(cursor),
        'search_surface': 'follow_list_page',
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/friendships/3027834848/followers/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    new_cusor = response.json()["next_max_id"]
    all_cursor.append({"AllCursor":new_cusor,"PagesNo":page})
    print("Getting New Cursor :- {}".format(new_cusor))
    
    if new_cusor:
        page+=1
        CrawlingCursor(new_cusor,page)



CrawlingCursor("QVFBYzVqNVZyTTlPcnV6UHNIelRiTVVwb0pmUy1yMmw5amEwejROR1NJbHpFRWhkOVRHcnB4bk96SjhocnhJQ0V3UnhGNl9lYmJEVkFYckx2YTVDaVcwMQ==",page=1)


df = pd.DataFrame(all_cursor)
df.to_excel("GotCursors.xlsx",index=False)