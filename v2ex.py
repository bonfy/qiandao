# coding: utf-8

import requests
import re
import os

# if you don't have a config.py
# You can set v2ex_username, v2ex_password yourself

v2ex_username = os.getenv('v2ex_username')
v2ex_password = os.getenv('v2ex_password')


def qiandao_v2ex():
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.57 Safari/537.36 OPR/40.0.2308.15 (Edition beta)',
                'Referer': 'https://v2ex.com/signin',
                'Origin': 'https://www.v2ex.com'
              }
    session = requests.Session()
    session.headers.update(headers)

    resp = session.get('https://v2ex.com/signin')
    u, p = re.findall(r'class="sl" name="([0-9A-Za-z]{64})"', resp.text)
    once_code = re.search(r'value="(\d+)" name="once"', resp.text).group(1)

    resp = session.post('https://www.v2ex.com/signin', {u: v2ex_username, p: v2ex_password, 'once':once_code, 'next':'/'})
    resp = session.get('https://www.v2ex.com/mission/daily')
    if u'每日登录奖励已领取' in resp.text:
        print('Already got it.')
    else:
        resp = session.get('http://v2ex.com' + re.search(r'/mission/daily/redeem\?once=\d+', resp.text).group())
        if resp.ok:
            print('Got daily gold.')

if __name__ == '__main__':
    qiandao_v2ex()
