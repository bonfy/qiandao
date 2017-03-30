# coding: utf-8

import requests
import re
import os

# You can set jobbole_username, jobbole_password yourself

jobbole_username = os.getenv('jobbole_username')
jobbole_password = os.getenv('jobbole_password')


def qiandao_jobbole():
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.57 Safari/537.36 OPR/40.0.2308.15 (Edition beta)',
                'Referer': 'http://www.jobbole.com/login/?redirect=http%3A%2F%2Fwww.jobbole.com%2F',
                'Origin': 'http://www.jobbole.com'
              }
    session = requests.Session()
    session.headers.update(headers)

    dct = dict(action='user_login', user_login=jobbole_username, user_pass=jobbole_password, remember_me=1, redirect_url='http://www.jobbole.com/')

    resp = session.post('http://www.jobbole.com/wp-admin/admin-ajax.php', data=dct)
    res_json = resp.json()
    if res_json['jb_result'] == 0: # 0 for login success -1 for login fail
        dct_point = dict(action='get_login_point')
        resp = session.post('http://www.jobbole.com/wp-admin/admin-ajax.php', data=dct_point)
        qiandao_status = resp.json()
        if qiandao_status['jb_result'] == 0:
            print('{}, 积分为{}'.format(qiandao_status['jb_msg'], qiandao_status['user_points']))
        else:
            print(qiandao_status['jb_msg'])
    else:
        print('login failed\nPlease check your username and password')

if __name__ == '__main__':
    qiandao_jobbole()
