#
#   공대선배
#   opencv python 코딩
#   화면에 글자 출력 코드
#

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image # pillow 라이브러리로 부터 세개의 모듈을 사용하겠다. 
import numpy as np

# PIL을 열기위해서 pip install pillow 로 하면 설치가 되는데..
# python -m pip install --upgrade pip
# python -m pip install --upgrade pillow
# 위의 방법들로 안되어서 관리자 권한으로도 실행해 봤는데도 해결이 안됨.
# pyton -m pip install pillow 를 이용하여 라이브러리 설치 성공.
# 이유 : 경로때문에 발생하는 오류 Fatal error in launcher: Unable to create process using

# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # 0번 카메라를 불러온다. 카메라가 여러대일 경우 1, 2 .. 한대일 경우 0
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 글꼴파일을 불러옴
font = ImageFont.truetype('fonts/SCDream6.otf', 20) # ImageFont.truetype(불러올 폰트 경로, 글자크기)

# 무한루프
while True:
    # 현재시각을 불러와 문자열로저장
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') # string format time 시간을 문자열 형태로 저장해준다.

    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점 = 딱 맞는 위치를 잡기 위해서는 어느 정도의 노가다가 필요하다., color는 색상(파랑,초록,빨강), tickness는 선굵기(-1은 내부를 채우는 것)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)
    
    # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
    frame = Image.fromarray(frame)    
    draw = ImageDraw.Draw(frame)    
    # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
    draw.text(xy=(10, 15),  text= "공대선배 웹캠 " + nowDatetime, font=font, fill=(255, 255, 255))
    frame = np.array(frame)

    cv2.imshow("text", frame)   # text라는 이름의 현재 시간을 표시하는 글자를 써준 영상 출력
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break

capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌