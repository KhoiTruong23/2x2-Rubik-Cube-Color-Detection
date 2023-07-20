import cv2
import numpy as np
colors = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
square_positions = [(250, 150), (325, 150), (250, 225), (325, 225)]
thickness = 2
cap = cv2.VideoCapture(0)
square_1 = np.float32([[260, 160], [260+20, 160], [260, 160+20], [260+20, 160+20]])
square_2 = np.float32([[335, 160], [335+20, 160], [335, 160+20], [335+20, 160+20]])
square_3 = np.float32([[260, 235], [260+20, 235], [260, 235+20], [260+20, 235+20]])
square_4 = np.float32([[335, 235], [335+20, 235], [335, 235+20], [335+20, 235+20]])
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
color = (0, 255, 0)
thickness1 = 20
text = "OpenCV"

def output_color(frame, k, square):
    arr=np.round(square[0]).astype(int)
    org=tuple(arr)
    if k == 1:
        print("blue")
        cv2.putText(frame, 'blue', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    if k == 2:
        print("orange")
        cv2.putText(frame, 'orange', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (40,103,255), 2)
    if k == 3:
        print("white")
        cv2.putText(frame, 'white', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    if k == 4:
        print("green")
        cv2.putText(frame, 'green', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    if k == 5:
        print("red")
        cv2.putText(frame, 'red', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    if k == 6:
        print("yellow")
        cv2.putText(frame, 'yellow', org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20, 251, 255), 2)
    if k == 7:
        print("fail")

def getWarp(frame, square):
    rect_coords = np.float32([[0, 0], [20, 0], [0, 20], [20, 20]])
    M1 = cv2.getPerspectiveTransform(square, rect_coords)
    square_1_check = cv2.warpPerspective(frame, M1, (20, 20))
    return square_1_check

def draw_squares(frame):
    for i in range(len(square_positions)):
        x, y = square_positions[i]
        color = colors[i]
        cv2.rectangle(frame, (x, y), (x+37, y+37), color, thickness)

def check(orange_hsv,white_hsv,green_hsv,red_hsv,yellow_hsv,blue_hsv,img_test):
    diff_orange = np.absolute(orange_hsv - img_test)
    diff_white = np.absolute(white_hsv - img_test)
    diff_green = np.absolute(green_hsv - img_test)
    diff_red = np.absolute(red_hsv - img_test)
    diff_yellow = np.absolute(yellow_hsv - img_test)
    diff_blue = np.absolute(blue_hsv - img_test)
    for x in range(width-1):
     for y in range(height-1):
        if(diff_blue[y,x,0]>250) or (diff_blue[y,x,0]<10):
            return 1
        if (diff_red[y, x, 0] > 250) or (diff_red[y, x, 0] < 10):
            return 5
        if(diff_orange[y,x,0]>250) or (diff_orange[y,x,0]<10):
                return 2
        if(diff_white[y,x,0]>250) or (diff_white[y,x,0]<10):
            return 3
        if (diff_green[y, x, 0] > 250) or (diff_green[y, x, 0] <10):
            return 4
        if (diff_yellow[y, x, 0] > 250) or (diff_yellow[y, x, 0] <10):
            return 6
        else: return 7

while True:
 ret, frame = cap.read()
 img_test1 = getWarp(frame, square_1)
 img_test2 = getWarp(frame, square_2)
 img_test3 = getWarp(frame, square_3)
 img_test4 = getWarp(frame, square_4)
 img_test1 = cv2.cvtColor(img_test1,cv2.COLOR_BGR2HSV)
 img_test2 = cv2.cvtColor(img_test2,cv2.COLOR_BGR2HSV)
 img_test3 = cv2.cvtColor(img_test3,cv2.COLOR_BGR2HSV)
 img_test4 = cv2.cvtColor(img_test4,cv2.COLOR_BGR2HSV)
 height, width = img_test1.shape[:2]
 ####
 yellow = np.zeros((300, 300, 3), dtype="uint8")
 yellow[:] = (20, 251, 255) # Set the color to yellow
 yellow=cv2.resize(yellow,(width,height))
 yellow_hsv = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
 ####
 blue = np.zeros((300, 300, 3), dtype="uint8")
 blue[:] = (175, 88, 0)  # Set the color to yellow
 blue = cv2.resize(blue, (width, height))
 blue_hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
 ####
 green = np.zeros((300, 300, 3), dtype="uint8")
 green[:] = (106, 209, 0)  # Set the color to yellow
 green = cv2.resize(green, (width, height))
 green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
 ####
 red = np.zeros((300, 300, 3), dtype="uint8")
 red[:] = (59, 54, 217)  # Set the color to yellow
 red = cv2.resize(red, (width, height))
 red_hsv = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
 ####
 white = np.zeros((300, 300, 3), dtype="uint8")
 white[:] = (215, 198, 193)  # Set the color to yellow
 white = cv2.resize(white, (width, height))
 white_hsv = cv2.cvtColor(white, cv2.COLOR_BGR2HSV)
 ####
 orange = np.zeros((300, 300, 3), dtype="uint8")
 orange[:] = (40,103,255)  # Set the color to yellow
 orange = cv2.resize(orange, (width, height))
 orange_hsv= cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
 ####
 k1=check(orange_hsv,white_hsv,green_hsv,red_hsv,yellow_hsv,blue_hsv,img_test1)
 k2=check(orange_hsv, white_hsv, green_hsv, red_hsv, yellow_hsv, blue_hsv, img_test2)
 k3=check(orange_hsv, white_hsv, green_hsv, red_hsv, yellow_hsv, blue_hsv, img_test3)
 k4=check(orange_hsv, white_hsv, green_hsv, red_hsv, yellow_hsv, blue_hsv, img_test4)
 if ret:
     draw_squares(frame)
     output_color(frame, k1, square_1)
     output_color(frame, k2, square_2)
     output_color(frame, k3, square_3)
     output_color(frame, k4, square_4)
     cv2.imshow('Video', frame)

 cv2.waitKey(1)