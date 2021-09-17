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
import glob

if __name__ == "__main__":
    if 'REQUEST_METHOD' in os.environ:
        param = cgi.FieldStorage()
        print('Content-Type: application/json\n\n')
        n = param.getfirst("n",0)
        m = param.getfirst("m",0)
        ut = time.time()
        
        log_dir_name = 'logs/'
        html_dir_name = '/usr/local/apache2/htdocs/chats/'
        file_name = ''
        if n == 0:
                file_name = 'おととい来やがれ'
        else:
                file_name = n
        #print("名前:"+ n + "\nメッセージ:"+ m + "\n", file=sys.stderr)
        lists = defaultdict(list)
        lists["mode"].append(m)
        if m == "!create":            
            with open(log_dir_name + file_name, mode="a") as f:
                pass
            with open(html_dir_name + file_name + '.html', mode="w") as f:
                lines = """<!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset = "utf-8" />
        <title>西田研究議会モスクワ支部 会議室</title>
        <link rel="icon" type="image/x-icon" href="/img/nishidicon.jpg">
    </head>

    <body bgcolor="#FFC7AF" text="#000000">
        <h1>西田研究議会モスクワ支部 (Ver: 0.0.1 cgi)<br>
            Исследовательский Совет Нисиды Московский Отделение(Вер: 0.0.1 cgi)</h1>
        <a href="/"><img src="/img/top.png" alt="トップ"></a>
        <br />
        <a href="/handle_chat.html">ルーム一覧</a>
        <br /><h1>""" + file_name + """</h1>
        <div id = "id"></div>
        NAME
        <input type="text" id="name" autocomplete="off">
        <br />
        MESSAGE
        <input type="text" id="message" autocomplete="off">
        <button type="button" id="submit" value="送信" disabled>送信</button>
        <br />
        <button type="button" id="delete" value="メッセージクリア">チャット内容クリア</button>
        <br />        
        Comannds: !now !我が母校 !zn,n∈N !Z
        <p id="error"></p>
        <h2>-CHAT LOG-</h2>
        <div id = "content"></div>
        <script type="text/javascript">
        var room_name = '""" + file_name + """';
        </script>
        <script type="text/javascript" src="chat.js"></script>
    </body>

    </html>"""
                f.write(lines)              
            lists["new_room"].append(file_name)                

        elif m == "!delete":
            if os.path.exists(log_dir_name + file_name) and os.path.exists(html_dir_name + file_name + '.html'):
                os.remove(log_dir_name + file_name)            
                os.remove(html_dir_name + file_name + '.html')
                lists["deleting_room"].append(file_name)  
            else:
                lists["deleting_room"].append('')  

        elif m == "!search":
            for r in glob.glob(log_dir_name + '*'):
                if (n.lower() in r.lower()):
                    lists["searching_room"].append(os.path.basename(r))               

        elif m == "!show":            
            for r in glob.glob(log_dir_name + '*'):
                lists["rooms"].append(os.path.basename(r).encode(errors="surrogateescape").decode())

        print(json.dumps(lists))
