import hashlib
import random
import requests
import time
import json

from server.models import User


def request_im(accid, name):
    AppKey = 'a9232b9c59aba44b53f95579506cd4a8'
    AppSecret = 'c74b7724c366'

    # 随机数
    Nonce = random.randint(1, 99999999)
    Nonce = "%08d" % Nonce
    # 时间戳
    CurTime = time.time()
    CurTime = str(CurTime)
    content = AppSecret + Nonce + CurTime
    # checksum
    CheckSum = hashlib.sha1(content.encode()).hexdigest()

    accid = accid
    name = name
    url = 'https://api.netease.im/nimserver/user/create.action'
    headers = {
        "appKey": AppKey,
        "NoNce": Nonce,
        "CurTime": CurTime,
        "CheckSum": CheckSum,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {
        "accid": accid,
        "name": name
    }
    response = requests.post(url, headers=headers, params=params)
    info = response.content.decode()
    info = json.loads(info).get("info")

    return info


class UserServices(object):

    @staticmethod
    def create_user(kwargs):
        password = kwargs.pop('password')
        accid = kwargs.get("accid")
        name = kwargs.get("name")
        info = request_im(accid, name)  # {'token': , 'name': , 'accid': }
        user = User(**info)
        user.set_password(password)
