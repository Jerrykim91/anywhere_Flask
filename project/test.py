# 슬렉 메세지 
import requests
from slacker import Slacker
from datetime import datetime



def postMsg(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers = {"Authorization": "Bearer "+token},
        data    = {"channel": channel,"text": text})
 

def timeTracker(msg):
    """ message를 파이썬 로그와 슬랙으로 동시에 값을 전달 """
    
    timeTkr = datetime.now().strftime('[%m/%d %H:%M:%S] ') + msg
    print(timeTkr)
    postMsg(myToken,"#alarm",timeTkr)
    10

import time
if __name__ == "__main__":
    
    now = datetime.now()
    print('현재 시간',now)
    t = '테스트_Chatbat'
    timeTracker(t)
    custm = input('분 단위 입력:')
    custm_sec = int(custm)*60 # 입력한 시간 
    sec = custm_sec
    print(custm_sec)
    
    
    #while은 반복문으로 sec가 0이 되면 반복을 멈춰라
    while (sec != 0 ):
        sec = sec-1
        time.sleep(0.99)
        if sec == 0:
            timeTracker(t)
            print('종료')
        elif sec < 16:
            print(sec)
            
    print(time.time())
        

    # timeTracker(t)

    # 추가할 기능 


# def countdown(num_of_secs):
#     while num_of_secs:
#         m, s = divmod(num_of_secs, 60)
#         min_sec_format = '{:02d}:{:02d}'.format(m, s)
#         print(min_sec_format, end='/r')
#         time.sleep(1)
#         num_of_secs -= 1
        
#     print('Countdown finished.')

# inp = input('Input number of seconds to countdown: ')
# countdown(inp)



# 슬랙 알람 설정 방법을 설정하고 작업에 임해야 한다. 
# 슬랙 -> 내가 사용하고자 하는 채널 '#ai' -> 이 채널에 모든 멤버 보기 -> 통합 -> 앱 -> 만들어둔 읽고 쓰는 앱을 클릭 