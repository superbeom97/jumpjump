### face_recog_id.py
### 카메라 열어서 얼굴 인식 및 신원 확인!!

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
    ## Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]       ## (y_cord_start, y_cord_end)
        roi_color = frame[y:y+h, x:x+w]

        ## recognize? deep learned model predict keras tensorflow pythorch scikit learn
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        ## 사각형 만들기
        color = (255, 0, 0) # BGR (not RGB) 0-255 -> (255, 0, 0) 에서 255는 totally blue
        stroke = 2
        end_cord_x = x + w   ## end_cord_x = width
        end_cord_y = y + h   ## end_cord_y = height
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    ## Display the resulting frame
    cv2.imshow('frame', frame)
    if (cv2.waitKey(20) & 0xFF == ord('q')):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()