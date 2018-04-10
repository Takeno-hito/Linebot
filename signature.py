# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
import json
import botconfig

def check_signature(head, body):
    pass
    hash = hmac.new(channel_secret.encode('utf-8', body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash)
    headdic = json.load(head)
