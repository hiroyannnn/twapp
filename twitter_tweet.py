
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
#import settings
from requests_oauthlib import OAuth1Session
import json

def postTweet(consumer_key,consumer_secret,token,token_secret,text):
    # key
    #CK = settings.consumer_key
    #CS = settings.consumer_secret
    #AT = settings.token
    #AS = settings.token_secret
    CK = consumer_key
    CS = consumer_secret
    AT = token
    AS = token_secret


    # ツイート投稿用のURL
    url_text = "https://api.twitter.com/1.1/statuses/update.json"

    # OAuth認証で POST method で投稿
    twitter = OAuth1Session(CK, CS, AT, AS)

    # ツイート本文
    # Media ID を付加してテキストを投稿
    params = {'status':text}
    req_media = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print ("テキストアップデート失敗: %s", req_text.text)
        exit()

    print ("OK")
