# coding: utf-8

import requests
import os

mafengwo_username = os.getenv('mafengwo_username')
mafengwo_password = os.getenv('mafengwo_password')

def mafengwo():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.57 Safari/537.36 OPR/40.0.2308.15 (Edition beta)',
        'Referer': 'https://passport.mafengwo.cn/login-popup.html',
        'Origin': 'https://passport.mafengwo.cn',
        'Pragma': 'no-cache',
        'Host': 'passport.mafengwo.cn',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    session = requests.Session()
    session.headers.update(headers)

    login_url = 'https://passport.mafengwo.cn/login-popup.html'
    resp = session.post(login_url, {'passport': mafengwo_username, 'password': mafengwo_password, 'code':''})

    # Login Complete
    # TODO: Daka
