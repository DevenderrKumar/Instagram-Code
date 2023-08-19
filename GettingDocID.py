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
import re





# class GetDocumentID:

def GetDocID():
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Referer': 'https://www.instagram.com/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        '_nc_x': 'Ij3Wp8lg5Kz',
    }

    response = requests.get(
        'https://static.cdninstagram.com/rsrc.php/v3igsz4/yr/l/en_GB/q8xxLptjPhX.js',
        params=params,
        headers=headers,
    )
    if re.findall('\{alias\:null\,args\:null\,kind\:"ScalarField"\,name\:"caption_is_edited"\,storageKey\:null\}\,T\]\,storageKey\:null\}\]\,storageKey\:null\}\]\}\,params\:\{id\:"(.*?)"\,metadata\:',response.text):
        doc_id = re.findall('\{alias\:null\,args\:null\,kind\:"ScalarField"\,name\:"caption_is_edited"\,storageKey\:null\}\,T\]\,storageKey\:null\}\]\,storageKey\:null\}\]\}\,params\:\{id\:"(.*?)"\,metadata\:',response.text)
        return doc_id



    


#     def crawling_profile_info(product_id,profile_url,Post_url):
#     try:
#         item = dict()
#         headers["Referer"] = Post_url
#         response = requests.get(profile_info_url.format(product_id.split("_")[0]),headers=new_headers)
#         if response.status_code == 401:
#             print("Got 401 response So Sleep for 1-10 secends range....")
#             time.sleep(random.randrange(1,5))
#             new_headers["Referer"] = post_url
#             response = requests.get(profile_info_url.format(product_id.split("_")[0]),headers=new_headers)            
#         js = response.json()
#         item["Profile Url"] = profile_url
#         like_count = js["items"][0].get("like_count")
#         item["like_count"] = like_count if like_count else ""
#         post_image_url = js["items"][0]
#         if post_image_url.get("carousel_media"):
#             image_url =post_image_url["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
#             item["image_url"] = image_url 
#         elif post_image_url.get("image_versions2"):
#             image_url = post_image_url["image_versions2"]["candidates"][0]["url"]
#             item["image_url"] = image_url        
#         code = js["items"][0].get("code")
#         item["post_url"] = Post_url
#         is_video = js["items"][0].get("video_versions")
#         item["video_url"] = is_video[0].get("url") if is_video else ""
#         item["is_video"] = True if is_video else False
#         play_count = js["items"][0].get("play_count")
#         item["play_count"] = play_count if play_count else ""
#         data2.append(item)
#     except Exception as e:
#         print("Error in Profile_data :- {}".format(e))
#         pass



# def crawling_commits(cursor,profile_id,post_url,data):
#     global flag
#     while flag:
#         try:
#             params["min_id"] = cursor
#             random_time = random.randrange(1,8)
#             time.sleep(random_time)
#             headers["Referer"] = post_url
#             response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=params, cookies=comments_cookies,headers=comments_headers)
            
#             if response.status_code == 401:
#                 print("Got 401 response So Sleep for 1-5 secends range....")
#                 time.sleep(random.randrange(1,5))
#                 new_headers["Referer"] = post_url
#                 response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=params, cookies=comments_cookies,headers=comments_headers)            
          
#             js = response.json()
#             comments = js.get("comments")
#             next_cursor = js.get("next_min_id")
#             for comment in comments:
#                 item = dict()
#                 item["profile_url"] = profile_url.format(js["caption"]["user"]["username"])
#                 item["post_image"] = data.get("image_url")
#                 item["post_comments"] = data.get("Total_Comments")
#                 item["post_like"] = data.get("Total_Likes")
#                 item["Is_video"] = data.get("Video Url")
#                 item["Is_blue_dot"] = data.get("Blue Dot")
#                 item["is_private"] = data.get("is_private")
#                 item["Post_title"] = data.get("post_text")
#                 item["full_name"] = data.get("full_name")
#                 item["post_id"] = data.get("post_id") 
#                 item["post_url"] = post_url
#                 commit_text  = comment.get("text")
#                 item["commit_text"] = commit_text if commit_text else ""
#                 pk_id = comment.get("pk")
#                 item["pk_id"] = pk_id if pk_id else ""
#                 comment_count = js.get("comment_count")
#                 item["comment_count"] = comment_count if comment_count else ""
#                 user_id = comment.get("user_id")
#                 item["user_id"] = user_id if user_id else ""
#                 status = comment.get("status")
#                 item["status"] = status if status else ""
#                 username = comment["user"].get("username")
#                 item["comment_Profile_url"] = profile_url.format(username) if username else ""
#                 item["comment_by_username"] = username if username else ""
#                 is_verified = comment["user"].get("is_verified")
#                 item["is_verified"] = is_verified if is_verified else False
#                 # is_private = comment["user"].get("is_private")
#                 # item["is_private"] = is_private if is_private else False
#                 comment_on_username = js["caption"]["user"].get("full_name")
#                 item["comment_on_username"] = comment_on_username if comment_on_username else ""
#                 item["Date"] = time.strftime("%Y-%d-%m")
#                 item["Time"] = time.strftime("%H:%M:%S")
#                 mycol.insert_one(item)
#                 print(item)
#                 print("Inserting to DB......")
#                 # data1.append(item)
#             if next_cursor:
#                 print("Next Cursor :- {}".format(next_cursor))
#                 cursor = next_cursor
#             else:
#                 flag = False
#         except Exception as e:
#             print("Error in crawling_commits function :- {}".format(e))
#             print("sleeping for 10")
#             time.sleep(10)
#             continue



# def crawling_first_page_comments(self,product_id,post_url,data):
#     try:
#         if data.get("post_id") not in posts_ids_scraped:
#             posts_ids_scraped.append(data.get("post_id"))
#             random_time = random.randrange(1,5)
#             time.sleep(random_time)
#             params = {'can_support_threading': 'true','permalink_enabled': 'false',}
#             self.headers["Referer"] = post_url

#             response = requests.get(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', params=params, headers=new_headers)
            
#             if response.status_code == 401:
#                 print("Got 401 response So Sleep for 1-10 secends range....")
#                 time.sleep(random.randrange(1,10))
#                 response = requests.get(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', params=params, headers=new_headers)
            
#             js = response.json()
#             comments = js.get("comments")
#             next_cursor = js.get("next_min_id")
#             for comment in comments:
#                 item = dict()
#                 item["profile_url"] = profile_url.format(js["caption"]["user"]["username"])
#                 item["post_image"] = data.get("image_url")
#                 item["post_comments"] = data.get("Total_Comments")
#                 item["post_like"] = data.get("Total_Likes")
#                 item["Is_video"] = data.get("Video Url")
#                 item["Is_blue_dot"] = data.get("Blue Dot")
#                 item["is_private"] = data.get("is_private")
#                 item["Post_title"] = data.get("post_text")
#                 item["full_name"] = data.get("full_name")
#                 item["post_id"] = data.get("post_id") 
#                 item["post_url"] = post_url
#                 commit_text  = comment.get("text")
#                 item["commit_text"] = commit_text if commit_text else ""
#                 pk_id = comment.get("pk")
#                 item["pk_id"] = pk_id if pk_id else ""
#                 comment_count = js.get("comment_count")
#                 item["comment_count"] = comment_count if comment_count else ""
#                 user_id = comment.get("user_id")
#                 item["user_id"] = user_id if user_id else ""
#                 status = comment.get("status")
#                 item["status"] = status if status else ""
#                 username = comment["user"].get("username")
#                 item["comment_Profile_url"] = profile_url.format(username) if username else ""
#                 item["comment_by_username"] = username if username else ""
#                 is_verified = comment["user"].get("is_verified")
#                 item["is_verified"] = is_verified if is_verified else False
#                 is_private = comment["user"].get("is_private")
#                 item["is_private"] = is_private if is_private else False
#                 comment_on_username = js["caption"]["user"].get("full_name")
#                 item["comment_on_username"] = comment_on_username if comment_on_username else ""
#                 item["Date"] = time.strftime("%Y-%d-%m")
#                 item["Time"] = time.strftime("%H:%M:%S")
#                 mycol.insert_one(item)
#                 print(item)
#                 print("Inserting to DB......")
#                 # data1.append(item)
#             if next_cursor:
#                 print("Next Cursor Sending to crawling_first_page_comments function :- {}".format(next_cursor))
#                 time.sleep(10)
#                 crawling_commits(next_cursor,product_id,post_url,data)
#             else:
#                 print("Not found the next page cursor")
#     except Exception as e:
#         print("Error in crawling_first_page_comments :- {}".format(e))





# # Taking data from input file and getting data
# # f = open("input_data.json","r").read()
# # input_data = json.loads(f)




# # Creating DataBase connection and fetching data from DB
# fetch_data_from_database = []
# print("Creating Connection for DB and fetching data")
# client = Create_Database_connect_with_data()
# time.sleep(2)
# mydb = client["instagram"]
# collection = mydb["instagram_profiles_POST_Virat_Kholi"]
# collection_data = collection.find({"full_name":"Virat Kohli"})
# for data in collection_data:
#     fetch_data_from_database.append(data)
#     # posts_ids.append(data.get("post_id"))


# mydb = client["instagram"]
# mycol = mydb["instagram_POST_Comments_Virat_Kohli"]

# print("fetching data for {} now..... AND Total post are {}.......".format(fetch_data_from_database[0].get("full_name"),len(fetch_data_from_database)))
# # Two function for fetching comments and details for every post... 
# for in_data in fetch_data_from_database[0:10]:
#     post_id = in_data["post_id"]
#     post_url = in_data["Post_url"]
#     crawling_first_page_comments(post_id,post_url,in_data)

















































































































# For Batter Output you should apply csrf token in headers for not blocking easily
# def GetCommentNextPage(self,cursor,profile_id,post_url,LogingCookies,userpass):
#     global flag
#     while flag:
#         try:
#             self.NextParams["min_id"] = cursor
#             random_time = random.randrange(1,8)
#             print("Requesting for Next page function for Comments ....")
#             time.sleep(random_time)
#             headers["Referer"] = post_url
#             response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=self.NextParams, cookies=LogingCookies,headers=self.comments_headers)
#             if response.status_code == 401:
#                 print("Got 401 response So Sleep for 1-5 secends range....")
#                 time.sleep(random.randrange(1,5))
#                 self.new_headers["Referer"] = post_url
#                 response = requests.get(f'https://www.instagram.com/api/v1/media/{profile_id}/comments/', params=self.NextParams, cookies=LogingCookies,headers=self.new_headers)       
#             if ',"require_login":true,"status":"fail"}' in response.text and response.status_code != 200:
#                 res = self.login_insta(userpass["username"],userpass["password"])
#                 LogingCookies = res.cookies.get_dict()
#                 self.GetCommentNextPage(self,cursor,profile_id,post_url,LogingCookies,userpass)

#             js = response.json()
#             comments = js.get("comments")
#             next_cursor = js.get("next_min_id")
#             print(post_url)
#             print("Number of comments For GetCommentNextPage is :- {}".format(len(comments)))
#             for comment in comments:
#                 item = dict()
#                 item["profile_url"] = self.profile_url.format(js["caption"]["user"]["username"])
#                 item["post_url"] = post_url
#                 commit_text  = comment.get("text")
#                 item["commit_text"] = commit_text if commit_text else ""
#                 pk_id = comment.get("pk")
#                 item["pk_id"] = pk_id if pk_id else ""
#                 comment_count = js.get("comment_count")
#                 item["comment_count"] = comment_count if comment_count else ""
#                 user_id = comment.get("user_id")
#                 item["user_id"] = user_id if user_id else ""
#                 status = comment.get("status")
#                 item["status"] = status if status else ""
#                 username = comment["user"].get("username")
#                 item["comment_Profile_url"] = self.profile_url.format(username) if username else ""
#                 item["comment_by_username"] = username if username else ""
#                 is_verified = comment["user"].get("is_verified")
#                 item["is_verified"] = is_verified if is_verified else False
#                 comment_on_username = js["caption"]["user"].get("full_name")
#                 item["comment_on_username"] = comment_on_username if comment_on_username else ""
#                 item["Date"] = time.strftime("%Y-%d-%m")
#                 item["Time"] = time.strftime("%H:%M:%S")
#                 # print(item)
#                 GotComments.append(item)
#                 print("Fetching Data for Comments for Next Pages .....")
#             if next_cursor:
#                 print("Next Cursor :- {}".format(next_cursor))
#                 flag = True
#                 cursor = next_cursor
#             else:
#                 flag = False
#         except Exception as e:
#             print("Error in GetCommentNextPage function :- {}".format(e))
#             print("sleeping for 10")
#             time.sleep(10)
#             continue


# # For Batter Output you should apply csrf token in headers for not blocking easily
# def GetCommentFirstPage(self,product_id,post_url,LogingCookies,userpass):
#     global flag
#     try:
#         random_time = random.randrange(1,5)
#         time.sleep(random_time)
#         params = {'can_support_threading': 'true','permalink_enabled': 'false',}
#         self.comments_headers["Referer"] = post_url
#         response = requests.get(f'https://www.instagram.com/api/v1/media/{product_id}/comments/', params=params, headers=self.comments_headers,cookies=LogingCookies)
#         js = response.json()
#         comments = js.get("comments")
#         next_cursor = js.get("next_min_id")
#         print(post_url)
#         print("Number of comments is :- {}".format(len(comments)))
#         for comment in comments:
#             item = dict()
#             item["post_url"] = post_url
#             commit_text  = comment.get("text")
#             item["commit_text"] = commit_text if commit_text else ""
#             pk_id = comment.get("pk")
#             item["pk_id"] = pk_id if pk_id else ""
#             comment_count = js.get("comment_count")
#             item["comment_count"] = comment_count if comment_count else ""
#             user_id = comment.get("user_id")
#             item["user_id"] = user_id if user_id else ""
#             status = comment.get("status")
#             item["status"] = status if status else ""
#             username = comment["user"].get("username")
#             item["comment_Profile_url"] = self.profile_url.format(username) if username else ""
#             item["comment_by_username"] = username if username else ""
#             is_verified = comment["user"].get("is_verified")
#             item["is_verified"] = is_verified if is_verified else False
#             is_private = comment["user"].get("is_private")
#             item["is_private"] = is_private if is_private else False
#             comment_on_username = js["caption"]["user"].get("full_name")
#             item["comment_on_username"] = comment_on_username if comment_on_username else ""
#             item["Date"] = time.strftime("%Y-%d-%m")
#             item["Time"] = time.strftime("%H:%M:%S")
#             # print(item)
#             GotComments.append(item)

#         if next_cursor:
#             print("Next Cursor Sending to crawling_commits function :- {}".format(next_cursor))
#             time.sleep(10)
#             flag = True
#             self.GetCommentNextPage(next_cursor,product_id,post_url,LogingCookies,userpass)
#         else:
#             print("Not found the next page cursor")
#     except Exception as e:
#         print("Error in crawling_first_page_comments :- {}".format(e))