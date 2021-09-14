from flask import Flask, request, render_template, send_file

import os
import json
import joblib

# 슬렉 메세지 
import time
import requests
from slacker import Slacker
from datetime import datetime


server = Flask(__name__)
lot_num = datetime.today().strftime("%Y.%m.%d %H:%M:%S")

"""
금리, 환률, 코스피, 코스탁 정보 
"""

def postMsg(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers = {"Authorization": "Bearer "+token},
        data    = {"channel": channel,"text": text})
 

def timeTracker(msg , myToken):
    """ message를 파이썬 로그와 슬랙으로 동시에 값을 전달 """
    
    timeTkr = datetime.now().strftime('[%m/%d %H:%M:%S] ') + msg
    print(timeTkr)
    postMsg(myToken,"#alarm",timeTkr)



@ server.route("/", methods=['GET', 'POST'])  # page path setting
def index():
    if request.method == 'GET':
        # print(lot_num)
        date = datetime.now().strftime("%Y.%m.%d")
        times = 0 # 실시간 원함
        # timeTracker(msg , myToken)
        return render_template('index.html',date=date)

    if request.method == 'POST':
        myToken = 0
        custm_min = 0 # 분단위 입력
        sec = int(custm_min)*60

        #while은 반복문으로 sec가 0이 되면 반복을 멈춰라
        while (sec != 0 ):
            sec = sec-1
            time.sleep(0.99)
            if sec == 0:
                timeTracker(msg) #  msg 입력? - msg
                print('종료')
            elif sec < 16:
                print(sec)
                
        print(time.time())

        return render_template('post.html')

@ server.route("/demo", methods=['GET', 'POST'])  # page path setting
def demo():
    if request.method == 'GET':
        print(lot_num)
        return render_template('demo.html')


if __name__ == "__main__":
    
    server.run(debug=True, host="172.30.1.56", port=5000)
    
