#
#   공대선배
#   opencv python 코딩
#   카메라 연결 코드
#

import os
import cv2
from just_playback import Playback  # pip install just_playback
from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play


# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # capture라는 변수에 0번 웹캠으로부터 비디오 영상을 가져온다. 두개를 쓸경우 1로 지정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한루프
while True:
    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    cv2.imshow("original", frame)   # frame(카메라 영상)을 original 이라는 창에 띄워줌 
    
    # waitKey를 여러개 줄 경우 키가 제대로 작동하지 않는 현상 발생.
    # if cv2.waitKey(1) == ord('a'):
    #     playback1 = Playback()
    #     playback1.load_file("hi.mp3")
    # waitKey( 키 입력 대기 시간 ms) 
    # 키 입력 대기 시간
    # 함수 매개 변수로 넣는 키 입력 대기 시간은 ms 단위이고 0이면 무한대기이다.
    # 리턴 값
    # 이 함수의 리턴 값은 키보드로 입력한 키값이다.
    # 만약 리턴 값이 -1이면 입력 대기시간 동안 아무키도 눌리지 않았다는 뜻이다.
    # 리턴 값은 아스키 값과 동일하다.

    # apt install mpg123
        # file = "hi.mp3"
        # os.system("mpg123 " + file)
    #     playback1 = Playback()
    #     playback1.load_file("hi.mp3")
    #     playback1.play()
    #     playback1.stop()
    # if cv2.waitKey(1) == ord('b'):
    #     playback2 = Playback()
    #     playback2.load_file("nice_to_meet_you.mp3")
    #     playback2.play()
    #     playback2.stop()
    # if cv2.waitKey(1) == ord('c'):
    #     playback3 = Playback()
    #     playback3.load_file("hana.mp3")
    #     playback3.play()
    #     playback3.stop()
    
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break


capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌




# 실습 과정:
# 1. 카메라 연결 후, 검색에서 카메라 앱 실행 후 확인
# 2. VSCode 터미널에서 python -m venv cv_env => cv_env 라는 이름의 가상환경 구축
# 3. F1 - select interpreter - 방금 만든 가상환경 선택 - scipt - python.exe 선택
# 4. (cv_env)가 앞에 잘 붙어있으면 성공
# 5. 안된다면 (permission error)
#     5.1 검색 - powershell 관리자 권한으로 실행
#     5.2 Set-ExecutionPolicy RemoteSigned
# 6. pip install opencv-python 으로 opencv 선택
# 7. python -m pip install --upgrade pip
# 8. 코드를 실행해서 잘 나오는지 확인

# just Play_back 활용법

# from just_playback import Playback
# playback = Playback() # creates an object for managing playback of a single audio file
# playback.load_file('music-files/sample.mp3')
# # or just pass the filename directly to the constructor

# playback.play() # plays loaded audio file from the beginning
# playback.pause() # pauses playback. Has no effect if playback is already paused
# playback.resume() # resumes playback. Has no effect if playback is playing
# playback.stop() # stops playback. Has no effect if playback is not active

# playback.seek(60) # positions playback at 1 minute from the start of the audio file
# playback.set_volume(0.5) # sets the playback volume to 50% of the audio file's original value

# playback.loop_at_end(True) # since 0.1.5. Causes playback to automatically restart when it completes.

# playback.active # True if playback is active i.e playing or paused
# playback.playing # True if playback is active and not paused
# playback.curr_pos # current absolute playback position in seconds from 
# 				  #	the start of the audio file (unlike pygame.mixer.get_pos). 
# playback.paused # True if playback is paused.
# playback.duration # length of the audio file in seconds. 
# playback.volume # current playback volume
# playback.loops_at_end # True if playback is set to restart when it completes.

