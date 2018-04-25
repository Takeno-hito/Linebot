# -*- coding: utf-8 -*-
import sys, os

import requests
import logging
sys.path.append(os.pardir)
import botconfig
import json

def replytext(Token, text):
    print 'called:{}'.format(text)
    print Token
    payload = {
        "replyToken": "{}".format(Token),
        "messages":[
            {
                "type":"text",
                "text": "{}".format(text)
            }
        ]
    }
    endpoint = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(botconfig.access_token)
    }
    r = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    print r.text
    print payload
