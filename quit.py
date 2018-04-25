# -*- coding: utf-8 -*-

import sys, os

import requests
sys.path.append(os.pardir)
import botconfig
import json

def quitroom(groupId):
    endpoint = "https://api.line.me/v2/bot/group/{}/leave".format(botconfig.access_token)
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(botconfig.access_token)
    }
    requests.post(endpoint, headers=headers)
