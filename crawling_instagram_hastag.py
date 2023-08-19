from requests import Session
import requests
import pandas as pd
from lxml import html
import time
import random
from datetime import datetime
import json
import pdb
import pymongo


has_tag_data = []
all_cursors = []
post_url = "https://www.instagram.com/p/{}/"

profile_url = "https://www.instagram.com/explore/tags/{}/"

tag_cookies = {
    'ig_did': 'E8E2C977-E665-4EEB-B128-6D8D92A85228',
    'datr': 'xKmkYzg_H2hB218oV81-7V7g',
    'mid': 'Y6SpzwAEAAFEyKlch75tbOOP3puO',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'rur': '"PRN\\05456853077686\\0541706468477:01f782e44afe7cce3121c32b78088a4eb7320736a77efe995da8eab7956238b97063c3fd"',
    'fbsr_124024574287414': 'eg619RAVIUnwCRrdJAfkwqE6x5_cvxFkt0Fqpl30qe8.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQVFkTFJCS29adHRTZVk2di0zeVpzZHZmLUpLVDlfbjBLLWYxUUxvOTY3aDRodTk0N0x0RF9Xd29nU25sTFR5WVZabW8wTVZkSnR6UUVBRVFQUGgtU09lZDZaUS1GQTJqbEctcnRhMFRfTG90U0tMY2w5OHZOZ1l1Qm15N0VqZ2RRTXBtTG42ZlhIS3Q3Ny1HeElXWWdjQUg5cXFUZk0yR2k0NXhJUWV4YnloVjd5eDQ1STRjVDd5TEV3TmNOdUhZTGI4MkxzbW1Td3BpRi11N1NvQW00THhPNVFLYm80OTQxa1RYcUQxQnpWclNZWVZlRGc3VEk0dDZvTUVtZDZXc0VDc0Y0eEVjbHZ3T3hZZDFIU3l5WnVZcFV1TE9ZLVQydkVkMGhSZUc5bmF2VHpUQVhVYjZycTVEdHlCSEJvSmpkQnpZSlg5OV9QZmtBQmp5ajdlTmI1ZTM1RlZub0VhU1FfcWRLMjM5ZTAxdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFDSVBaQzNjWkFDeDk0UU1QQjE5WTFaQzFhbXl0elNQRFpCbFpBM0pKTVBmZm9qR1Y4VXRoV0k1d1pCbVZuYXVrOWZVVnc1UW5Kc0c5cjlBbDVyN21ES1VtTUlLazRFemF3cXFVOVk2c2hBMTRVSmRhcEpReVRYZ2VWTVhoVTlrNW5PcHhjczlCOWxDTVZCNjFNNDYwckhsOVpCaWppR0V5bFJaQWJ0QWp3T3lPNjFHSVVrUVkwRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzQ5MzIyMDN9',
    'csrftoken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'ds_user_id': '56853077686',
    'sessionid': '56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdTUvKIEPWPmVvVB1xAl9fDMwUupp-IgkpyrQHs8A',
    'shbid': '"18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"',
    'shbts': '"1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"',
}

tag_headers = {
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
    'Referer': 'https://www.instagram.com/explore/tags/rahulgandhi/',
    # 'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="PRN\\05456853077686\\0541706468477:01f782e44afe7cce3121c32b78088a4eb7320736a77efe995da8eab7956238b97063c3fd"; fbsr_124024574287414=eg619RAVIUnwCRrdJAfkwqE6x5_cvxFkt0Fqpl30qe8.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQVFkTFJCS29adHRTZVk2di0zeVpzZHZmLUpLVDlfbjBLLWYxUUxvOTY3aDRodTk0N0x0RF9Xd29nU25sTFR5WVZabW8wTVZkSnR6UUVBRVFQUGgtU09lZDZaUS1GQTJqbEctcnRhMFRfTG90U0tMY2w5OHZOZ1l1Qm15N0VqZ2RRTXBtTG42ZlhIS3Q3Ny1HeElXWWdjQUg5cXFUZk0yR2k0NXhJUWV4YnloVjd5eDQ1STRjVDd5TEV3TmNOdUhZTGI4MkxzbW1Td3BpRi11N1NvQW00THhPNVFLYm80OTQxa1RYcUQxQnpWclNZWVZlRGc3VEk0dDZvTUVtZDZXc0VDc0Y0eEVjbHZ3T3hZZDFIU3l5WnVZcFV1TE9ZLVQydkVkMGhSZUc5bmF2VHpUQVhVYjZycTVEdHlCSEJvSmpkQnpZSlg5OV9QZmtBQmp5ajdlTmI1ZTM1RlZub0VhU1FfcWRLMjM5ZTAxdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFDSVBaQzNjWkFDeDk0UU1QQjE5WTFaQzFhbXl0elNQRFpCbFpBM0pKTVBmZm9qR1Y4VXRoV0k1d1pCbVZuYXVrOWZVVnc1UW5Kc0c5cjlBbDVyN21ES1VtTUlLazRFemF3cXFVOVk2c2hBMTRVSmRhcEpReVRYZ2VWTVhoVTlrNW5PcHhjczlCOWxDTVZCNjFNNDYwckhsOVpCaWppR0V5bFJaQWJ0QWp3T3lPNjFHSVVrUVkwRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzQ5MzIyMDN9; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdTUvKIEPWPmVvVB1xAl9fDMwUupp-IgkpyrQHs8A; shbid="18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"; shbts="1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

flag = True
pages_count_ = 10


post_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'loaErFG0dIbM2XErdvS2mFTjrDGq4kjp',
    'X-Instagram-AJAX': '1006879122',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': 'hmac.AR0YGf2APW88ep4_LaZc9LodVWbWV1V6bYHmwfV4LnQm82vM',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/explore/tags/rahulgandhi/',
    'Cookie': 'ig_did=E8E2C977-E665-4EEB-B128-6D8D92A85228; datr=xKmkYzg_H2hB218oV81-7V7g; mid=Y6SpzwAEAAFEyKlch75tbOOP3puO; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="PRN\\05456853077686\\0541706468542:01f7f0e6b801c5e25250c8e1a2aab1f36535d5479f8d8b55df8a01b482a7c145521297bf"; fbsr_124024574287414=eg619RAVIUnwCRrdJAfkwqE6x5_cvxFkt0Fqpl30qe8.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQVFkTFJCS29adHRTZVk2di0zeVpzZHZmLUpLVDlfbjBLLWYxUUxvOTY3aDRodTk0N0x0RF9Xd29nU25sTFR5WVZabW8wTVZkSnR6UUVBRVFQUGgtU09lZDZaUS1GQTJqbEctcnRhMFRfTG90U0tMY2w5OHZOZ1l1Qm15N0VqZ2RRTXBtTG42ZlhIS3Q3Ny1HeElXWWdjQUg5cXFUZk0yR2k0NXhJUWV4YnloVjd5eDQ1STRjVDd5TEV3TmNOdUhZTGI4MkxzbW1Td3BpRi11N1NvQW00THhPNVFLYm80OTQxa1RYcUQxQnpWclNZWVZlRGc3VEk0dDZvTUVtZDZXc0VDc0Y0eEVjbHZ3T3hZZDFIU3l5WnVZcFV1TE9ZLVQydkVkMGhSZUc5bmF2VHpUQVhVYjZycTVEdHlCSEJvSmpkQnpZSlg5OV9QZmtBQmp5ajdlTmI1ZTM1RlZub0VhU1FfcWRLMjM5ZTAxdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFDSVBaQzNjWkFDeDk0UU1QQjE5WTFaQzFhbXl0elNQRFpCbFpBM0pKTVBmZm9qR1Y4VXRoV0k1d1pCbVZuYXVrOWZVVnc1UW5Kc0c5cjlBbDVyN21ES1VtTUlLazRFemF3cXFVOVk2c2hBMTRVSmRhcEpReVRYZ2VWTVhoVTlrNW5PcHhjczlCOWxDTVZCNjFNNDYwckhsOVpCaWppR0V5bFJaQWJ0QWp3T3lPNjFHSVVrUVkwRVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzQ5MzIyMDN9; csrftoken=loaErFG0dIbM2XErdvS2mFTjrDGq4kjp; ds_user_id=56853077686; sessionid=56853077686%3ALrdaBEnLQwm1wT%3A7%3AAYdTUvKIEPWPmVvVB1xAl9fDMwUupp-IgkpyrQHs8A; shbid="18949\\05456853077686\\0541706300671:01f78a2489b9ef37fb2de3ea1e412b59e5640243cb4c64c86dd9cc0c41061e7e49ffd3dc"; shbts="1674764671\\05456853077686\\0541706300671:01f7bcc698bdaef8eb07491b743346f2912e3213781b80e78e58ab2aea3cc139c5fdecb5"; fbsr_124024574287414=05NrH3ZwyY4sqTidFGFdZ0U-k159fDiN5olvTnHX1fk.eyJ1c2VyX2lkIjoiMTAwMDEyNTAzMjY1MzcwIiwiY29kZSI6IkFRQUo1Y1h3WnJWV0RsNWFWbWZGRWZuTlNzb2hzekFnWTVFZ09TaW1abl9aNkN4TF9kd0NkSTRuaWNLTkZPR1R3QnRCNE10Y0xMaXVfSjJqLWNISjJoNzEwSmJwWVJ5aVdZTVQ4X3dfQnllTTlBZHRnNVBWbl9sd0NZR192b244OGR6dGkza3RBRGpLM1ZZQklnZWVHNTR0VjNtbVdWcnllOGg1TVMyMFhGdkljMEdrN0RkeU5INndWWWNrS1JxQjlmU25DcmVDamhJZkNUME9MeElHUTRtMnEwZTBPaE9OaGFjZ2xNRkwzNVkwa05PVnVuTEhuOTJiX2p4UHNNTnYwMUszNVYyWUc5dm0yUng1cG9hUkY0MU9IRXhkdXVwQnNDRjdJRmxzcEwxZTBWN3M3dGYtYl92dzVQM1FNbzNicUQzRG1NTmRGQkVnR1ZDbkloMEs2NGRqR3lKVXh0dWpKS2o1dFNJbGwzN2xndyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFITDZwVjFLVFlXaEdGb2RSVTROY29HWkF0WkN0MEJqdVpBNVZYbkhVR0FaQVdSQWs0alVXcU95WXpBU0twckpJMEFhT1pDVFNScDFkQ1E4eGRVWGNYN0xnQmFNMGkwMHN6YWt6VnVnSTk2eW9kTUVYWkI5VHVQaHZBd24yU3h6THlCc0lhSkwwVnJYb0t1WVBrSkFxbG5yOFZldFpCVFk1c214WElvaWxNYWhQVUtDRks1MnM0WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NDkzMjE4MX0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'include_persistent': '0',
    'max_id': 'QVFEbDByX0lqSTlqMTNTdFVxUmpTd1lmM25JZUk4S2o4OHFvMXM0RmNCWVpmWGlZZ1lnU0RpcHRaNUhwQ2FpSlNrUnd6MG55MWZCeDY3ZGlJdTRMb01XYg==',
    'next_media_ids[]': '2606538588778855211',
    'page': '1',
    'surface': 'grid',
    'tab': 'recent',
}


def Create_Database_connect_with_data():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client



def crawling_hastag_next_page(next_cursor,next_media_ids,page_number,tag):
    global flag
    global pages_count_
    try:
        while flag:
            random_number = random.randrange(1,5) 
            time.sleep(random_number)
            print("next_cursor :- {}".format(next_cursor))
            data["max_id"] = next_cursor
            data["page"] = page_number
            # if page_number <= pages_count_:
            #     flag = False
            # pdb.set_trace()
            data["next_media_ids[]"] = next_media_ids if next_media_ids else "[]"
            if next_cursor is None:
                flag = False
            post_headers["Referer"] = "https://www.instagram.com/explore/tags/{}/".format(tag)
            response = requests.post('https://www.instagram.com/api/v1/tags/{}/sections/'.format(tag), headers=post_headers, data=data)
            # pdb.set_trace()
            json_data = response.json()
            next_id_ = json_data.get("next_max_id")
            next_page = json_data.get("next_page")
            sections = json_data.get("sections")
            if sections:
                for section in sections:
                    for medias in section["layout_content"]["medias"]:
                        # for media in medias:
                        item = dict()
                        item["Hastag_url"] = profile_url.format(tag)
                        item["Page count"] = page_number
                        item["Hastag"] = "#{}".format(tag)
                        item["PK_id"] = medias.get("media").get("pk")
                        item["id"] = medias.get("media").get("id")
                        code = medias.get("media").get("code")
                        item["post_url"] = post_url.format(code) if code else ""
                        if medias.get("media").get("carousel_media"):
                            image_url = medias["media"]["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
                            item["image_url"] = image_url 
                        elif medias.get("media").get("image_versions2"):
                            image_url = medias["media"]["image_versions2"]["candidates"][0]["url"]
                            item["image_url"] = image_url
                        print("******____________********")
                        try:
                            post_text = medias["media"].get("caption")
                            item["post_text"] = post_text.get("text") if post_text else ""
                        except Exception as e:
                            print("Error in Text :- {}".format(e))
                        try:
                            full_name = medias["media"].get("caption")
                            item["full_name"] = full_name.get("user").get("full_name") if full_name else ""
                        except Exception as e:
                            print("Error in full_name :- {}".format(e))
                        try:
                            is_private = medias["media"].get("caption")
                            item["is_private"] = is_private.get("user").get("is_private") if is_private else False
                        except Exception as e:
                            print("Error in is_private :- {}".format(e))
                        try:
                            username = medias["media"].get("caption")
                            item["profile_name"] = username.get("user").get("username") if username else "Not mention"
                        except Exception as e:
                            print("Error in profile_name :- {}".format(e))
                        try:
                            like_count = medias["media"].get("like_count")
                            item["like_count"] = like_count if like_count else ""
                        except Exception as e:
                            print("Error in like_count :- {}".format(e))
                        try:
                            comment_count = medias["media"].get("comment_count")
                            item["comment_count"] = comment_count if comment_count else ""
                        except Exception as e:
                            print("Error in comment_count :- {}".format(e))
                        item["post_type"] = "recent_post"
                        item["Date"] = time.strftime("%Y-%d-%m")
                        item["Time"] = time.strftime("%H:%M:%S")
                        print("recent_post with next page :- {}".format(item))
                        # pdb.set_trace()
                        mycollection.insert_one(item)
                        print("Inserted DB .......")
                        # has_tag_data.append(item)
            else:
                flag = False

            next_cursor = next_id_
            page_number = next_page
            next_media_ids = json_data["next_media_ids"] if json_data.get("next_media_ids") else ""
            tag = tag
            log_item = dict()
            log_item["LogType"] = "Hastag_logs"
            log_item["Hastag_search"] = tag
            log_item["cursor"] = next_cursor
            log_item["Has Next_page"] = True if next_cursor else False
            log_item["page_number"] = page_number
            log_item["next_media_ids"] = next_media_ids
            logs_collection.insert_one(log_item)


            
    except Exception as e:
        print("Errorin PDP page {}".format(e))
        pass



def crawling_hastag_first(tag,page_number):
    params = {'tag_name': '{}'.format(tag),}
    tag_headers["Referer"] = "https://www.instagram.com/explore/tags/{}/".format(tag)
    response = requests.get('https://www.instagram.com/api/v1/tags/web_info/', params=params, cookies=tag_cookies, headers=tag_headers)
    # pdb.set_trace()
    json_data = response.json()
    top_post = json_data["data"].get("top")
    if top_post:
        for top in top_post["sections"]:
            for media in top["layout_content"]["medias"]:
                item = dict()
                item["Hastag_url"] = profile_url.format(tag)
                item["Page count"] = page_number
                item["Hastag"] = "#{}".format(tag)
                item["PK_id"] = media.get("media").get("pk")
                item["id"] = media.get("media").get("id")
                code = media.get("media").get("code")
                item["post_url"] = post_url.format(code) if code else ""
                if media.get("media").get("carousel_media"):
                    image_url = media["media"]["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
                    item["image_url"] = image_url 
                elif media.get("media").get("image_versions2"):
                    image_url = media["media"]["image_versions2"]["candidates"][0]["url"]
                    item["image_url"] = image_url
                post_text = media["media"].get("caption").get("text")
                item["post_text"] = post_text if post_text else ""
                full_name = media["media"].get("caption").get("user").get("full_name")
                item["full_name"] = full_name if full_name else ""
                is_private = media["media"].get("caption").get("user").get("is_private")
                item["is_private"] = is_private if is_private else False
                username = media["media"].get("caption").get("user").get("username")
                item["profile_name"] = username if username else "Not mention"
                like_count = media.get("media").get("like_count")
                item["like_count"] = like_count if like_count else ""
                comment_count = media.get("media").get("comment_count")
                item["comment_count"] = comment_count if comment_count else ""
                item["post_type"] = "top_post"
                item["Date"] = time.strftime("%Y-%d-%m")
                item["Time"] = time.strftime("%H:%M:%S")
                print("top_post :- {}".format(item))
                mycollection.insert_one(item)
                print("Inserted DB .......")

    recent_post = json_data["data"].get("recent")
    if recent_post:
        for top in recent_post["sections"]:
            for media in top["layout_content"]["medias"]:
                item = dict()
                item["Hastag_url"] = profile_url.format(tag)
                item["Page count"] = page_number
                item["Hastag"] = "#{}".format(tag)
                item["PK_id"] = media.get("media").get("pk")
                item["id"] = media.get("media").get("id")
                code = media.get("media").get("code")
                item["post_url"] = post_url.format(code) if code else ""
                if media.get("media").get("carousel_media"):
                    image_url = media["media"]["carousel_media"][0]["image_versions2"]["candidates"][0]["url"]
                    item["image_url"] = image_url 
                elif media.get("media").get("image_versions2"):
                    image_url = media["media"]["image_versions2"]["candidates"][0]["url"]
                    item["image_url"] = image_url
                post_text = media["media"].get("caption")
                item["post_text"] = post_text.get("text") if post_text else ""
                full_name = media["media"].get("caption")
                item["full_name"] = full_name.get("user").get("full_name") if full_name else ""
                is_private = media["media"].get("caption")
                item["is_private"] = is_private.get("user").get("is_private") if is_private else False
                username = media["media"].get("caption")
                item["profile_name"] = username.get("user").get("username") if username else "Not mention"
                like_count = media.get("media").get("like_count")
                item["like_count"] = like_count if like_count else ""
                comment_count = media.get("media").get("comment_count")
                item["comment_count"] = comment_count if comment_count else ""
                item["post_type"] = "recent_post"
                item["Date"] = time.strftime("%Y-%d-%m")
                item["Time"] = time.strftime("%H:%M:%S")
                print("recent_post :- {}".format(item))
                mycollection.insert_one(item)
                print("Inserted DB .......")
    
    next_cursor = json_data["data"]["recent"].get("next_max_id")
    next_media_ids = json_data["data"]["recent"].get("next_media_ids")
    page_number = json_data["data"]["recent"].get("next_page")
    if next_cursor:
        # pdb.set_trace()
        item = dict()
        item["LogType"] = "Hastag_logs"
        item["Hastag_search"] = tag
        item["cursor"] = next_cursor
        item["Has Next_page"] = True if next_cursor else False
        item["page_number"] = page_number
        item["next_media_ids"] = next_media_ids
        logs_collection.insert_one(item)
        crawling_hastag_next_page(next_cursor,next_media_ids,page_number,tag)




client = Create_Database_connect_with_data()
mydb = client["instagram"]
mycollection = mydb["instagram_Hastag_POST"]
logs_collection = mydb["instagram_logs"]
tag = "karnatakaelections2023"
cursor_data = logs_collection.find({"Hastag_search":f"{tag}"})



# checking if tag is already scraped or not if yes then it take last cursor from local DB and then start fetch data for tag
for cur in cursor_data:
    all_cursors.append(cur)

if all_cursors:
    start_cursor = all_cursors[-1].get("cursor")
    start_next_media_ids = all_cursors[-1].get("next_media_ids")
    start_page_number = all_cursors[-1].get("page_number")
    start_tag = all_cursors[-1].get("Hastag_search")
    time.sleep(3)
    print("Found Cursor in DB and Started scraping with last cursor....")
    crawling_hastag_next_page(start_cursor,start_next_media_ids,start_page_number,start_tag)
else:
    time.sleep(3)
    print("Not found the any cursor for tag :- {}".format(tag))
    crawling_hastag_first(tag,page_number=0)
    

#     # crawling_hastag_first(tag,page_number=0)
#     crawling_hastag_next_page(next_cursor,next_media_ids,page_number,tag)






# df = pd.DataFrame(has_tag_data)
# df.to_excel("hastag_{}_posts.xlsx".format(tag),index=False)