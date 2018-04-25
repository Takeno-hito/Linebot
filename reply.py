# -*- coding: utf-8 -*-
import sys, os

import requests
import logging
sys.path.append(os.pardir)
import botconfig
import json

def replytext(Token, text):
    try:
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
    except:
        logger = logging.getLogger('LoggingTest')
        logger.setLevel(10)
        fh = logging.FileHandler('logger.log')
        logger.addHandler(fh)
        sh = logging.StreamHandler()
        logger.addHandler(sh)

        formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.log(50, '')-)
