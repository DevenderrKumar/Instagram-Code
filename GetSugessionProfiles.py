import json
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
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs


client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["instagram_ViralPitch"]
# logs_collection = mydb["instagram_logs"]
mycol = mydb["instagram_profiles_Suggession"]

suggession_data = []
base_url = "https://www.instagram.com/{}"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
 'Accept': '*/*',
 'Accept-Language': 'en-US,en;q=0.5',
 'X-IG-D': 'www',
 'Content-Type': 'application/x-www-form-urlencoded',
 'X-FB-LSD': 'awSamDzatUFJUwCH0k6D8z',
 'X-ASBD-ID': '129477',
 'Origin': 'https://www.instagram.com',
 'Alt-Used': 'www.instagram.com',
 'Connection': 'keep-alive',
 'Referer': 'https://www.instagram.com/keshavi_chhetri_official/similar_accounts/',
 'Sec-Fetch-Dest': 'empty',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Site': 'same-origin',
 'Pragma': 'no-cache',
 'Cache-Control': 'no-cache'}


def login_insta(username,password):
    login_url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    ck = requests.get(login_url)
    crsf = ck.cookies['csrftoken']
    headers = {
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-ch-ua-platform':'Linux',
        'x-csrftoken': crsf}
    time = int(datetime.now().timestamp())
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',  # <-- note the '0' - that means we want to use plain passwords
        'queryParams': {},
        'optIntoOneTap': 'false'}
    # res = requests.post(login_url,data=payload,headers=headers,proxies=proxieslt)
    res = requests.post(login_url,data=payload,headers=headers)
    print(res)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    return res




def GetLikes(ProfileUrl_,LoginCookies):
    print(ProfileUrl_,LoginCookies)
    HomeResponse = GetHomePage(ProfileUrl_,LoginCookies)
    soup = bs(HomeResponse,features="lxml")
    PostID = soup.find("meta",{"property":"al:ios:url"}).get('content').split("=")[-1]
    response = requests.get(f'https://www.instagram.com/api/v1/media/{PostID}/likers/', cookies=LoginCookies, headers=headers)
    json_data = response.json()
    LinksCount = json_data.get("users")
    headers["Referer"] = ProfileUrl_
    if LinksCount:
        for links_count in LinksCount:
            item = dict()
            item["PostUrl"] = ProfileUrl_
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
            # print("Inserted DB .......")




# This function is used to get the ID and qurey key from home page
def GetHomePage(url,LogingCookies):
    response = requests.get(url, cookies=LogingCookies, headers=headers)
    # return response.text

    # For CodeID to get for Suggession profiles urls needs to return the CodeID
    CodeID = re.findall('"user\_id"\:"(.*?),',response.text)
    return CodeID[0] 

def GetSugessions(url,username_,LogingCookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRFToken': '2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '129477',
        'X-IG-WWW-Claim': 'hmac.AR1qYgzflBqc55DVe0II_XRzbTQkUNQvy_nKNGcUgeIgPqEO',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': f'https://www.instagram.com/{username_}/',
        # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"; shbts="1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"; csrftoken=2vT8lqOf1rkXalPqabg1ofJVqkVjBKPM; ds_user_id=14816613506; sessionid=14816613506%3AdtYo2Rtqv52izx%3A27%3AAYdXYfpo3-M5yNFAcmdvfRQ7VDb5JBCSyoqL6UZpgg; rur="PRN\\05414816613506\\0541718180169:01f7987846bcd1edfa05020f95268737b1b2ea5f9fbc435a54500d5c07befc7fdd609fa8"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    response = requests.get(url, cookies=LogingCookies, headers=headers)
    json_data = response.json()
    Edges = json_data["data"]["user"]["edge_chaining"]["edges"]
    for edge in Edges:
        item = dict()
        username = edge["node"]["username"]
        full_name = edge["node"]["full_name"]
        is_private = edge["node"]["is_private"]
        is_verified = edge["node"]["is_verified"]
        profile_pic_url = edge["node"]["profile_pic_url"]
        profile_url = f"https://www.instagram.com/{username}/"
        item["username"] = username
        item["full_name"] = full_name
        item["is_private"] = is_private
        item["is_verified"] = is_verified
        item["profile_pic_url"] = profile_pic_url
        item["profile_url"] = profile_url
        print(item)
        mycol.insert_one(item)
        # suggession_data.append(item)



# user_pass = [{'username':'ajeetkumar2oiiop','password':'Ajeet@10'},
#             {'username':'Amita89852','password':'Ajeet@10'},
#             {'username':'kunal986312','password':'Ajeet@10'},
#             {'username':'mekeja7kumar','password':'@Aa123456'}]


def StartProcess():
    user_pass = [{'username':'Amita89852','password':'Ajeet@10'}]

    # It is used to read files and for profiles and hit one by one
    # df = pd.read_excel("instagram_suggessions_updated.xlsx")
    # df = df.drop_duplicates(["username"])

    # _Prfofile_urls = [{"profile_url":"https://www.instagram.com/martateresaxsaltyvibes/","username":"martateresaxsaltyvibes"},{"profile_url":"https://www.instagram.com/rezzaut/","username":"rezzaut"}]
    
    
    _Prfofile_urls = ["martateresaxsaltyvibes","rezzaut","gojooosatoru259","everything_my_bro","sisodiya___jyoti","mo_hini_8145","girija_partap_0007"]
    for userpass in user_pass:
        res = login_insta(userpass["username"],userpass["password"])
        LogingCookies = res.cookies.get_dict()
        for _len in range(len(_Prfofile_urls)):
            # PrData = df.iloc[_len].to_dict()
            PrData = _Prfofile_urls[_len]
            # GetLikes(PrData,LogingCookies) # Getting Likes from Post


            # Need to uncomment for GetSuggessions profiles urls
            GetData = GetHomePage(base_url.format(PrData),LogingCookies)
            api_url = "https://www.instagram.com/graphql/query/?query_hash=d4d88dc1500312af6f937f7b804c68c3&user_id={}&include_chaining=false&include_reel=true&include_suggested_users=false&include_logged_out_extras=false&include_live_status=false&include_highlight_reels=true".format(GetData).replace('"',"")
            api_url = api_url.replace('"',"")
            GetSugessions(api_url,PrData,LogingCookies) # Getting Seggessions profiles from profiles 
            





StartProcess()




# df = pd.DataFrame(suggession_data)
# df.to_excel("instagram_suggessions_updated__TwoUrls.xlsx",index=False)









# Requests instagram without cookies
# import requests

# cookies = {}

# headers = {
#     'authority': 'www.instagram.com',
#     'accept': '/',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
#     'cache-control': 'no-cache',
#     # 'cookie': 'mid=YR-xcwAEAAGZ7rpVv5Lb75f1M6wY; ig_did=01F3BE4F-F405-4973-8D72-FE0A6F7CE8C4; fbm_124024574287414=base_domain=.instagram.com; datr=QFyKYebyWFAxzcGHf7aTKCq9; ig_nrcb=1; shbid="7509\\0548802916640\\0541718095517:01f75de596d0bad58ca935ef913e2b04cb573edfb7633ca1384ec2be08df0a1dfba5accb"; shbts="1686559517\\0548802916640\\0541718095517:01f759dcb1fa85c8511c7e4bf6bca1004a22019277d4b057a3f23982002978e393082791"; csrftoken=FkB9cFuY0FiIkDHci3w30n249HIN7lQi; ds_user_id=59877467676; sessionid=59877467676%3AkoAqfjmLlzjcQD%3A2%3AAYdt-iixH0cbQwxshvAvBBy-7mj6ZwpVAYM8dmcIlw; fbsr_124024574287414=UxJmQFHPGR6feRYWdWpd6d9Ye7ACW1ALJfJ9_KP8a8I.eyJ1c2VyX2lkIjoiMTAwMDI5NTY0MDc3MjQ3IiwiY29kZSI6IkFRQjd0VUJSb3Q4VzBiYXdhWHFOZU4zbTJPR0t6THhwT0ctTVl4YjgzLURFZl9FZnA0VXRudkJpVjJBc2hMZ0UtTTdocWtuaDZ5ajRxaU9FenpacGlfYURQTnZuOERBcndxQlhlQnN1QWVMR2JpaWJfaTM3bzNnZXpmZTZ4WVRjcnNGNWt2aFRWb1ExU0M4cjc1bG1qSlZQX0wwQ2VGcjRkV3RTT2VybzExcFo2R0ItZlJlNUFuaEVsQzJVVmlYb2ZXbTREZ01yWF9kQnFxVHZoMXBXRkdDUjhPd2prcG9ackNRTENfSTVZOHhYRUtMZHNEWmRIbkZUZlVXZENqQ1VCVkplbVNRdXhLNV9iTW13REhYMG5QOHVhQmFzblZpLW1sNVZ0MDlMbi1aUjAtM1RnZ1duZGgyM1ZFN0JXdHlRdzNNTlRRcjN2Z05BNUE3TjdEUVVCaEI0aXc3M3QyV093RVpNd0R3Y1VhQ2pwZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFMbDQ2NXBLcHRIODZuTXV6VU0zcGIyTGFUdWtVMkRaQ2VHdEk3aTRzR2RMVG9jSTIxTkY5elZNTDR0TVJOa3BCekNVVHVLZW82OUp2TWxmTmlFWkFqTldhdnBBaVdwZEVReDJqVHdBY0gyS3hQNGVlVEVJU2pmcXRPZXZMazZiRll6dlpCV1cyR2diNDlhRURJSEkxZEVVU240REdGcjR1SFE4dE50OWowZEpHSW9GdklaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2NjU4OTM1fQ; fbsr_124024574287414=s2AePsV6UQHZchueMzcZTefQ30RrUhHHloHyDhsxrc0.eyJ1c2VyX2lkIjoiMTAwMDI5NTY0MDc3MjQ3IiwiY29kZSI6IkFRQUZJTmVUd3JNb08xZDFVWG5lanFYVWRlcWd5V3lvX1k4eTl3Mzc3MlB4dUNWWHhqZHpHcnlFYkVTeVM5N3pYS1NJeTFyQkthUHpab3JyeUg0dGJZaHVaekdQOWQ2TEx5QkNyOHl5U2tMYVZIa3ZzM1I2UnpYakM1Q2Vnam1xVWhyQ2haMndCb1JqSXd5akpzNkg3MmpOa3lYTFhheGZLaV9jTFZOMkx3WTVhLUs3T1FsVWxhdTRvemRWRzQ5bnVNMkpJVU9LV0p6ekNlUjY5SWF4UUdaVVlXamtGa1NtYXpvTTNwZUdXcEw0OENJbFBvRGc3MG9rS3c1UFBRRXN0X1N2RUsxOGRhb2RGRjhBaHQwb093ZzBJclA0a191MTNQTTFickJGb0ZRRVRnSTZmdjctTjM0RmZnMkJ2TU5wTGRLVzhNZHNtMThDaUFoZ25HZ014a1djZnZqQWpORF9VNlB2VzlLeURXdWJyZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFDRFcwcklzWkNWWkE2eWFIMk1GTXoyWkE5WkFUNnZVdEhHU2JCemRmcTFYT3U2bVFheVRRVEpmTGllT1k3czAzNFhXM0xvZEFyMVRXeUUzbm1CSGFIODlmS05qaXR2NTZlU0RpZ25YRlZjdWp0QTVhejkzblFGWUtGNHNIT3NDVFpBRHpNMFM5eEg5bHIxdFVyS1BEUHFsM1hzV0tPU3cxNFA0MzBHenVVSk05NDRWOGZRQVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODY2NTg5NDV9; rur="VLL\\05459877467676\\0541718194953:01f736f420e965f455af2cf3198f85cf38dacb15f7c09aa6c5fc2781acae495f06fd2723"',
#     'pragma': 'no-cache',
#     'referer': 'https://www.instagram.com/therock/',
#     'sec-ch-prefers-color-scheme': 'light',
#     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#     'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.106", "Google Chrome";v="114.0.5735.106"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-ch-ua-platform-version': '"5.15.0"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'viewport-width': '1848',
#     'x-asbd-id': '129477',
#     'x-csrftoken': 'FkB9cFuY0FiIkDHci3w30n249HIN7lQi',
#     'x-ig-app-id': '936619743392459',
#     'x-ig-www-claim': 'hmac.AR2SVTJm4yUlDchYRErjZRSjYVgAxC_WFHwUnLBma_Pidv9F',
#     'x-requested-with': 'XMLHttpRequest',
# }

# params = {
#     'username': 'therock',
# }

# response = requests.get(
#     'https://www.instagram.com/api/v1/users/web_profile_info/',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )