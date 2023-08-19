from requests import Session
import requests
import pandas as pd
from lxml import html
import time
# from pymongo import MongoClient
import random
from datetime import datetime
import json
import pymongo



new_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm8y-E',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/p/Cn6dk7nyIQd/',
    'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="PRN\\05456853077686\\0541706429153:01f7fbb72bc59a78fbf8dbf6310a2afdf6b30048cc73f412d5056875b826858419bcfeb5"; fbsr_124024574287414=lVuK0xMAbTWtEDwnIXk_8f8YxjW65rvjUpWaZgnAw2A.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQU5URXhDdkJXUy1FczcyWjVBQm52U3JhVzlwUGpuNGYwVFFCMnEyeEhFRkN1aXBxZ3NhSjN4M3lLeTlxbGpNVnlVUjdDZE01TUczM3hINkFRSVdyZ0x5c0J0cjkzenppZ1UzRkhNZGEyZ21aYWpTTFU0S1VYTnU2azZ5NUVERUd1YjFIWEdxLUwzblR6NkdEcEI2LUpTZ3hrQ3dPQkdlS2JtUFJkWkRXWnBsbTBVVURyUFVqYTlESC1vSE85RFpEVzRTTmdEblJZMnM2dlNoNXMzYXRUbTdlZ1cta3JVd21YNWhlVWJrRlJDNEdWaXBhMEpzUld4SGhkZHVzZ0hRYUVjWEtZa21jQU0zbnB4YV90RHdVV095bHd4Z0hTakYzRjdjMDlvVGR1emtfd3N0V3NJSy05ZUJubk5mRXZvZGpHczF6d0dpZHhST3NlUHNsMHZkSF9aIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxaQml2ekhUazZWOTdXWkNuc0xDcFdHWkNjTDdIb3ZaQ1RESXEyTkVaQ0loY0drb1pBQmNicVFRdzlKQnlPeEhIaXZFNDQwelFINmxLY0NqdjR2R3pER2txUEI2SDNrNGlUVXBUNEwwdDlRbE5GTlpDQXhCb29ZRG1icTBDWkJSY05INTBsR0JaQ2w3RDlQS1NUZjZpeUxRUm01d1k1TW5jYkJ4dVVmWkNaQnF0NWx1UXczTFhGOFRzWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDg5MzEwNn0; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYcpRlthQHl1Nd4Edrblr64YH7zQlHaYamaUMPoBlg; shbid="18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"; shbts="1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"; fbsr_124024574287414=E09UCz0EsLCV21IW-N8dLgKCjV18J08FZxtShHK1Ab4.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQlhuZmh6QU5EZXNTaUZFSFpOcVZFYjFRaFE3ZjJkWmlPcm5NSlZnLURfQ29mVUI0OWFmRmtQQTdZVFRMalVQV2g2SE9TUEplNXQzR3dXcDk4TnpIYWxWQ2lDSktoNGdnbGlOQnhWRFp4dGxRbWhDakhmWENiVmVpNEFRNTgtZVV3M2JNc0FEeVM0M0Y4cnY2NHBMbjJneTdDUzhfTVVUcnRsb29fcmM1ekI1eHpzdkVNX1RyMUZiOE5rVEtWSGd5aXZWWjhuS291RUJ3YXVLb1N2bDBFLWY2NjZKM1EySjNHcXZFVTVBdnZQY3pPdmI0OWZRSVRPNnhEUlczLU0taDhaMi14YkU5ZmN3MFQ4Z0xzZWZNTGI3Vk9NYWpzd082UnZZZjJIekV6cmQwX19ZUVcxakFmQ2F6ekFvWDYwS2lURl9uVlhQYjU0eWxnaGV0YjNmLU4wUk9VZTMzR052TjZOcDdRUlhaT25BZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFFMlJWZUNIYnBKNkY2NVN3TXVzUnZRbHhQMDJRM2Fva0tnc1dQQzBmUUNWRTRHcHV5TWh5bGRUcTFBelIwblE1alNZTFpCcEdROWxsV2F5R1RWREhaQzJwZnc4OWpHTnFrT2VvSWFMa3dLNmpDcnpZbHZpQmtIVFFiQ1pCVG1WVnlPZEZQSnBFQlh2YjJxTlFNQm5UNWlEQ0hyNnhQWXJ4Q2l5bnlaQmRFR2s2d25NTW5jWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDg5MjU4NH0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'iyIURBRE2aLVA8o6C1LIXuQfhLT2cY0x',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm87hY',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/p/Cnd_PF5q8ui/',
    'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; csrftoken=iyIURBRE2aLVA8o6C1LIXuQfhLT2cY0x; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; ds_user_id=56853077686; sessionid=56853077686%3AmlPdv1mNGeIpkY%3A13%3AAYdR0Pe3glKJwvM8S7k8QU4HVg2vXpz5x1dBs0y7Asw; shbid="18949\\05456853077686\\0541705513015:01f784b523da6fb7b7ed34578cee7d9e46efd31c45f1f6f7f25ba6f52c09e627204ea63a"; shbts="1673977015\\05456853077686\\0541705513015:01f7fc823f1b4efb5541f0897a5c5bfa40650a383f71d8d6701ca4209849e4faaca73ccd"; rur="PRN\\05456853077686\\0541705581753:01f7f245e00e8770f9c246f276499d4024bc987c64e56d5a8709f002fc37c9850894104c"; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=av8NEaBk8j-fO37gjut8FaeTvLnSEz04dRK1X0WI0FA.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRREFUTWlUTEZLTHpRWExyaGJtM2RMLTg5cFdSOTgwbFIyNncxYlJSRDI5czN1cVIwaU93MzdySG9LODFfdVN5NUFjdXNoRXgxTHFyYlFkc0lvR1JFa1p4bGNYQThRQTk4ZVV6bGtYZGY3SUpBS0xqS1NJaE5aSFlXaUhCMlpxaWhQaDFLZVFzcVhkN2JQQjRZOTBUMWhxdlpHRHlIc2JKdVBWMW9PdE80bGpBM2duY0NtRUhuUHZqbTJXWE40TEJvZkdzRnBjNDRqaVRrNHk5Tng3MFZKald0cDY1QmcyMGVuYzJhYm00V3pkWkVIY0MyR3RSQlZ0U045M0ZaN0tyM1RHLVhMSV9XR2lIREZjRzhqNXlfS2ZDTUVVenFXNHNlNGtsb3VYWWVVSjczc2R4OHpZR1FlOEg4YnJldWFoTzZCVGtxcVY0aXJDblJLemVfRmdKR1ZmIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVFaTFCa3FkbURFdjRsWkNuZTFOVVdBSDgycE5lMkYwZzNLUUtMdzY5dkVtdVpDNU5aQTFmWkNwNThxNWZzQ2JkWkJZTEJGQW9SUUkyZTlINWhxcE5JSlJnUHdMNXhyWkNSbm1IZHd5QVI1cHZ0U0VGd3pDY2FTdFVUaURXWHdYaVF6dGU3ekdnS0piejIxMkIzR1ZsNEtLelpCWkJ1UUU5NjFpR29aQ1AxQ3lwY01yMjBSVjZWZ1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzM5ODE2NzF9; fbsr_124024574287414=Rv3IIBiafnRV42s1y9Il5bUSH7pVANhk64hhFKK734s.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQzN4WGRJSl9QLWdlaGpzcVNQQ1RYODY4ckxqVzRub1AwYTQ2OUVMU2ZzaElrbmpyZnpxVGR1NXBSeHQ2VjBwOEo2TjdIaU5XTS00dTdkcEZzZEJtbW5tSmNJc2hZRHU4c095NUJ3ejBqZGJndWt2dTZ4eHU0RVNKLWh1RDd3eHE0RTd4YTRrY0tTUU9TOUgtSXJsYWs3UElwRHJMeGc5X09hQ2ZFek04NDhtdGJ1OWJnaWFDMXlHRlZpTE1lSnFjZVJIZkVpOVA3REltUmRRRkZKQnkyZUZ0aVdEcVBqRUdwUGc5V3FpRlBrTGp1SW10eXNiX0ZqcDFiSV91QjMyRWp2b1JVcmJtZDZMZzduYVZXRlpyTWNrM05panBTTk5YNVBCWk1PRnFObHpaek5jZjlOZVZfMEk1WTlrZjRNdHczSXB0QkJRZnNxaTlOV2JqVWJBeEVHQUVKYjJpLVpEeENlZGFTU0xCQk0zZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFDWkJZYkJCWVRnQkhiYkZGaXhIM1FPNjlQWWs4QVRUeUF4WkFXRGJVZ0twSExSakZ0RHB1OUxiVUFIMWRJREk2aERIY284ZjhvOVUzbk5qWHBpdVRIRTY4b1BqNWtIRGpaQWJFaFpCYUszWkNMTEZySkNDcGVQaHNaQ2Z1dzF3b3ZiQ1pDNENkQzZsYTA2WDRVTUcxS0N2M2pjSTEzbW1ZWkIzVG1mclZrSWNBbUlySTFxZFJpRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzQwNDU3MzZ9',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'can_support_threading': 'true',
    'min_id': '{"cached_comments_cursor": "17993125444659398", "bifilter_token": "KHkAwERihXApQAACmwCh39A_AMKOeGZ5tT8ABr5H_qLvPwBXEnc3RpI_AIhgyR4n0T8ASxEkU1nFPwCM9_nWRrs_AO1PTk5rR0AAMeysKwLHPwAVcCBqOs8_ANdm_bUHjD8AuUTkVL7fPwBaUwOQ5uY_AJ3fG4aMzkAAAA=="}',
}

comments_cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'rur': '"PRN\\05456853077686\\0541706434335:01f75aec09e69cb98999eb21ed48fc62a409bf090c0cb607949fbd0cc68dff129ae9a787"',
    'fbsr_124024574287414': 'Wub-h66H1zj0RmSRHkvSO1Wd8kCaQ3bxgBaOFAf3_sU.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQmZqMk1JVUxNNVcwRlUwODhqWmhYZnlFQ2NNTUZSeGUzcmNFTXhBaGtkTWdIemxKYkY4M3lHSkMwOVFPYlppY0tCQXJNZmxnZjJIeENkWC1HOG5FM2MzcThhMEtaX0tWbnpuaEtHd092dlY0Zmd5ckFXbjhtSjlNejFCby1oTVNQTUJxSUNKZEYyV25kSDZERjItb3FvbW9vcFlyREJMZGtPeDNSdkxjbGtBQjV4aEJoZVFzenhRSnF4MVVMMi1nMXd1WXVkcDBHZzRfOE0xNVV2ZHlRamd5Z2RFTDBaZzlnai1Qb3lyMk9IRDR4MjdZME9xYkdhWk9jaVkxbk5KSnc1bm5PLTVwY0lCY3RMMTFNWTN4Q2dOWkZUVjQwN2ZXQ21ZdXptX0s0bWh6NGdkU194S0ZzOTVwTVp3OUp1RnJkNkY4OUV2NVZIUFBrS0tJSk9oWEQwUUgyTWxDOGk4bmZ4LXlhdGdTYXZ2QSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFGanJGZjdXdEduMmdaQVg3V29vSkNWVTEwSXJCY2ptS2tuVjIyZ1pBRnRieVFleHlrdVNYSTcyRDN1WWZ6OG5EREFJd1JBNVNNOXlXTHNoWFRiUlV1V1RaQU42cWNtWTdtY0JBb1VHVzV5S2xDV2FhNDBFVW5Oa1c1Q0ZMYWtLUHFXSk93N0VmWkNBb2pzVUp3dFpDT0hLU1VaQzJWdGNwb2U4WkFzMmo4NWlkTWN6dEJZcUZRWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDg5ODMxMH0',
    'csrftoken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'ds_user_id': '56853077686',
    'sessionid': '56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdTUvKIEPWPmVvVB1xAl9fDMwUupp-IgkpyrQHs8A',
    'shbid': '"18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"',
    'shbts': '"1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"',
}

comments_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm8wWF',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/p/Cnd_PF5q8ui/',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="PRN\\05456853077686\\0541706434335:01f75aec09e69cb98999eb21ed48fc62a409bf090c0cb607949fbd0cc68dff129ae9a787"; fbsr_124024574287414=Wub-h66H1zj0RmSRHkvSO1Wd8kCaQ3bxgBaOFAf3_sU.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQmZqMk1JVUxNNVcwRlUwODhqWmhYZnlFQ2NNTUZSeGUzcmNFTXhBaGtkTWdIemxKYkY4M3lHSkMwOVFPYlppY0tCQXJNZmxnZjJIeENkWC1HOG5FM2MzcThhMEtaX0tWbnpuaEtHd092dlY0Zmd5ckFXbjhtSjlNejFCby1oTVNQTUJxSUNKZEYyV25kSDZERjItb3FvbW9vcFlyREJMZGtPeDNSdkxjbGtBQjV4aEJoZVFzenhRSnF4MVVMMi1nMXd1WXVkcDBHZzRfOE0xNVV2ZHlRamd5Z2RFTDBaZzlnai1Qb3lyMk9IRDR4MjdZME9xYkdhWk9jaVkxbk5KSnc1bm5PLTVwY0lCY3RMMTFNWTN4Q2dOWkZUVjQwN2ZXQ21ZdXptX0s0bWh6NGdkU194S0ZzOTVwTVp3OUp1RnJkNkY4OUV2NVZIUFBrS0tJSk9oWEQwUUgyTWxDOGk4bmZ4LXlhdGdTYXZ2QSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFGanJGZjdXdEduMmdaQVg3V29vSkNWVTEwSXJCY2ptS2tuVjIyZ1pBRnRieVFleHlrdVNYSTcyRDN1WWZ6OG5EREFJd1JBNVNNOXlXTHNoWFRiUlV1V1RaQU42cWNtWTdtY0JBb1VHVzV5S2xDV2FhNDBFVW5Oa1c1Q0ZMYWtLUHFXSk93N0VmWkNBb2pzVUp3dFpDT0hLU1VaQzJWdGNwb2U4WkFzMmo4NWlkTWN6dEJZcUZRWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDg5ODMxMH0; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdTUvKIEPWPmVvVB1xAl9fDMwUupp-IgkpyrQHs8A; shbid="18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"; shbts="1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'can_support_threading': 'true',
    'min_id': '{"cached_comments_cursor": "17981506852884848", "bifilter_token": "KHkAgXZAYGzlPwAikDiHS3w_AGKcowkqxj8AxHAfbU3JPwBGnnieXBVBAOhTDfMlzz8A12b9tQeMPwALlfiPnMY_AG53PWgqhT8ArreKnSjVPwAx7KwrAsc_ANMnck3v_D8A9QkzLsnBQABXEnc3RpI_ALlE5FS-3z8AAA=="}',
}



data1 = []
data2 = []
data3 = []
posts_ids_scraped = []

flag = True
profile_info_url = "https://www.instagram.com/api/v1/media/{}/info/"
post_url = "https://www.instagram.com/p/{}/"
profile_url = "https://www.instagram.com/{}/"


def Create_Database_connect_with_data():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client


def crawling_profile_info(product_id,profile_url,Post_url):
    try:
        item = dict()
        headers["Referer"] = Post_url
        response = requests.get(profile_info_url.format(product_id.split("_")[0]),headers=new_headers)
        if response.status_code == 401:
            print("Got 401 response So Sleep for 1-10 secends range....")
            time.sleep(random.randrange(1,5))
            new_headers["Referer"] = post_url
            response = requests.get(profile_info_url.format(product_id.split("_")[0]),headers=new_headers)            
        js = response.json()
        item["Profile Url"] = profile_url
        like_count = js["items"][0].get("like_count")
        item["like_count"] = like_count if like_count else ""
        post_image_url = js["items"][0]
        if post_image_url.get("carousel_media"):
            image_url =post_image_url["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
            item["image_url"] = image_url 
        elif post_image_url.get("image_versions2"):
            image_url = post_image_url["image_versions2"]["candidates"][0]["url"]
            item["image_url"] = image_url        
        code = js["items"][0].get("code")
        item["post_url"] = Post_url
        is_video = js["items"][0].get("video_versions")
        item["video_url"] = is_video[0].get("url") if is_video else ""
        item["is_video"] = True if is_video else False
        play_count = js["items"][0].get("play_count")
        item["play_count"] = play_count if play_count else ""
        data2.append(item)
    except Exception as e:
        print("Error in Profile_data :- {}".format(e))
        pass



def crawling_commits(cursor,profile_id,post_url,data):
    global flag
    while flag:
        try:
            params["min_id"] = cursor
            random_time = random.randrange(1,8)
            time.sleep(random_time)
            headers["Referer"] = post_url
            response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=params, cookies=comments_cookies,headers=comments_headers)
            
            if response.status_code == 401:
                print("Got 401 response So Sleep for 1-5 secends range....")
                time.sleep(random.randrange(1,5))
                new_headers["Referer"] = post_url
                response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=params, cookies=comments_cookies,headers=comments_headers)            
          
            js = response.json()
            comments = js.get("comments")
            next_cursor = js.get("next_min_id")
            for comment in comments:
                item = dict()
                item["profile_url"] = profile_url.format(js["caption"]["user"]["username"])
                item["post_image"] = data.get("image_url")
                item["post_comments"] = data.get("Total_Comments")
                item["post_like"] = data.get("Total_Likes")
                item["Is_video"] = data.get("Video Url")
                item["Is_blue_dot"] = data.get("Blue Dot")
                item["is_private"] = data.get("is_private")
                item["Post_title"] = data.get("post_text")
                item["full_name"] = data.get("full_name")
                item["post_id"] = data.get("post_id") 
                item["post_url"] = post_url
                commit_text  = comment.get("text")
                item["commit_text"] = commit_text if commit_text else ""
                pk_id = comment.get("pk")
                item["pk_id"] = pk_id if pk_id else ""
                comment_count = js.get("comment_count")
                item["comment_count"] = comment_count if comment_count else ""
                user_id = comment.get("user_id")
                item["user_id"] = user_id if user_id else ""
                status = comment.get("status")
                item["status"] = status if status else ""
                username = comment["user"].get("username")
                item["comment_Profile_url"] = profile_url.format(username) if username else ""
                item["comment_by_username"] = username if username else ""
                is_verified = comment["user"].get("is_verified")
                item["is_verified"] = is_verified if is_verified else False
                # is_private = comment["user"].get("is_private")
                # item["is_private"] = is_private if is_private else False
                comment_on_username = js["caption"]["user"].get("full_name")
                item["comment_on_username"] = comment_on_username if comment_on_username else ""
                item["Date"] = time.strftime("%Y-%d-%m")
                item["Time"] = time.strftime("%H:%M:%S")
                mycol.insert_one(item)
                print(item)
                print("Inserting to DB......")
                # data1.append(item)
            if next_cursor:
                print("Next Cursor :- {}".format(next_cursor))
                cursor = next_cursor
            else:
                flag = False
        except Exception as e:
            print("Error in crawling_commits function :- {}".format(e))
            print("sleeping for 10")
            time.sleep(10)
            continue



def crawling_first_page_comments(product_id,post_url,data):
    try:
        if data.get("post_id") not in posts_ids_scraped:
            posts_ids_scraped.append(data.get("post_id"))
            random_time = random.randrange(1,5)
            time.sleep(random_time)
            params = {'can_support_threading': 'true','permalink_enabled': 'false',}
            new_headers["Referer"] = post_url

            response = requests.get(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', params=params, headers=new_headers)
            
            if response.status_code == 401:
                print("Got 401 response So Sleep for 1-10 secends range....")
                time.sleep(random.randrange(1,10))
                response = requests.get(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', params=params, headers=new_headers)
            
            js = response.json()
            comments = js.get("comments")
            next_cursor = js.get("next_min_id")
            for comment in comments:
                item = dict()
                item["profile_url"] = profile_url.format(js["caption"]["user"]["username"])
                item["post_image"] = data.get("image_url")
                item["post_comments"] = data.get("Total_Comments")
                item["post_like"] = data.get("Total_Likes")
                item["Is_video"] = data.get("Video Url")
                item["Is_blue_dot"] = data.get("Blue Dot")
                item["is_private"] = data.get("is_private")
                item["Post_title"] = data.get("post_text")
                item["full_name"] = data.get("full_name")
                item["post_id"] = data.get("post_id") 
                item["post_url"] = post_url
                commit_text  = comment.get("text")
                item["commit_text"] = commit_text if commit_text else ""
                pk_id = comment.get("pk")
                item["pk_id"] = pk_id if pk_id else ""
                comment_count = js.get("comment_count")
                item["comment_count"] = comment_count if comment_count else ""
                user_id = comment.get("user_id")
                item["user_id"] = user_id if user_id else ""
                status = comment.get("status")
                item["status"] = status if status else ""
                username = comment["user"].get("username")
                item["comment_Profile_url"] = profile_url.format(username) if username else ""
                item["comment_by_username"] = username if username else ""
                is_verified = comment["user"].get("is_verified")
                item["is_verified"] = is_verified if is_verified else False
                is_private = comment["user"].get("is_private")
                item["is_private"] = is_private if is_private else False
                comment_on_username = js["caption"]["user"].get("full_name")
                item["comment_on_username"] = comment_on_username if comment_on_username else ""
                item["Date"] = time.strftime("%Y-%d-%m")
                item["Time"] = time.strftime("%H:%M:%S")
                mycol.insert_one(item)
                print(item)
                print("Inserting to DB......")
                # data1.append(item)
            if next_cursor:
                print("Next Cursor Sending to crawling_first_page_comments function :- {}".format(next_cursor))
                time.sleep(10)
                crawling_commits(next_cursor,product_id,post_url,data)
            else:
                print("Not found the next page cursor")
    except Exception as e:
        print("Error in crawling_first_page_comments :- {}".format(e))





# Taking data from input file and getting data
# f = open("input_data.json","r").read()
# input_data = json.loads(f)




# Creating DataBase connection and fetching data from DB
fetch_data_from_database = []
print("Creating Connection for DB and fetching data")
client = Create_Database_connect_with_data()
time.sleep(2)
mydb = client["instagram"]
collection = mydb["instagram_profiles_POST_Virat_Kholi"]
collection_data = collection.find({"full_name":"Virat Kohli"})
for data in collection_data:
    fetch_data_from_database.append(data)
    # posts_ids.append(data.get("post_id"))


mydb = client["instagram"]
mycol = mydb["instagram_POST_Comments_Virat_Kohli"]

print("fetching data for {} now..... AND Total post are {}.......".format(fetch_data_from_database[0].get("full_name"),len(fetch_data_from_database)))
# Two function for fetching comments and details for every post... 
for in_data in fetch_data_from_database[0:10]:
    post_id = in_data["post_id"]
    post_url = in_data["Post_url"]
    crawling_first_page_comments(post_id,post_url,in_data)


# crawling_first_page_comments("3026009462037888780_5486909","https://www.instagram.com/p/Cn-i5K_vT8M/",fetch_data_from_database[0])


# for in_data in fetch_data_from_database:
#     post_id = in_data["post_id"]
#     profile_url = in_data["profile_url"]
#     Post_url = in_data["Post_url"]
#     print("crawling_first_page_comments Function Completed Now.......... And Sleeping for 5 sec..")
#     time.sleep(5)
#     crawling_profile_info(post_id,profile_url,Post_url)

# merging post and comments into a list
# print("crawling_profile_info Function Completed Now..........")
# for dt1 in data1:
#     for dt2 in data2:
#         dt1.update(dt2)
#         data3.append(dt1)



# Pushing Data in DB
# print("Total Comments in length is :- {}".format(len(data1)))
# print("Comments are scraped with profile details Pushing LocalDB now.....")
# time.sleep(4)
# mydb = client["instagram"]
# mycol = mydb["instagram_POST_Comments"]
# for data in data1:
#     print("Geting product url :- {}".format(data))
#     mycol.insert_one(data)
#     print("Inserted DB .......")


# If you want to Create data in Excel then Acitvate this lines of comment excel file will generate....
# df = pd.DataFrame(data3)
# df.to_excel("commints_of_post_of_Virat_kholi.xlsx",index=False)
# print("Processed is completed now File is Generated now PL check .............")








# url = "https://www.instagram.com/api/v1/media/3018548393001277430/comments/?can_support_threading=true&permalink_enabled=false"
# Calling Functions Here
# currentDateAndTime = datetime.now()
# current_time = currentDateAndTime.strftime("%H:%M:%S")

# current_cursor = '{"cached_comments_cursor": "17975624305950587", "bifilter_token": "KHkAwLkltqDpPwCBO9NHRN4_AKIVcZqDxz8AQ-LZNqfaQADkK_skr8c_AAOi_XSq4j8AbIW6QTXFPwDt9dcFZew_ANHhwp2vqj8Acr6Z8WjFPwBUnsMiFeY_ANWcwvT_gT8At_fG8zrFPwBajV_7kOY_AJ0Uw3Tnzj8AAA=="}'
# product_id = "3017474773819626429"
# post_url = "https://www.instagram.com/p/CngOVHMOJO9/"
# crawling_commits(current_cursor,product_id,post_url)
# print("crawling_commits Function Completed Now.......... And Sleeping for 10 sec..")
# time.sleep(5)
# crawling_profile_info(product_id)
# print("crawling_profile_info Function Completed Now..........")






# db('instagram').collection('instagram_POST_Comments').aggregate([{$group: {_id:{profile_url:"$profile_url",comment_by_username:"$comment_by_username"}}}])