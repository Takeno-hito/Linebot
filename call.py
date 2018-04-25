# -*- coding: utf-8 -*-

import sys
import json
from command import other
#from command.minigame import gamble, rpg

dataString = sys.argv[1]
data = json.loads(dataString)

print 'Hello, World!'

for event in data['events']:
    if(event['type'] == 'message'):
        if(event['message']['type'] == 'text'):
            text = event['message']['text']
            if(text == '/help'):
                other.help(event)
            elif(text == '/bye'):
                print 'Bye!'
                other.bye(event)
            elif(text == '/lot'):
                gamble.lottery(event)
            elif(text == '/stat'):
                other.status(event)
