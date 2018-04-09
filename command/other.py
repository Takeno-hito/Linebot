import sys, os
import json
import requests
sys.path.append(os.pardir)
import botconfig

def bye(data):
    # data : type dic (line event)
    if(data.source.type == 'user'):
        pass

    else if(data.source.type == 'group'):
        replytext(data.replyToken, "ばいばい；；")
        quitgroup(data.source.groupId)

    else if(data.source.type == 'room'):
        replytext(data.replyToken, "ばいばい；；")
        quitroom(data.source.roomId)

def status(data):
    if(data.source.type == 'user'):
        header = "Bearer " + access_token
        url = 'https://api.line.me/v2/bot/profile/' + data.source.userId
        response = requests.get(url, headers = header)
        resData = json.load(response)

        string = '''
        あなたの情報
        type : user
        userId : {}
        名前 : {}
        '''.format(data.source.userId, resData.displayName)
        replytext(data.replyToken, string)

    if(data.source.type == 'group'):
        if('data.soure.userId' in locals()):
            header = "Bearer " + access_token
            url = 'https://api.line.me/v2/bot/group/{groupId}/member/{userId}'.format(
                groupId = data.source.groupId, userId = data.source.userId)
            response = requests.get(url, headers = header)
            resData = json.load(response)

            string = '''
            グループの情報
            type : group
            groupId : {}

            あなたの情報
            userId : {}
            名前 : {}
            '''.format(data.source.groupId, data.source.userId, resData.displayName)
            replytext(data.replyToken, string)

        else:
            string = '''
            グループの情報
            type : group
            groupId : {}

            あなたの情報
            userId : *****
            名前 : *****

            情報を得たい場合は、友達追加をして、LINEの公式アカウントの利用条件に同意する必要があります。
            同意する方法の一つに、このBotを追加する方法があります。
            '''.format(data.source.groupId)
            replytext(data.replyToken, string)
    else if(data.source.type == 'room'):
        string = 'ルームでは、一部の機能が制限されています。グループに招待して使用するようお願いします。'
