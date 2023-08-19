import requests
import time
import random
import pymongo
import logging
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import logging
import pymongo,datetime
from datetime import datetime
from datetime import timedelta
from collections import Counter

import argparse
import re,os,json,requests
import pymongo,datetime
from google.cloud import storage
import hashlib
import os
import dateutil.parser as dp

# import cv2
import numpy as np
from warnings import filterwarnings
import random
import pdb
from datetime import datetime
from multiprocessing import Process
from fake_headers import Headers

flag = True



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
 'Accept': '*/*',
 'Accept-Language': 'en-US,en;q=0.5',
 'X-CSRFToken': 'FiNRRKhMpxDBSdptzIwEJ1JAynmDsuW3',
 'X-IG-App-ID': '936619743392459',
 'X-ASBD-ID': '129477',
 'X-IG-WWW-Claim': 'hmac.AR3j75b5XiHq6RpE4jyiLHDXPGp4ZW8PyOjqOFCcZAYCJB4Q',
 'X-Requested-With': 'XMLHttpRequest',
 'Connection': 'keep-alive',
 'Referer': 'https://www.instagram.com/martateresaxsaltyvibes/',
 'Sec-Fetch-Dest': 'empty',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Site': 'same-origin',
 'Pragma': 'no-cache',
 'Cache-Control': 'no-cache'}

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


GotPost = list()
GotSuggession = list()
GotLikes = list()
GotComments = list()
GotReels = list()


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["ViralPitch_Intagram_Scraper"]
Likes_ = mydb["Intagram_likes_new"]
Suggessions = mydb["Intagram_Suggessions_new"]
Reels = mydb["Intagram_Reels_new"]
Posts = mydb["Intagram_Post_new"]



class GetAllSuggessions:

    def __init__(self):
        self.base_url = "https://www.instagram.com/{}"
        self.headers = headers
        self.ReelsUrl = "https://www.instagram.com/reel/{}/"
        self.PostApiUrl = "https://www.instagram.com/api/v1/clips/user/"
        self.data = {'include_feed_video': 'true','page_size': '12','target_user_id': '173560420'}
        self.new_headers = new_headers
        self.NextParams = {'can_support_threading': 'true','min_id': '{"cached_comments_cursor": "17981506852884848", "bifilter_token": "KHkAgXZAYGzlPwAikDiHS3w_AGKcowkqxj8AxHAfbU3JPwBGnnieXBVBAOhTDfMlzz8A12b9tQeMPwALlfiPnMY_AG53PWgqhT8ArreKnSjVPwAx7KwrAsc_ANMnck3v_D8A9QkzLsnBQABXEnc3RpI_ALlE5FS-3z8AAA=="}'}
        self.post_url = "https://www.instagram.com/p/{}/"
        self.profile_url = "https://www.instagram.com/{}/"
        self.user_pass = [{'username':'devender85068202522023','password':'Dev@1234'}]
        self.next_comments_params = {'can_support_threading': 'true','min_id': '{"server_cursor": "QVFDWDZGTW1UeTZFX3hyM2dzSG8wcjN5dDlVYmVKZzZ0MnVyaWsyWGh5TkQ4WW5qSkI1a0dZVHN4OVN3Ry1jcTlpNlBIQXFnelJHUmhMRGRpU1Y5RXV1OFFhYjNHaXpZMHFVQTdVUTA2VnNoSEE=", "is_server_cursor_inverse": true}',}
        self.LikesCookies  = {'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
                'datr': 'xKmkYzg_H2hB218oV81-7V7g',
                'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
                'ig_nrcb': '1',
                'fbm_124024574287414': 'base_domain=.instagram.com',
                'shbid': '"16489\\05414816613506\\0541718183157:01f78423e95aebfda20f2b631032b72e8937638fdc5a420ca4e7327b8da2a349fcd45866"',
                'shbts': '"1686647157\\05414816613506\\0541718183157:01f796dbfe56bdc11597d892cba4fe5dddbd8c5b3f1a909eb815de68a7351699d21b2cec"',
                'ds_user_id': '59934099250',
                'csrftoken': 'kHNHphxDchKHkPOWehbvq1kFv8I4PP5E',
                'rur': '"RVA\\05459934099250\\0541718454218:01f7085915e66cdb283f7779dd15ce023ae3fccac53972efc2dd176ae1088bb4e294c080"',
                'sessionid': '59934099250%3A3Bdw5pGEDxD9l9%3A17%3AAYfqE59S3YixQZjwE0EfxRpCEK0f-evCeHGrrRkFiA'}
        self.comments_headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-CSRFToken': 'FiNRRKhMpxDBSdptzIwEJ1JAynmDsuW3',
                'X-IG-App-ID': '936619743392459',
                'X-ASBD-ID': '129477',
                'X-IG-WWW-Claim': 'hmac.AR3j75b5XiHq6RpE4jyiLHDXPGp4ZW8PyOjqOFCcZAYCJBBI',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/p/CCIcO6khRE3/',
                # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="16489\\05414816613506\\0541718183157:01f78423e95aebfda20f2b631032b72e8937638fdc5a420ca4e7327b8da2a349fcd45866"; shbts="1686647157\\05414816613506\\0541718183157:01f796dbfe56bdc11597d892cba4fe5dddbd8c5b3f1a909eb815de68a7351699d21b2cec"; rur="EAG\\05459910281066\\0541718350938:01f769c9e30baf96c8e47658a6e0b3f8391b22be378b088a9116a6bcb77360a45cb2c689"; sessionid=59910281066%3ARTpXo4Qu7Uvvwo%3A17%3AAYcCNWGy7_6dFP_9FrpD3nI-gln8I8KZk-IzScX80Q; ds_user_id=59910281066; csrftoken=FiNRRKhMpxDBSdptzIwEJ1JAynmDsuW3',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
        

    def Create_Database_connect_with_data(self):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            return client
        except Exception as e:
            logging.error("Error in Create_Database_connect_with_data :- {}".format(e))
            pass

    def getBucketProfile(self, item):
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/var/live/gtranslateapi-d9895ca275db.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/mac/Desktop/scraping Project/ScrapInstagram/gtranslateapi-d9895ca275db.json"
        bucket_name = "liveprofiledata"
        storage_client = storage.Client()
        BUCKET = storage_client.bucket(bucket_name)
        try:
            filename = 'live_'+str(item)+'_live.json'
            #print(filename)
            blob = BUCKET.blob(filename)
            if blob:
                data = json.loads(blob.download_as_string(client=None))
        except Exception as er :
            opi=1
            data={}
        return data


    def GetReels(self,product_id,PRCODE):
        try:
            _profile_url_ = self.profile_url.format(PRCODE)
            print("Fetching Data For :- {}".format(_profile_url_))
            time.sleep(random.randint(1,6))
            cookies = {}
            self.data["target_user_id"]=product_id[0]
            req = requests.post(self.PostApiUrl, cookies=cookies, headers=headers, data=self.data)
            json_data = req.json()
            AllReels = json_data.get("items")
            for Reel in AllReels:
                item = dict()
                item["ProfileUrl"] = _profile_url_
                item["product_id"] = product_id[0]
                try:
                    Reels_url = self.ReelsUrl.format(Reel["media"]["code"])
                    item["ReelsUrl"] = Reels_url
                except Exception as e:
                    logging.error("Error in ReelsUrl Pl check :- {}".format(e))
                try:
                    ReelsText = Reel.get("media")
                    item["ReelsText"] = ReelsText.get("caption").get("text") if ReelsText.get("caption") else ""
                except Exception as e:
                    logging.error("Error in ReelsText :- {}".format(e))
                try:
                    status = Reel.get("media")
                    item["Active/Not"] = status.get("caption").get("status") if status.get("caption") else ""
                except Exception as e:
                    logging.error("Error in Active/Not :- {}".format(e))
                try:
                    play_count = Reel.get("media")
                    item["play_count"] = play_count.get("play_count") if play_count.get("play_count") else ""
                except Exception as e:
                    logging.error("Error in play_count :- {}".format(e))
                try:
                    username = Reel.get("media")
                    item["username"] = username.get("user").get("username") if username.get("user") else ""
                except Exception as e:
                    logging.error("Error in username :- {}".format(e))
                try:
                    full_name = Reel.get("media")
                    item["full_name"] = full_name.get("user").get("full_name") if full_name.get("user") else ""
                except Exception as e:
                    logging.error("Error in full_name :- {}".format(e))
                try:
                    comment_count = Reel.get("media")
                    item["comment_count"] = comment_count.get("comment_count") if comment_count.get("comment_count") else ""
                except Exception as e:
                    logging.error("Error in comment_count :- {}".format(e))
                try:
                    like_count = Reel.get("media")
                    item["like_count"] = like_count["like_count"] if like_count.get("like_count") else ""
                except Exception as e:
                    logging.error("Error in like_count :- {}".format(e))

                try:
                    video_duration = Reel.get("media")
                    item["video_duration"] = video_duration["video_duration"] if video_duration.get("video_duration") else ""
                except Exception as e:
                    logging.error("Error in video_duration :- {}".format(e))

                try:
                    has_audio = Reel.get("media")
                    item["has_audio"] = has_audio["has_audio"] if has_audio.get("has_audio") else ""
                except Exception as e:
                    logging.error("Error in has_audio :- {}".format(e))

                try:
                    has_audio = Reel.get("media")
                    item["has_audio"] = has_audio["has_audio"] if has_audio.get("has_audio") else ""
                except Exception as e:
                    logging.error("Error in has_audio :- {}".format(e))

                try:
                    pk_id = Reel.get("media")
                    item["PK_ID"] = pk_id["pk"] if pk_id.get("pk") else ""
                except Exception as e:
                    logging.error("Error in pk :- {}".format(e))
            
                try:
                    ID_ = Reel.get("media")
                    item["ID"] = ID_["id"] if ID_.get("id") else ""
                except Exception as e:
                    logging.error("Error in ID_ :- {}".format(e))


                try:
                    video_versions = Reel.get("media")
                    item["video_versions"] = video_versions["video_versions"][0]["url"] if video_versions.get("video_versions") else ""
                except Exception as e:
                    logging.error("")
                item["Date"] = time.strftime("%Y-%d-%m")
                item["Time"] = time.strftime("%H:%M:%S")
                # GotReels.append(item)
                print("Getting The Reels :- {}".format(PRCODE))
                Reels.insert_one(item)
        except Exception as e:
            logging.error("Error in Getting The Reels Function :- {}".format(e))
            pass

    def GetLIkes(self,PostID,PostUrl,userpass,LogingCookies,ProfileName):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-CSRFToken': LogingCookies["csrftoken"],
                'X-IG-App-ID': '936619743392459',
                'X-ASBD-ID': '129477',
                'X-IG-WWW-Claim': 'hmac.AR3j75b5XiHq6RpE4jyiLHDXPGp4ZW8PyOjqOFCcZAYCJFMN',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Referer': f'{PostUrl}',
                # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="16489\\05414816613506\\0541718183157:01f78423e95aebfda20f2b631032b72e8937638fdc5a420ca4e7327b8da2a349fcd45866"; shbts="1686647157\\05414816613506\\0541718183157:01f796dbfe56bdc11597d892cba4fe5dddbd8c5b3f1a909eb815de68a7351699d21b2cec"; rur="NAO\\05459910281066\\0541718344060:01f77ec9dddea911366c76e43ec99f35c54883325777ec2b4ee9190da7b06ad68a575594"; sessionid=59910281066%3ARTpXo4Qu7Uvvwo%3A17%3AAYcCNWGy7_6dFP_9FrpD3nI-gln8I8KZk-IzScX80Q; ds_user_id=59910281066; csrftoken=FiNRRKhMpxDBSdptzIwEJ1JAynmDsuW3',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
            # LogingCookies["sessionid"] = f"{UserId[0]}%3AMQcDnmOotqLl14%3A2%3AAYfmXNX_dZMYRPRGCAXItbhgYlQJMCLia_L5pxGrZw"
            response = requests.get(f'https://www.instagram.com/api/v1/media/{PostID}/likers/', cookies=LogingCookies, headers=headers)
            

            if ',"require_login":true,"status":"fail"}' in response.text and response.status_code != 200:
                print("Calling Again for Likes cookies")
                random_number = random.randrange(1,5) 
                time.sleep(random_number)
                res = self.login_insta(userpass["username"],userpass["password"])
                LogingCookies = res.cookies.get_dict()
                # self.GetLIkes(PostID,PostUrl,userpass,LogingCookies,UserId)


            json_data = response.json()
            LinksCount = json_data.get("users")
            if LinksCount:
                for links_count in LinksCount:
                    item = dict()
                    item["PostUrl"] = PostUrl
                    item["username"] = links_count.get("username") if links_count.get("username") else ""
                    item["pk_id"] = links_count.get("pk_id") if links_count.get("pk_id") else ""
                    item["pk"] = links_count.get("pk") if links_count.get("pk") else ""
                    item["full_name"] = links_count.get("full_name") if links_count.get("full_name") else ""
                    item["is_private"] = links_count.get("is_private") if links_count.get("is_private") else ""
                    item["is_verified"] = links_count.get("is_verified") if links_count.get("is_verified") else ""
                    item["profile_pic_id"] = links_count.get("profile_pic_id") if links_count.get("profile_pic_id") else ""
                    item["profile_pic_url"] = links_count.get("profile_pic_url") if links_count.get("profile_pic_url") else ""
                    Likes_.insert_one(item)
                    print("__LIKES_____ :- {}".format(ProfileName))

                    # print("*****__________*********")
                    # print(item)
                    # # GotLikes.append(item)
                    # print("*****__________*********")
        except Exception as e:
            logging.error("Error in Likes Function :- {}".format(e))
            pass




    def GetProfilePost(self,profile_name,LogingCookies,Profile_id_,options,userpass,UserId):
        try:
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            self.headers["Referer"] = self.profile_url.format(profile_name)
            profile_api = f"https://www.instagram.com/api/v1/feed/user/{profile_name}/username/?count=12"
            response = requests.get(profile_api,headers=self.headers,cookies=LogingCookies)
            if ',"require_login":true,"status":"fail"}' in response.text and response.status_code != 200:
                random_number = random.randrange(1,5) 
                time.sleep(random_number)
                res = self.login_insta(userpass["username"],userpass["password"])
                LogingCookies = res.cookies.get_dict()
                # self.GetCommentNextPage(self,cursor,profile_id,post_url,LogingCookies,userpass)
                self.GetProfilePost(profile_name,LogingCookies,Profile_id_,options,userpass,UserId)
            json_data = response.json()
            products = json_data.get("items")
            if products:
                blue_dot = json_data.get("user").get("is_verified")
                try:
                    for product in products:
                        item = dict()
                        try:
                            item["profile_url"] = self.profile_url.format(profile_name)
                        except Exception as e:
                            logging.error("Error in profile_url {}".format(e))
                        try:
                            item["Blue Dot"] = blue_dot
                            post_code = product.get("code")
                            item["Post_url"] = self.post_url.format(post_code) if post_code else ""
                        except Exception as e:
                            logging.error("Error in blue dot and post_url {}".format(e))
                        try:
                            post_id = product.get("id")
                            item["post_id"] = post_id if post_id else ""
                        except Exception as e:
                            logging.error("Error in post_id {}".format(e))
                        try:

                            if product.get("caption"):
                                item["post_text"] = product["caption"].get("user").get("full_name")
                            elif product.get("user"):
                                item["post_text"] = product.get("text")
                        except Exception as e:
                            print("Error in post_text {}".format(e))
                        try:
                            if product.get("caption"):
                                item["full_name"] = product["caption"].get("user").get("full_name")
                            elif product.get("user"):
                                item["full_name"] = product.get("user").get("full_name")

                        except Exception as e:
                            logging.error("Error in full_name :- {}".format(e))
                        try:
                            if product.get("caption"):
                                item["is_private"] = product["caption"].get("user").get("is_private")
                            elif product.get("user"):
                                item["is_private"] = product.get("user").get("is_private")
                        except Exception as e:
                            logging.error("Error in is_private :- {}".format(e))
                        try:
                            if product.get("carousel_media"):
                                image_url =product["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
                                item["image_url"] = image_url 
                            elif product.get("image_versions2"):
                                image_url = product["image_versions2"]["candidates"][0]["url"]
                                item["image_url"] = image_url   
                        except Exception as e:
                            logging.error("Error in image_url {}".format(e))
                        # print(item) 
                        try:
                            comment_count = product.get("comment_count")
                            item["Total_Comments"] = comment_count if comment_count else ""
                        except Exception as e:
                            logging.error("Error in total_comments {}".format(e))
                        try:
                            like_count = product.get("like_count")
                            item["Total_Likes"] = like_count if like_count else ""
                        except Exception as e:
                            logging.error("Error in total_links {}".format(e))
                        try:
                            video_link = product.get("video_versions")
                            item["Video Url"] = video_link[0].get("url") if video_link else ""
                        except Exception as e:
                            logging.error("Error in video_url :- {}".format(e))
                        item["Date"] = time.strftime("%Y-%d-%m")
                        item["Time"] = time.strftime("%H:%M:%S")
                        # print("*******___________*********")
                        # print(item)
                        # GotPost.append(item)
                        Posts.insert_one(item)
                        print("GetProfilePost Calling ! :- {}".format(profile_name))

                        # Get all Suggesssion. It is needs to be 1 for Getting suggesssion
                        if options["SuggessionScrape"] == 1:
                            logging.info("Is is calling SuggessionScrape ")
                            # GetData = self.GetHomePage(self.base_url.format(options["ProfileCode"]),LogingCookies)
                            api_url = "https://www.instagram.com/graphql/query/?query_hash=d4d88dc1500312af6f937f7b804c68c3&user_id={}&include_chaining=false&include_reel=true&include_suggested_users=false&include_logged_out_extras=false&include_live_status=false&include_highlight_reels=true".format(Profile_id_).replace('"',"")
                            api_url = api_url.replace('"',"")
                            self.GetSugessions(api_url,options["ProfileCode"],LogingCookies) # Getting Seggessions profiles from profiles 
                        
                        # Get all Likes. It needs to be 1 for Getting the likes
                        if options["GetLIkes"] == 1:
                            # GetLikesCookies = response.cookies.get_dict()
                            self.GetLIkes(item["post_id"].split("_")[0],item["Post_url"],userpass,LogingCookies,options["ProfileCode"])



                        # Get all comments. It needs to be 1 for Getting the Comments
                        # if options["CommentsScrape"] == 1:
                        #     self.GetCommentFirstPage(item["post_id"],item["Post_url"],LogingCookies,userpass)
                            # self.GetLIkes(item["post_id"].split("_")[0],LogingCookies,item["Post_url"])

                except Exception as e:
                    print("Error in products data :- {}".format(e))
                    pass
        except Exception as e:
            print("Error in list page function :- {}".format(e))
            pass




    def login_insta(self,username,password):
        try:
            login_url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
            ck = requests.get(login_url)
            crsf = ck.cookies['csrftoken']
            headers = {
                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
                'x-requested-with': 'XMLHttpRequest',
                'referer': 'https://www.instagram.com/accounts/login/',
                'sec-ch-ua-platform':'Linux',
                'x-csrftoken': crsf}
            time_ = int(datetime.now().timestamp())
            payload = {
                'username': username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_}:{password}',  # <-- note the '0' - that means we want to use plain passwords
                'queryParams': {},
                'optIntoOneTap': 'false'}
            # res = requests.post(login_url,data=payload,headers=headers,proxies=proxieslt)
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            res = requests.post(login_url,data=payload,headers=headers)

            print(res)

            print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            return res
        except Exception as e:
            logging.error(f"Error in login_insta function :- {e}")

    def GetHomePage(self,url,LogingCookies):
        try:
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            response = requests.get(url, cookies=LogingCookies, headers=headers)
            return response
            # CodeID = re.findall('"user\_id"\:"(.*?),',response.text)
            # return CodeID[0]
        except Exception as e:
            logging.error(f"Error in GetHomePage function :- {e}")
            pass





    def GetSugessions(self,url,username_,LogingCookies):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-CSRFToken': "w7OkPIUN5MxUIm9AVdvlWI9XlmvoSuZn",
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
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            response = requests.get(url, cookies=LogingCookies, headers=headers)
            json_data = response.json()
            Edges = json_data["data"]["user"]["edge_chaining"]["edges"]
            for edge in Edges:
                item = dict()
                try:
                    username = edge["node"]["username"]
                except Exception as e:
                    logging.error(f"Error in username :- {e}")
                try:
                    full_name = edge["node"]["full_name"]
                except Exception as e:
                    logging.error(f"Error in full_name {e}")
                try:
                    is_private = edge["node"]["is_private"]
                except Exception as e:
                    logging.error(f"Error in is_private :- {e}")
                try:
                    is_verified = edge["node"]["is_verified"]
                except Exception as e:
                    logging.error(f"Error in is_varified :- {e}")
                try:
                    profile_pic_url = edge["node"]["profile_pic_url"]
                except Exception as e:
                    logging.error(f"Error in profile_pic_url :- {e}")
                profile_url = f"https://www.instagram.com/{username}/"
                item["username"] = username
                item["full_name"] = full_name
                item["is_private"] = is_private
                item["is_verified"] = is_verified
                item["profile_pic_url"] = profile_pic_url
                item["profile_url"] = profile_url
                # print(item)
                # GotSuggession.append(item)
                Suggessions.insert_one(item)
                print("GetSugessions Calling ! :- {}".format(username_))
        except Exception as e:
            logging.error("Error in GetSugessions Functions :- {}".format(e))




    def StartProcess(self,ProfileCode_):  
        try:  
            for userpass in self.user_pass:
                res = self.login_insta(userpass["username"],userpass["password"])
                LogingCookies = res.cookies.get_dict()
                for _len in range(len(ProfileCode_)):
                    PrData = ProfileCode_[_len]
                    if PrData["ProfileScrape"] == 1:
                        GetDataResponse = self.GetHomePage(self.base_url.format(PrData["ProfileCode"]),LogingCookies)
                        Profile_id_ = re.findall(',"profile_id":"(.*?)",',GetDataResponse.text)
                        UserId = re.findall('\,"identity"\:\{"appScopedIdentity"\:"(.*?)",',GetDataResponse.text)
                        self.GetProfilePost(PrData["ProfileCode"],LogingCookies,Profile_id_[0],PrData,userpass,UserId)
                        ProfileCode = PrData["ProfileCode"]
                        self.GetReels(Profile_id_,ProfileCode)
                    else:
                        print("It is already is scrap so SKIP IT NOW :- {}".format(PrData["ProfileCode"]))
                    
        except Exception as e:
            logging.error("Error in StartProcess Function :- {}".format(e))
            pass





# _Prfofile_urls = ["https://www.instagram.com/p/CkvgGBHtpBg/","rezzaut","gojooosatoru259","everything_my_bro","sisodiya___jyoti","mo_hini_8145","girija_partap_0007"]

# _Prfofile_urls = [{"ProfileCode":"emmawatson","ProfileScrape":1,"SuggessionScrape":1,"CommentsScrape":1,"GetLIkes":1,"GetReels":1}]

_Prfofile_urls = [{"ProfileCode":"khaby00","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":" ","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"lelepons","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"chiaraferragni","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"sommerray","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"camerondallas","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"zachking","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"amandacerny","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},
                  {"ProfileCode":"mrbeast","ProfileScrape":1,"SuggessionScrape":1,"GetLIkes":1,"GetReels":1},]



# Creating Objects for Class and calling the function For starting the PROGRAM
obj = GetAllSuggessions()
obj.StartProcess(_Prfofile_urls)



















# Data is fetching from xlsx file for Fetching Posts, likes, seggessions, reels, And this is for Dynamic profiles
# df = pd.read_excel("Likes_data_profiles.xlsx")
# profile_data = []
# for i in range(10):
#     _Prfofile_urls = df.iloc[i].to_dict()
#     profile_data.append(_Prfofile_urls)

# obj.StartProcess(profile_data)

           
            
