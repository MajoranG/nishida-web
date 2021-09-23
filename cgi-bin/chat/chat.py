#!/usr/bin/python3

import cgi
import cgitb
import os
import sys
import json
import time
from collections import defaultdict
import datetime
import pytz
import random
import re

def add_message(n,m):
    f = open(dir_name + file_name, mode="a")
    list1 = defaultdict(list)
    if n == 0:
        #list1["name"].append("シリアルナンバー" + id + "の西田")
        list1["name"].append("名無しの西田さん")
    else:
        list1["name"].append(n)
        for z in re.findall(r'!z\d+', m):
            n = int(z[2:])
            full_z = "絶対" * n
            m = m.replace(z, full_z)
        m = m.replace('!Z', '絶対絶対100%どころか120%1000%絶対')
        list1["ip"].append(ip)
        list1["id"].append(id)
        nowdate = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        strnowdate = nowdate.strftime('%Y/%m/%d %H:%M:%S')
        list1["time"].append(strnowdate)
        list1["message"].append(m)
        f.write(str(ut)+","+str(list1["name"][0])+","+str(list1["message"][0])+","+str(list1["ip"][0])+","+str(list1["time"][0])+","+list1["id"][0]+"\n")
        f.close()

def message_func(lists):
    fb = open(dir_name + file_name, mode = "r")
    for line in fb:
        data = line.split(",")
        lists["utime"].append(data[0])
        lists["name"].append(data[1])
        lists["message"].append(data[2])
        lists["ip"].append(data[3])
        lists["time"].append(data[4])
        lists["id"].append(data[5].strip())
        if data[2].strip() == "!now":
            nowdate = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
            strnowdate = nowdate.strftime('%Y/%m/%d %H:%M:%S')
            lists["utime"].append(data[0])
            lists["name"].append("NSDBOT")
            lists["message"].append("NOW:"+strnowdate)
            lists["ip"].append("NSD.NSD.NSD.NSD")
            lists["id"].append('NSD')
            lists["time"].append(data[4])
        if data[2].strip() == "!我が母校":
            lists["utime"].append(data[0])
            lists["name"].append("NSDBOT")
            lists["message"].append('<a href ="https://www.sakura.chs.nihon-u.ac.jp/" target="_blank">here</a>')
            lists["ip"].append("NSD.NSD.NSD.NSD")
            lists["id"].append('NSD')
            lists["time"].append(data[4])
    fb.close()
    return lists
    
if __name__ == "__main__":
    if 'REQUEST_METHOD' in os.environ:
        param = cgi.FieldStorage()
        print('Content-Type: application/json\n\n')
        n = param.getfirst("n",0)
        m = param.getfirst("m",0)
        o = param.getfirst("o",0)
        ut = time.time()

        ip = 'NUL.NUL.NUL.NUL'
        id = 'NULL'
        if 'REMOTE_ADDR' in os.environ:
            ip = os.environ['REMOTE_ADDR']
            id = ''.join([format(int(ip.split('.')[i]), '02x') for i in range(4)]).upper()

        if n == "!id":
            lists = defaultdict(list)
            lists["your_id"].append(id)
            print(json.dumps(lists))
            exit(0)

        dir_name = 'logs/'
        file_name = o
        #print("名前:"+ n + "\nメッセージ:"+ m + "\n", file=sys.stderr)
        if n != "!reload" and m != "!reload" and n != "!delete" and m != "!delete":
            add_message(n,m)
            
        if n == "!delete" and m == "!delete":
            os.remove(dir_name + file_name)

        lists = defaultdict(list)
        if os.path.exists(dir_name + file_name):
            message_func(lists)
            print(json.dumps(lists))
