import cv2
import numpy as np


# + 나 *를 쓰지 않고 cv2.add, cv2.multiply를 쓰는 이유 : + 나 * 사용시 255값을 넘어가게되면, overflow가 일어나 값이 0이 되고, 검은색이 나오게 된다.
# add 나 multiply를 쓰게되면 255값을 넘지 않게 자동으로 조정해준다.

# 색감 변경 함수
def color_filter(img, color, scale):    # 입력변수는 영상, 변경할 색상, 변경할 비율
    dst = np.array(img, np.uint8)       # 입력 영상과 같은 영상을 복사
    if color == 'blue' or color == 0:   # 색상이 파란색이라면
        dst[:, :, 0] = cv2.multiply(dst[:, :, 0], scale)    # 세로, 가로 모든열 영상중 파란색의 비율을 바꿔줌
    elif color == 'green' or color == 1:    # 색상이 초록색이라면
        dst[:, :, 1] = cv2.multiply(dst[:, :, 1], scale)    # 영상중 초록색의 비율을 바꿔줌
    if color == 'red' or color == 2:    # 색상이 빨간색이라면
        dst[:, :, 2] = cv2.multiply(dst[:, :, 2], scale)    # 영상중 빨간색의 비율을 바꿔줌
    return dst      # 처리된 영상을 반환

# 밝기 변경 함수
def set_brightness(img, scale):         # 입력변수는 영상, 밝기를 변경할 값
    return cv2.add(img, scale)          # 전체 픽셀값에 scale을 더하여 밝기를 변경

# 대비 변경 함수 - 색상 히스토그램 영역을 넓게 펴준다. =  색상이  
# 색 대비를 증가시키거나 감소시켜주는 함수(img의 색대비를 scale만큼 변화
def set_contrast(img, scale):           # 입력변수는 영상, 대비를 변경할 값
    return np.uint8(np.clip((1 + scale) * img - 128 * scale, 0, 255))   # 대비를 scale 비율로 변환

# 이미지 크기 변경 함수 - img의 크기를 scale만큼 변화
def set_size(img, scale):
    return cv2.resize(img, dsize=(int(img.shape[1]*scale), int(img.shape[0]*scale)), interpolation=cv2.INTER_AREA)

# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)