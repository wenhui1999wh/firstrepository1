# import time
# import hashlib
# import base64
# import requests
# from Crypto.Cipher import AES
#
#
# mysticTime = str(int(time.time() * 1000))
#
# def get_sign(mysticTime):
#     # key为固定单词
#     data = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key=fsdsogkndfokasodnaso'
#     sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
#     return sign
#
# def get_resppnse(sign, mysticTime):
#     word = input("输入你要翻译的内容")
#     url = 'https://dict.youdao.com/webtranslate'
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#         'Connection': 'keep-alive',
#         'Content-Length': '325',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': 'OUTFOX_SEARCH_USER_ID=602478100@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=938885626.2245677',
#         'Host': 'dict.youdao.com',
#         'Origin': 'https://fanyi.youdao.com',
#         'Referer': 'https://fanyi.youdao.com/',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-site',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
#         'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#     }
#     data = {
#         "i": f"{word}",
#         "from": "zh-CHS",
#         "to": "en",
#         "domain": "0",
#         "dictResult": "true",
#         "keyid": "webfanyi",
#         "sign": sign,
#         "client": "fanyideskweb",
#         "product": "webfanyi",
#         "appVersion": "1.0.0",
#         "vendor": "web",
#         "pointParam": "client,mysticTime,product",
#         "mysticTime": mysticTime,
#         "keyfrom": "fanyi.web",
#         "mid": "1",
#         "screen": "1",
#         "model": "1",
#         "network": "wifi",
#         "abtest": "0",
#         "yduuid": "abcdefg",
#     }
#     response = requests.post(url, headers=headers, data=data).text
#     print("response", response)
#     decodeKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
#     decodeIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
#     # 先对两个参数进行参数加密
#     key = hashlib.md5(decodeKey.encode(encoding='utf-8')).digest()
#     iv = hashlib.md5(decodeIv.encode(encoding='utf-8')).digest()
#     # AES解密
#     aes_en = AES.new(key, AES.MODE_CBC, iv)
#     # 将已经加密的数据放进该方法
#     data_new = base64.urlsafe_b64decode(response)
#     # 参数准备完毕后，进行解密
#     result = aes_en.decrypt(data_new).decode('utf-8')
#     print("翻译结果", result)
#
#
#
# get_resppnse(get_sign(mysticTime), mysticTime)
#
import os
import requests
import subprocess
import json
from functools import partial
import hashlib
import time
import execjs
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

# print("js_name", execjs.get().name)


localtime = str(int(time.time() * 1000))
data = "client=fanyideskweb&mysticTime={}&product=webfanyi&key=fsdsogkndfokasodnaso".format(localtime)
sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Referer": "https://fanyi.youdao.com/index.html"
}
cookies = {
    "OUTFOX_SEARCH_USER_ID": "-2094880112@10.108.162.135",
    "OUTFOX_SEARCH_USER_ID_NCOO": "86107500.53660281"
}
url = "https://dict.youdao.com/webtranslate"
word = input('请输入翻译内容:')
data = {
    "i": f"{word}",
    "from": "auto",
    "to": "",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": localtime,
    "keyfrom": "fanyi.web"
}
response = requests.post(url=url, headers=headers, cookies=cookies, data=data).text
# print("response", response)
with open('youdao.js', 'r', encoding='utf-8') as po:
    signs = execjs.compile(po.read()).call('datas', response)
    text = json.loads(signs)
    try:
        print(text['dictResult']['ce']['word']['trs'][0]['#text'])
    except:
        print(text['translateResult'][0][0]['tgt'])


