# -*- coding: utf-8 -*-

import http.client
import hashlib
from urllib import parse
import random
import json

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'
httpClient = None
myurl = '/api/trans/vip/translate'


while 1:
    q = input('请输入要翻译的语句\n')
    if q == 'done':
        break
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + \
        parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + \
        '&salt=' + str(salt) + '&sign=' + sign

    # print(myurl)
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_json = response.read().decode('utf-8')
        result_dict = json.loads(result_json)
        #print(result_dict)
        #print(myurl)

        dst = result_dict["trans_result"][0]["dst"]
        print(dst)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
