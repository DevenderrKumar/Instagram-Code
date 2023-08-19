from requests import Session
import requests
import pandas as pd
from lxml import html
import time
from pymongo import MongoClient
import random
import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = client["instagram"]
logs_collection = mydb["instagram_logs"]
mycol = mydb["instagram_profiles_POST_Links"]


next_page_url = "https://www.instagram.com/api/v1/feed/user/{}/?count=12&max_id={}"
post_url = "https://www.instagram.com/p/{}/"
profile_url = "https://www.instagram.com/{}/"

data = []

cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'csrftoken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'ds_user_id': '56853077686',
    'sessionid': '56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYcZ08waRnaYmt3XkyqAYyrnGQGsK132xlItqRbbNJ8',
    'shbid': '"18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"',
    'shbts': '"1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"',
    'rur': '"PRN\\05456853077686\\0541717925060:01f710b51f99bcd2894786cfd0efcf7f4a4e9b562711dd4da103fca1e72a9d8479538da8"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm8zoU',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/p/CtIxMlcp9JW/',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYcZ08waRnaYmt3XkyqAYyrnGQGsK132xlItqRbbNJ8; shbid="18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"; shbts="1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"; rur="PRN\\05456853077686\\0541717925060:01f710b51f99bcd2894786cfd0efcf7f4a4e9b562711dd4da103fca1e72a9d8479538da8"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def Create_Database_connect_with_data():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client


def CrawlingLinks(RawData):
    PostID = RawData.get("post_id")
    response = requests.get(f'https://www.instagram.com/api/v1/media/{PostID}/likers/', cookies=cookies, headers=headers)
    json_data = response.json()
    LinksCount = json_data.get("users")
    headers["Referer"] = RawData.get("Post_url")
    if LinksCount:
        for links_count in LinksCount:
            item = dict()
            item["PostUrl"] = RawData.get("Post_url")
            item["username"] = links_count.get("username") if links_count.get("username") else ""
            item["pk_id"] = links_count.get("pk_id") if links_count.get("pk_id") else ""
            item["pk"] = links_count.get("pk") if links_count.get("pk") else ""
            item["full_name"] = links_count.get("full_name") if links_count.get("full_name") else ""
            item["is_private"] = links_count.get("is_private") if links_count.get("is_private") else ""
            item["is_verified"] = links_count.get("is_verified") if links_count.get("is_verified") else ""
            item["profile_pic_id"] = links_count.get("profile_pic_id") if links_count.get("profile_pic_id") else ""
            item["profile_pic_url"] = links_count.get("profile_pic_url") if links_count.get("profile_pic_url") else ""
            print(item)
            mycol.insert_one(item)
            print("Inserted DB .......")






print("Creating Connection for DB and fetching data")
client = Create_Database_connect_with_data()
time.sleep(2)
mydb = client["instagram"]
collection = mydb["instagram_profiles_POST"]
# collection_data = collection.find({})
collection_data = collection.find({})
for data in collection_data[:200]:
    CrawlingLinks(data)

# CrawlingLinks("3118959111076041302")