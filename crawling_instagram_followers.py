from requests import Session
import requests
import pandas as pd
from lxml import html
import time
import random

base_url = "https://www.instagram.com/{}/"

next_url = "https://www.instagram.com/api/v1/friendships/51943876446/followers/?count=12&max_id={}&search_surface=follow_list_page"
data = []


cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'csrftoken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'ds_user_id': '56853077686',
    'sessionid': '56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdtHmLsK2SwGv2lpZPbHNWust8BaJTGeKsURXDaQ20',
    'shbid': '"18949\\05456853077686\\0541717563683:01f7e2b658d9717a77104d05c7f06a4927da2c99db7ed2a7b6b6f19d4d93d6d83f880e5a"',
    'shbts': '"1686027683\\05456853077686\\0541717563683:01f74d901903dac2f5b3929a92411ff4a4cd1540ad6ac921e95d7d48cd8c2d853ad90876"',
    'rur': '"PRN\\05456853077686\\0541717565127:01f767d6e9bcdcf064f7f154901ae3ef2b0f57230651f48a3e33440e9af7cc766265cadf"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm89WG',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/elonmask_ceo/',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdtHmLsK2SwGv2lpZPbHNWust8BaJTGeKsURXDaQ20; shbid="18949\\05456853077686\\0541717563683:01f7e2b658d9717a77104d05c7f06a4927da2c99db7ed2a7b6b6f19d4d93d6d83f880e5a"; shbts="1686027683\\05456853077686\\0541717563683:01f74d901903dac2f5b3929a92411ff4a4cd1540ad6ac921e95d7d48cd8c2d853ad90876"; rur="PRN\\05456853077686\\0541717565127:01f767d6e9bcdcf064f7f154901ae3ef2b0f57230651f48a3e33440e9af7cc766265cadf"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}



def crawling_followers(url):
    response = requests.get(url,headers=headers,cookies=cookies)
    json_data = response.json()
    products = json_data.get("users")
    for product in products:
        item = dict()
        username = product.get("username")
        item["User_Name"] = username if username else ""
        item["Product_url"] = base_url.format(username)
        profile_pic_id = product.get("profile_pic_id")
        item["profile_pic_id"] = profile_pic_id if profile_pic_id else ""
        full_name = product.get("full_name")
        item["full_name"] = full_name if full_name else ""
        pk_id = product.get("pk_id")
        item["pk_id"] = pk_id if pk_id else ""
        is_private = product.get("is_private")
        item["is_private"] = is_private if is_private else ""
        profile_pic_url = product.get("profile_pic_url")
        item["profile_pic_url"] = profile_pic_url if profile_pic_url else ""
        print(item)
        data.append(item)




url = "https://www.instagram.com/api/v1/friendships/51943876446/followers/?count=12&search_surface=follow_list_page"
follower_url = "https://www.instagram.com/api/v1/friendships/2215130631/followers/?count=12&search_surface=follow_list_page"
crawling_followers(follower_url)


df = pd.DataFrame(data)
df.to_excel("instagram_followers_pooja_jha2323.xlsx",index=False)
