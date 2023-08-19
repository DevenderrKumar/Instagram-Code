from requests import Session
import requests
from lxml import html
import pandas as pd
import time
# from pymongo import MongoClient
import random
from datetime import datetime
import json
import re
import pymongo
import logging


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
 'Accept': '*/*',
 'Accept-Language': 'en-US,en;q=0.5',
 'Content-Type': 'application/x-www-form-urlencoded',
 'X-FB-Friendly-Name': 'PolarisPostCommentsPaginationQuery',
 'X-CSRFToken': 'Va85aED8CMoupgfWEViUiPZRPNowB8CO',
 'X-IG-App-ID': '936619743392459',
 'X-FB-LSD': '8b225Ry5ilHMod-7wxZbey',
 'X-ASBD-ID': '129477',
 'Origin': 'https://www.instagram.com',
 'Connection': 'keep-alive',
 'Referer': 'https://www.instagram.com/p/CCIcO6khRE3/',
 'Sec-Fetch-Dest': 'empty',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Site': 'same-origin',
 'Pragma': 'no-cache',
 'Cache-Control': 'no-cache'}


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["ViralPitch_Intagram_Scraper"]
GetCommentsAll = mydb["Intagram_Post_Comments"]

# TheLoginCookies = ""

# mydb_check = client["ViralPitch_Intagram_Scraper"]
# GetCommentsAll_check = mydb["Intagram_Post_Comments"]


class Getcomments:

    def __init__(self):
        self.base_url = "https://www.instagram.com/{}"
        self.TheLoginCookies = ""
        self.PostApiUrl = "https://www.instagram.com/api/v1/clips/user/"
        self.FirstData = {'include_feed_video': 'true','page_size': '12','target_user_id': '173560420'}
        self.NextParams = {'can_support_threading': 'true','min_id': '{"cached_comments_cursor": "17981506852884848", "bifilter_token": "KHkAgXZAYGzlPwAikDiHS3w_AGKcowkqxj8AxHAfbU3JPwBGnnieXBVBAOhTDfMlzz8A12b9tQeMPwALlfiPnMY_AG53PWgqhT8ArreKnSjVPwAx7KwrAsc_ANMnck3v_D8A9QkzLsnBQABXEnc3RpI_ALlE5FS-3z8AAA=="}'}
        self.post_url = "https://www.instagram.com/p/{}/"
        self.profile_url = "https://www.instagram.com/{}/"
        self.user_pass = [{'username':'pranavchikra','password':'Ajeet@123'},
                            {'username':'amirkhn91227','password':'Ajeet@123'},
                            {'username':'sayisid176','password':'Ajeet@123'},
                            {'username':'smritinayir','password':'Ajeet@123'},
                            {'username':'waldiyababita','password':'Ajeet@123'},
                            {'username':'wopajos544','password':'Ajeet@123'},
                            {'username':'shreadharry','password':'Ajeet@123'},
                            {'username':'deshwalsamira','password':'Ajeet@123'},
                            {"username":"modata1398","password":"Ajeet@123"},
                            {"username":"migado5632","password":"Ajeet@123"},
                            {"username":"lebih34093","password":"Ajeet@123"},
                            {"username":"momam43895","password":"Ajeet@123"},
                            {"username":"tikamo3778","password":"Ajeet@123"},
                            {"username":"cibana8004","password":"Ajeet@123"},
                            {'username':'ajeetkumar2oiiop','password':'Ajeet@10'},
                            {'username':'devender85068202522023','password':'Dev@1234'}]
        self.headers = headers


    def Create_Database_connect_with_data(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        return client


    def GetNextComments(self,cursor,profile_id,post_url,LogingCookies,user_name,pass_word):
        global flag
        while flag:
            try:
                self.NextParams["min_id"] = cursor
                self.headers["Referer"] = post_url
                print("Sleeping for seconds... ")
                time.sleep(random.randint(1,4))
                response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=self.NextParams, cookies=LogingCookies,headers=self.headers)
                print("For GetNextComments Function Username :- {} And Password :- {}".format(user_name,pass_word))
                if response.status_code != 200:
                    try:
                        RandomNumber = random.randint(0,self.user_pass.__len__()-1)
                        user_name = self.user_pass[RandomNumber]["username"]
                        pass_word = self.user_pass[RandomNumber]["password"]
                    except Exception as e:
                        print("Error in RandomNumber and username/password :- {}".format(e))
                    print(f"Got {response.status_code} Resposne So waiting for some seconds and requests again... ")
                    print("for GetNextComments_ Username :- {} \nPassword :- {}".format(user_name,pass_word))
                    time.sleep(random.randint(1,5))
                    res = self.login_insta(user_name,pass_word)
                    LogingCookies = res.cookies.get_dict()
                
                
                GetConnection = self.Create_Database_connect_with_data()
                mydb = GetConnection["ViralPitch_Intagram_Scraper"]
                collection = mydb["Intagram_Post_Comments"]
                js = response.json()
                comments = js.get("comments")
                next_cursor = js.get("next_min_id")
                print("Post id is :- {}".format(profile_id))
                for comment in comments:
                    pk_id = comment.get("pk")
                    if not collection.find_one({"pk_id":"{}".format(pk_id)}) and pk_id:
                        item = dict()
                        item["pk_id"] = pk_id if pk_id else ""
                        item["post_url"] = post_url
                        item["profile_url"] = self.profile_url.format(js["caption"]["user"]["username"])
                        commit_text  = comment.get("text")
                        item["commit_text"] = commit_text if commit_text else ""
                        comment_count = js.get("comment_count")
                        item["comment_count"] = comment_count if comment_count else ""
                        user_id = comment.get("user_id")
                        item["user_id"] = user_id if user_id else ""
                        status = comment.get("status")
                        item["status"] = status if status else ""
                        username = comment["user"].get("username")
                        item["comment_Profile_url"] = self.profile_url.format(username) if username else ""
                        item["comment_by_username"] = username if username else ""
                        is_verified = comment["user"].get("is_verified")
                        item["is_verified"] = is_verified if is_verified else False
                        comment_on_username = js["caption"]["user"].get("full_name")
                        item["comment_on_username"] = comment_on_username if comment_on_username else ""
                        item["Date"] = time.strftime("%Y-%d-%m")
                        item["Time"] = time.strftime("%H:%M:%S")
                        # print(item)
                        GetCommentsAll.insert_one(item)
                        print("Next Page comments Inserting to DB......")
                    else:
                        print("This PK is is exsit for NextComments in comments DB...")
                        print("PK_id :- {}".format(pk_id))

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



    def GetComments(self,product_id,post_url,LogingCookies,user_name,pass_word):
        global flag
        try:
            random_time = random.randrange(1,5)
            time.sleep(random_time)
            params = {'can_support_threading': 'true','permalink_enabled': 'false'}
            self.headers["Referer"] = post_url
            self.headers["X-CSRFToken"] = LogingCookies["csrftoken"]
            response = requests.post(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', cookies=LogingCookies, headers=self.headers, data=params)
            print("For GetComments Function Username :- {} And Password :- {}".format(user_name,pass_word))
            GetConnection = self.Create_Database_connect_with_data()
            mydb = GetConnection["ViralPitch_Intagram_Scraper"]
            collection = mydb["Intagram_Post_Comments"]
            if response.status_code != 200:
                flag = True
                while flag:
                    print("Comming into the While Loop")
                    try:
                        RandomNumber = random.randint(0,self.user_pass.__len__()-1)
                        user_name = self.user_pass[RandomNumber]["username"]
                        pass_word = self.user_pass[RandomNumber]["password"]
                    except Exception as e:
                        print("Error in RandomNumber and username/password :- {}".format(e))
                    print(f"Got {response.status_code} Resposne So waiting for some seconds and requests again... ")
                    print("for GetComments_ Username :- {} \nPassword :- {}".format(user_name,pass_word))
                    time.sleep(random.randint(1,5))
                    res = self.login_insta(user_name,pass_word)
                    LogingCookies = res.cookies.get_dict()
                    random_time = random.randrange(1,5)
                    time.sleep(random_time)
                    params = {'can_support_threading': 'true','permalink_enabled': 'false'}
                    self.headers["Referer"] = post_url
                    self.headers["X-CSRFToken"] = LogingCookies["csrftoken"]
                    response = requests.post(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', cookies=LogingCookies, headers=self.headers, data=params)
                    if response.status_code == 200:
                        flag = False
                        print("Got 200 resposne Flag is False now So Leaving out of the while Loop")

            js = response.json()
            comments = js.get("comments")
            next_cursor = js.get("next_min_id")
            for comment in comments:
                item = dict()
                pk_id = comment.get("pk")
                if not collection.find_one({"pk_id":"{}".format(pk_id)}) and pk_id:
                    try:
                        item["pk_id"] = pk_id if pk_id else ""
                        item["post_url"] = post_url
                    except Exception as e:
                        print("Error in post_url :- {}".format(e))
                    try:
                        commit_text  = comment.get("text")
                        item["commit_text"] = commit_text if commit_text else ""
                    except Exception as e:
                        print("Error in commit_text :- {}".format(e))
                    try:
                        comment_count = js.get("comment_count")
                        item["comment_count"] = comment_count if comment_count else ""
                    except Exception as e:
                        print("Error in comment_count :- {}".format(e))
                    try:
                        user_id = comment.get("user_id")
                        item["user_id"] = user_id if user_id else ""
                    except Exception as e:
                        print("Error in user_id :- {}".format(e))
                    try:
                        status = comment.get("status")
                        item["status"] = status if status else ""
                    except Exception as e:
                        print("Error in status :- {}".format(e))
                    try:
                        username = comment["user"].get("username")
                        item["comment_Profile_url"] = self.profile_url.format(username) if username else ""
                        item["comment_by_username"] = username if username else ""
                    except Exception as e:
                        print("Error in comment_Profile_url :- {}".format(e))
                    try:
                        is_verified = comment["user"].get("is_verified")
                        item["is_verified"] = is_verified if is_verified else False
                    except Exception as e:
                        print("Error in is_verified :- {}".format(e))
                    try:
                        is_private = comment["user"].get("is_private")
                        item["is_private"] = is_private if is_private else False
                    except Exception as e:
                        print("Error in is_private :- {}".format(e))
                    try:
                        comment_on_username = js["caption"]
                        item["comment_on_username"] = comment_on_username.get("user").get("full_name") if comment_on_username else ""
                    except Exception as e:
                        print("Error in comment_on_username :- {}".format(e))
                    item["Date"] = time.strftime("%Y-%d-%m")
                    item["Time"] = time.strftime("%H:%M:%S")
                    # print(item)
                    GetCommentsAll.insert_one(item)
                    print("Inserting to DB......")
                else:
                    print("This PK is is exsit in comments DB...")
                    print("PK_id :- {}".format(pk_id))
            if next_cursor:
                flag = True
                print("Next Cursor Sending to crawling_first_page_comments function :- {}".format(next_cursor))
                time.sleep(random.randint(1,10))
                self.GetNextComments(next_cursor,product_id,post_url,LogingCookies,user_name,pass_word)
            else:
                print("Not found the next page cursor")
        except Exception as e:
            print("Error in crawling_first_page_comments :- {}".format(e))


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

    def StartProcess(self,posts):
        try:  
            try:
                RandomNumber = random.randint(0,self.user_pass.__len__()-1)
                user_name = self.user_pass[RandomNumber]["username"]
                pass_word = self.user_pass[RandomNumber]["password"]
            except Exception as e:
                print("Error in RandomNumber and username/password :- {}".format(e))

            res = self.login_insta(user_name,pass_word)
            LogingCookies = res.cookies.get_dict()
            self.TheLoginCookies = LogingCookies
            for PostDetail in posts:
                self.GetComments(PostDetail["post_id"].split("_")[0],PostDetail["Post_url"],self.TheLoginCookies,user_name,pass_word)

        except Exception as e:
            logging.error("Error in StartProcess Function :- {}".format(e))
            pass

obj = Getcomments()

client = pymongo.MongoClient("mongodb://localhost:27017/")
time.sleep(2)
mydb = client["ViralPitch_Intagram_Scraper"]
collection = mydb["Intagram_Post_new"]
collection_data = collection.find({"full_name":"Dwayne Johnson"})
fetch_data_from_database = list()
# Put the [start:end] in collection_data, Like collection_data[start:end] It will start form there
for data in collection_data:
    fetch_data_from_database.append(data)


# fetch_data_from_database()

# posts_ = [{"post_id":"3138123481568124192","Post_url":"https://www.instagram.com/p/CuM2q4ULh0g/"},
#           {"post_id":"3130253703546296717","Post_url":"https://www.instagram.com/p/Ctw5SiYulmN/"},
#           {"post_id":"3115740937514993038","Post_url":"https://www.instagram.com/p/Cs9Vd_wuUWO/"},
#           {"post_id":"3112094054727601610","Post_url":"https://www.instagram.com/p/CswYQ3fpM3K/"}]

posts_ = [{"post_id":"3115740937514993038","Post_url":"https://www.instagram.com/p/Cs9Vd_wuUWO/"},
          {"post_id":"3112094054727601610","Post_url":"https://www.instagram.com/p/CswYQ3fpM3K/"}]

obj.StartProcess(posts_)









