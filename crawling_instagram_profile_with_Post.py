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
import GetLocationPost

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["instagram_ViralPitch"]
logs_collection = mydb["instagram_logs_ViralPitch"]
mycol = mydb["instagram_profiles_POST_ViralPitch"]


# url = "https://www.instagram.com/api/v1/feed/user/173560420/?count=12&max_id={}"

next_page_url = "https://www.instagram.com/api/v1/feed/user/{}/?count=12&max_id={}"
first_page_api_url = "https://www.instagram.com/api/v1/feed/user/ellyseperry/{}/?count=12"
post_url = "https://www.instagram.com/p/{}/"
profile_url = "https://www.instagram.com/{}/"

data = []

flag = True
pages = 10

new_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm82vM',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/virat.kohli/',
    'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="PRN\\05456853077686\\0541706397854:01f72426c9b79a2ca3b27ccb076cc4abacd6021f051e1cd26e2ab405d88e9838de77fcc4"; fbsr_124024574287414=I_GwUcYTNrOhN8dYq5O2mmPMmaOL-pmJ2139uJqm2j8.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQ2VQRTlFc1dDYXN5NVFfMnpuSEF5M00tWVBTZHE5QU9mTlNCenp4WGxrWGlRclpLLXdMSkV4U2RRYldyQTNSczZiWW8taldqUVh3XzUxbWNaN1lvT1JmOGNudjdFRGI5OTM5TndiWXEzM2xsZG9Sa1NrdS13MWVVTGJKdXpFeWlKM3VhRW1ZcV9hbk14cDREcGtBd1NkZ0l5N3JyZjNOUGNFeGN3ckozaXdYVTRrZ0NzZUI0X3pKbDMtVk1MdE9LME1xS25VaDJKeEE2Z21JMzBfSGZyaGRMeVpBQjc0YndJMFV5eUg3c3dkdE5xWFdwYlZWbkJlZW5OOU84QXo0aDdLVkRRZ295RmNwMVBkSWV2WkV0QWNBR2N3YmRmOUdsMDI1dUtXVl9kVnNPUy1VcFJWN1ozQjRrTFROM3hYSi1CRU0yUkRZcm5iai1iS3BMRVowWHZ0MDFDdDB2U3J4cEc0Wk9xNWkzMV9JdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFLOTVuTVFUeXRhRTRrbGVJdEx4bEhKZEpnd1R2UmRLblJteFFSc2ZJWWZRNm04NFlZRlhPb1IxN3lubzNhYlpBRUZTbnlwYVBmekdld0hLdVZ6Z2hyT3NhRXJCYVJyaEJ4bzVVYVM2YnRQT3p0QllRZWdubmNPOTRQd0V6N3QxSVpBYkN2eU1YZ09Cb045NWNPbXJ4N25IWWhOWkM0c2R3aDBvYU9qUXJpWkMyT3dzQTFnWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDg2MTY5Nn0; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYcpRlthQHl1Nd4Edrblr64YH7zQlHaYamaUMPoBlg; shbid="18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"; shbts="1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"; fbsr_124024574287414=1e18iRUvKCV5bPC6dCZHFpePQvctEEBWHN0LYszhfYg.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQ0dYWGdzOTRrMU9nc05seUREYkdONDZXcEdxMGM3UEszNEF0WEpqUjl2S2hLSWlVS25GT1QyaGZvSk5hY0lUNzVfVm8weURnc1RuZTdCOFhidmRtSW9BR1FvVGpHYURWSFRfMXBYX3J3U3laaDVQeXJSM1YyOTllUjhYekFNQ243cWQ0YVh1ZFhSY1RQT2dOQ2d2UXRrYS13QkVYRHZ2Uk9nRVRBN09wUWg1MFdPb3lVVWhOeTVuY0xhU1Rsbi15TDJSdmRpUkZjTm5QNlRsQ01KT2FuMEZ4ajJ4REFYN3p0TnBDbmdvN29kSWY5aU9NbkJiOFRhQXJDR2pHZElSVHRRU183d1oxTkhyMDBZWEgyd3Z4TzktazBOZnBaZWoxRjVpV3c3MXJreXNTTXZVa2Z0eE0xd3MxTVFkZ0hlYUpJTTBOWG5QZjVsSkFXMDRxRkpjUi1fbV9qMnFSRjNCWGE4emU3WUxxX1JTdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFLNTkyZjFOZGdBc1BSU2lRWEZxWFRPYm1kaXVDRGdJSjB5OVNBbmtYOHh1V3kzMzRKVUtSczJCMjBpdU5UN3FiT3NGaVQzcVR4ZDFCcnIxb2xNeVRMa0c0bEVnWkFKZmtLbzV4VGVaQ1pDWVJBN1REVGNRaE9yTU9POHNuU1pCTE92NlNMVFVITmJUdkZKM2VhZUt4Mk5BZnZONXhOQkpSMDJBUVJaQ09GSXlFcElzaWtuc1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzQ4NjE1MjV9',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'csrftoken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'ds_user_id': '56853077686',
    'sessionid': '56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdc7g5hKBR4BRpIezln9RoCO0PpKjMWTj3VzG-8-FM',
    'shbid': '"18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"',
    'shbts': '"1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"',
    'rur': '"PRN\\05456853077686\\0541718092632:01f7b9945e5eeb60439cb72388f111bc7a21d7b24f0f5a6ad08ab2dd94c6111136fb3b89"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm82-C',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/tntsportsbr/',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdc7g5hKBR4BRpIezln9RoCO0PpKjMWTj3VzG-8-FM; shbid="18949\\05456853077686\\0541717923892:01f72e5f3d2af5f4ed9c2f0f6d8acd991dc30b5dfc550fa61a51ef480f13dc39773fbde6"; shbts="1686387892\\05456853077686\\0541717923892:01f7ea5ec9752f20107b3a8cc8337f5ce22d2aa8de655c0c5e2576ab90c3f38f0e893b23"; rur="PRN\\05456853077686\\0541718092632:01f7b9945e5eeb60439cb72388f111bc7a21d7b24f0f5a6ad08ab2dd94c6111136fb3b89"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}




def crawling_profile_next_post(next_id,used_id,profile_name,page_count):
    global pages
    global flag
    try:
        while flag:
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            print("next_cursor :- {}".format(next_id))
            print("User_Id :- {}".format(used_id))
            if next_id is None:
                flag = False
                print("Cursor is false now so it is quiting the program.... {}".format(profile_url.format(profile_name)))

            headers["Referer"] = profile_url.format(profile_name)
            response = requests.get(next_page_url.format(used_id,next_id),headers=headers,cookies=cookies)
            if response.status_code == 401:
                print("Got 401 response So Sleep for 1-10 secends range....")
                time.sleep(random.randrange(1,10))
                new_headers["Referer"] = profile_url.format(profile_name)
                response = requests.get(next_page_url.format(used_id,next_id),headers=new_headers,cookies=cookies)
            
            json_data = response.json()
            blue_dot = json_data["user"].get("is_verified")
            products = json_data.get("items")
            next_id_ = json_data.get("next_max_id")
            if next_id_:
                item_log = dict()
                item_log["LogType"] = "Posts"
                item_log["Hastag_search"] = profile_name
                item_log["cursor"] = next_id_
                item_log["Has Next_page"] = True if next_id_ else False
                item_log["page_number"] = page_count
                logs_collection.insert_one(item_log)
            used_id_ = json_data["user"].get("pk")


            if products:
                for product in products:
                    item = dict()
                    try:
                        item["profile_url"] = profile_url.format(profile_name)
                    except Exception as e:
                        logging.error("Error in profile_url {}".format(e))
                    try:
                        item["Blue Dot"] = blue_dot
                    except Exception as e:
                        logging.error("Error in Blue Dot {}".format(e))
                    try:
                        post_code = product.get("code")
                        item["Post_url"] = post_url.format(post_code) if post_code else ""
                        item["Page No"] = page_count
                    except Exception as e:
                        logging.error("Error in Post_url {}".format(e))

                    try:
                        post_id = product.get("id")
                        item["post_id"] = post_id if post_id else ""
                    except Exception as e:
                        logging.error("Error in post_id {}".format(e))
                    try:
                        item["post_text"] = product.get("caption").get("text") if product.get("caption") else ""
                        item["full_name"] = product.get("caption").get("user").get("full_name") if product.get("caption") else ""
                    except Exception as e:
                        logging.error("Error in post_text and full_name {}".format(e))
                    # item["is_private"] = product.get("caption").get("user").get("full_name") if product.get("caption") else ""
                    try:
                        is_private = product["caption"]
                        if is_private:
                            item["is_private"] = is_private.get("user").get("is_private") if is_private else False
                    except Exception as e:
                        logging.error("Error in is_private {}".format(e))
                        pass
                    try:
                        if product.get("carousel_media"):
                            image_url =product["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
                            item["image_url"] = image_url 
                        elif product.get("image_versions2"):
                            image_url = product["image_versions2"]["candidates"][0]["url"]
                            item["image_url"] = image_url
                        else:
                            print("No images")
                    except Exception as e:
                        logging.error("Error in image_url {}".format(e))
                    # print(item)
                    try:
                        comment_count = product.get("comment_count")
                        item["Total_Comments"] = comment_count if comment_count else ""
                    except Exception as e:
                        logging.error("Error in Total_Comments {}".format(e))
                    try:
                        like_count = product.get("like_count")
                        item["Total_Likes"] = like_count if like_count else ""
                    except Exception as e:
                        logging.error("Error in Total_Likes {}".format(e))
                    try:
                        video_link = product.get("video_versions")
                        item["Video Url"] = video_link[0].get("url") if video_link else ""
                    except Exception as e:
                        logging.error("Error in Video Url {}".format(e))
                    # print("Geting product url :- {}".format(item))
                    item["Date"] = time.strftime("%Y-%d-%m")
                    item["Time"] = time.strftime("%H:%M:%S")
                    # GetLocationPost
                    mycol.insert_one(item)
                    print("Next Page data Inserted DB .......")
                    # data.append(item)
            else:
                flag = False

            next_id = next_id_
            used_id = used_id_
            page_count+=1
    except Exception as e:
        print("Errorin PDP page {} and {}".format(e,post_url.format(post_code)))
        pass





def crawling_profile_post(profile_api , profile_url_, profile_name):
    try:
        random_number = random.randrange(1,5) 
        time.sleep(random_number)

        headers["Referer"] = profile_url.format(profile_name)
        response = requests.get(profile_api,headers=headers,cookies=cookies)

        # headers["Referer"] = profile_url.format(profile_name)
        # response = requests.get(profile_api,headers=headers,cookies=cookies)
        # if response.status_code == 401:
        #     print("Got 401 response So Sleep for 1-10 secends range....")
        #     time.sleep(random.randrange(1,10))
        #     new_headers["Referer"] = profile_url.format(profile_name)
        #     response = requests.get(next_page_url.format(used_id,next_id),headers=new_headers,cookies=cookies)

        json_data = response.json()
        blue_dot = json_data["user"].get("is_verified")
        products = json_data.get("items")
        next_id = json_data.get("next_max_id")
        used_id = json_data["user"].get("pk")
        if products:
            try:
                for product in products:
                    item = dict()
                    item["Page No"] = 0
                    try:
                        item["profile_url"] = profile_url.format(profile_name)
                    except Exception as e:
                        logging.error("Error in profile_url {}".format(e))
                    try:
                        item["Blue Dot"] = blue_dot
                        post_code = product.get("code")
                        item["Post_url"] = post_url.format(post_code) if post_code else ""
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
                        # post_text = product["caption"].get("text")
                        # item["post_text"] = post_text if post_text else ""
                    except Exception as e:
                        print("Error in post_text {}".format(e))
                    try:
                        if product.get("caption"):
                            item["full_name"] = product["caption"].get("user").get("full_name")
                        elif product.get("user"):
                            item["full_name"] = product.get("user").get("full_name")

                        # full_name = product["caption"].get("user").get("full_name")
                        # item["full_name"] = full_name if full_name else ""
                    except Exception as e:
                        logging.error("Error in full_name :- {}".format(e))
                    try:
                        if product.get("caption"):
                            item["is_private"] = product["caption"].get("user").get("is_private")
                        elif product.get("user"):
                            item["is_private"] = product.get("user").get("is_private")
                            # item["is_private"] = is_private if is_private else False\
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
                    # print("Geting product url :- {}".format(item))
                    item["Date"] = time.strftime("%Y-%d-%m")
                    item["Time"] = time.strftime("%H:%M:%S")
                    mycol.insert_one(item)
                    print("First Page data Inserted DB .......")
                    # data.append(item)
            except Exception as e:
                print("Error in products data :- {}".format(e))
                pass
            
            # if next_id:
            #     item_log = dict()
            #     item_log["LogType"] = "Posts"
            #     item_log["Hastag_search"] = profile_name
            #     item_log["cursor"] = next_id
            #     item_log["Has Next_page"] = True if next_id else False
            #     item_log["page_number"] = 0
            #     logs_collection.insert_one(item_log)
            #     print("Next page function is calling for First Time.....")
                # crawling_profile_next_post(next_id,used_id,profile_name,page_count=1) # Just uncommit this for next page posts
    except Exception as e:
        print("Error in list page function :- {}".format(e))
        pass



# this function is used to fetch the data from multiple users it reads json file
f = open("input_data.json","r").read()
input_data = json.loads(f)
for post_url_ in input_data[0]["crawling_Posts"]:
    profile_name  = post_url_["profile_name"]
    profile_url__  = post_url_["profile_url"]
    profile_api_url = f"https://www.instagram.com/api/v1/feed/user/{profile_name}/username/?count=12"
    print(profile_url__)
    crawling_profile_post(profile_api_url, profile_url__ ,profile_name)







#https://www.instagram.com/api/v1/feed/user/ellyseperry/instantbollywood/?count=12






# Starting from Here 
# url = "https://www.instagram.com/api/v1/feed/user/ellyseperry/username/?count=12"




# This is function is used to get the static profiles urls
# profile_name = "instantbollywood"
# url = f"https://www.instagram.com/api/v1/feed/user/{profile_name}/username/?count=12"
# crawling_profile_post(url,profile_name)










# Taking data from input file and getting data

# Total post 174,093 posts
# https://www.instagram.com/tntsportsbr/

# next :- 2551611187940597776_1974171340 need to add 
# next_page = "2446269968181842266_376525195"
# next :- 1974171340 need to add
# used_id_ = "376525195"
# profile_name = "icc"
# crawling_profile_next_post(next_page,used_id_,profile_name,page_count=760)


# profiles = [{"profile_id":"173560420","pagination":"2977255928651690524_173560420"}]



# df = pd.DataFrame(data)
# df.to_excel("instagram_manish4u_data.xlsx",index=False)






#Input URls Data :- 
# 
#[{"crawling_comments":[{"post_id":"3015320177991345619","post_url":"https://www.instagram.com/p/CnYkbndPeXT/"},{"post_id":"3014285071116831110","post_url":"https://www.instagram.com/p/CnU5E1DromG/"}]},
    # {"crawling_Posts":[{"profile_name":"realdonaldtrump","profile_url":"https://www.instagram.com/realdonaldtrump/"},{"profile_name":"who","profile_url":"https://www.instagram.com/who/"},{"profile_name":"kyliejenner","profile_url":"https://www.instagram.com/kyliejenner/"},
    # {"profile_name":"beyonce","profile_url":"https://www.instagram.com/beyonce/"},
    # {"profile_name":"cristiano","profile_url":"https://www.instagram.com/cristiano/"},
    # {"profile_name":"natgeo","profile_url":"https://www.instagram.com/natgeo/"}]}]

 





