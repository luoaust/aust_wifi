# -*- coding = utf-8 -*-
# @Time : 2021/4/14 0:07
# @Author: 罗清澈
# @File : 2.py
# @Software : PyCharm
# -*- coding = utf-8 -*-
# @Time : 2021/4/13 23:30
# @Author: 罗清澈
# @File : aust.py
# @Software : PyCharm

import requests

url = 'http://10.255.0.19/a41.js?version=1618299938425'

data = {
    "callback": "dr1003",
    "DDDDD": "学号@aust",  ##这里输入学号
    "upass": "密码",      ## 这里输入校园网的密码
    "0MKKey": "123456",
    "R1": "0",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "v6ip": "v: 8410",
}

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/javascript; charset=gbk",
    "Origin": "http://10.255.0.19",
    "Referer": "http://10.255.0.19/a79.htm",
    "Content-Length": "3185",
    "Cookie": "PHPSESSID=2p6flpg3ebhafjjkubo7v512mr",
    "Host":"10.255.0.19",
    "Connection": "keep-alive",
    "Accept": "*/*",
}

response = requests.post(url,data, headers =header).status_code

print("回应代码{}".format(response))
