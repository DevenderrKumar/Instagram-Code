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


cookies = {
    'datr': 'ZOPnY0WsUegvf1D9P2HSzER2',
    'ig_nrcb': '1',
    'mid': 'Y-fjaAAEAAEjwJ45rgvgmHMue748',
    'ig_did': '6B974EE0-195F-4625-B8F6-07B51776BA9A',
    'csrftoken': '0d5sq7GZKglrw4E6wgCLYebKevma02JD',
    'ds_user_id': '56853077686',
    'shbid': '"18949\\05456853077686\\0541718106920:01f7657eeb8a3534ab6af20f756fecdeace4f77210cdb2c499aedc1d5483355454993868"',
    'shbts': '"1686570920\\05456853077686\\0541718106920:01f7ff94bcbe59ccf147accb64828a1a535d65861a50e6cd5996169f78d31291985ea993"',
    'sessionid': '56853077686%3A1HOij6QWaikX9k%3A4%3AAYc3FogfSU-Z0Cbw67nNwAbGsvD_q9Mr83jKWVV9yw',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'fbsr_124024574287414': 'EuTqQEUobr3C7GW2iytINEGfwR7SJpHN4KPj6-lZKqQ.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQlpQMExoVkF3OGM1c2Vwb182T0tUb3Z6TkhIbGdOeUJkU29pV0hfN1RiemZWRUswdFhEdVN2N2I0YzlkRmlKTUdkdEU4Q0lfbGpSdVBFZ2JaSHNzWmJOektuRDB0TDdudWdWN25UYjZ6V1dVa19MYkxQTDAxUkxyZzVEcDVEa21MSHpkajBVeWlxWV92V01YM2VzZjVLZXRBbVdzaXlQbXVFWUdIYWxMakdoVDhWNS11T1ZqMFRGQUNvbE1BZmozQWFWZ3h5M3RjOGVBRHV6bFk0NnZZcmxmTURDTF9FTFI1Tk5hNzljQWVCN2xvcVhPU1c5dEpfMkVvUlpNMmp3MnBIUGFqQl9SaUNnZWZFYmRoaHNFNGZPVnZxcjdaVmNVVGctWGdNTndvaHEyTUc0YTNNaHE1aDVEZTJSYk5HcXNvOHBsTlpWNDgzMlBHNEZ4OTlpcWJoWS03UkRIVTVsdHFueVY2RTgtR1dydyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFIVERaQzBaQkhsZjRhNGpmV1pCU2gwZ0ZWMlNWMGxMTVpBMjBtSGhOcmJYYVRaQ3lRdG9NRkNkVmlpczJ3V1RITnlIMzJFVW5neFpCNXJEdlpBOEJzV1Z5UEJzaFdtelFnNzBLaU9TcHRNaWxqSnhPZlpBMXNZdFR1VGoyVjZoWkMyOXBqU1RqRUdwRDN0TGpidXg3bkVMOW1EWkJGY0dhS2U3dE1zNkhqS0xqVG1tOFJpbmhsSVpBRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODY1NzA5MzZ9',
    'rur': '"PRN\\05456853077686\\0541718106972:01f77b1d16cb0b1340b0f2bb0a85dc00f96ce9170f13cd7b746837a36d7ca2fd77383b01"',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=ZOPnY0WsUegvf1D9P2HSzER2; ig_nrcb=1; mid=Y-fjaAAEAAEjwJ45rgvgmHMue748; ig_did=6B974EE0-195F-4625-B8F6-07B51776BA9A; csrftoken=0d5sq7GZKglrw4E6wgCLYebKevma02JD; ds_user_id=56853077686; shbid="18949\\05456853077686\\0541718106920:01f7657eeb8a3534ab6af20f756fecdeace4f77210cdb2c499aedc1d5483355454993868"; shbts="1686570920\\05456853077686\\0541718106920:01f7ff94bcbe59ccf147accb64828a1a535d65861a50e6cd5996169f78d31291985ea993"; sessionid=56853077686%3A1HOij6QWaikX9k%3A4%3AAYc3FogfSU-Z0Cbw67nNwAbGsvD_q9Mr83jKWVV9yw; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=EuTqQEUobr3C7GW2iytINEGfwR7SJpHN4KPj6-lZKqQ.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQlpQMExoVkF3OGM1c2Vwb182T0tUb3Z6TkhIbGdOeUJkU29pV0hfN1RiemZWRUswdFhEdVN2N2I0YzlkRmlKTUdkdEU4Q0lfbGpSdVBFZ2JaSHNzWmJOektuRDB0TDdudWdWN25UYjZ6V1dVa19MYkxQTDAxUkxyZzVEcDVEa21MSHpkajBVeWlxWV92V01YM2VzZjVLZXRBbVdzaXlQbXVFWUdIYWxMakdoVDhWNS11T1ZqMFRGQUNvbE1BZmozQWFWZ3h5M3RjOGVBRHV6bFk0NnZZcmxmTURDTF9FTFI1Tk5hNzljQWVCN2xvcVhPU1c5dEpfMkVvUlpNMmp3MnBIUGFqQl9SaUNnZWZFYmRoaHNFNGZPVnZxcjdaVmNVVGctWGdNTndvaHEyTUc0YTNNaHE1aDVEZTJSYk5HcXNvOHBsTlpWNDgzMlBHNEZ4OTlpcWJoWS03UkRIVTVsdHFueVY2RTgtR1dydyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFIVERaQzBaQkhsZjRhNGpmV1pCU2gwZ0ZWMlNWMGxMTVpBMjBtSGhOcmJYYVRaQ3lRdG9NRkNkVmlpczJ3V1RITnlIMzJFVW5neFpCNXJEdlpBOEJzV1Z5UEJzaFdtelFnNzBLaU9TcHRNaWxqSnhPZlpBMXNZdFR1VGoyVjZoWkMyOXBqU1RqRUdwRDN0TGpidXg3bkVMOW1EWkJGY0dhS2U3dE1zNkhqS0xqVG1tOFJpbmhsSVpBRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODY1NzA5MzZ9; rur="PRN\\05456853077686\\0541718106972:01f77b1d16cb0b1340b0f2bb0a85dc00f96ce9170f13cd7b746837a36d7ca2fd77383b01"',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/p/CtTvdC-h6vi/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Microsoft Edge";v="114.0.1823.43"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"10.15.7"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
    'x-asbd-id': '129477',
    'x-csrftoken': '0d5sq7GZKglrw4E6wgCLYebKevma02JD',
    'x-fb-friendly-name': 'PolarisPostRootQuery',
    'x-fb-lsd': 'C86Ou_OpDsI2IgRUFOplCv',
    'x-ig-app-id': '936619743392459',
}






def GetLocation(DocId,PostCode,RefURl):
    headers["referer"] = RefURl

    data = {
        'av': '17841456810606634',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': '2',
        '__hs': '19520.HYP:instagram_web_pkg.2.1..0.0',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1007661002',
        '__s': 'jm84om:riv8zu:9r8ft3',
        '__hsi': '7243767167802440686',
        '__dyn': '7xeUmwlE7ibwKBWo2vwAxu13w8CewSwMwNw9G2S0lW4o0B-q1ew65xO2O1Vw8G1Qw5Mx62G3i0Bo7O2l0Fwqo31wnEfovw8O4U2zxe2Gew9O22362W2K0zK5o4q3y1Sx_w4HwJwSyES1Twoob82ZwrUdUbGwmk1xwmo6O0A8',
        '__csr': 's7spNdhsBihcyijRYnQDmKQImHjSuA8BAh8N7DHBLgW8y999XDAihaAGhu9BhkUSqidzaBox3ByV8yAql2VosyGgSi00hjJ06sw1FO0k60B8wM2Fo8fyU0GJzo5O1qw9-bw9a4Uf3wno11k2YWxR1-26czkfw0s18',
        '__comet_req': '7',
        'fb_dtsg': 'NAcPaFWEk0WnyOFutUl205WoQU2i_og7bnNMgT9E9O9lBCZ6n_78hwg:17864955220006059:1676141542',
        'jazoest': '26141',
        'lsd': 'C86Ou_OpDsI2IgRUFOplCv',
        '__spin_r': '1007661002',
        '__spin_b': 'trunk',
        '__spin_t': '1686570971',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'PolarisPostRootQuery',
        'variables': '{"shortcode":"'+f'{PostCode}'+'"}',
        'server_timestamps': 'true',
        'doc_id': f'{DocId}',
    }

    response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data)
    print(response.status_code)



url = "https://www.instagram.com/p/CtTvdC-h6vi/"
code_ = "CtTvdC-h6vi"


# response = requests.post(url, cookies=cookies, headers=headers)
# av_id = re.findall(',"userID":"(.*?)",',response.text)
# haste_session_id = re.findall(',"haste_session":"(.*?)",',response.text)
# _spin_r = re.findall(',"__spin_r":(.*?),',response.text)
# hsi_id = re.findall(',{"pageLoadEventId":"(.*?)",',response.text)
# lsd_token = re.findall('\["LSD",\[\]\,\{"token"\:"(.*?)"\},',response.text)
# __spin_t = re.findall('\,"\_\_spin\_t"\:(.*?)\,',response.text)

DocID = GettingDocID.GetDocID()

GetLocation(DocID,code_,url)