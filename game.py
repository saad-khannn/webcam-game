import cv2
import numpy as np
import time
from random import randrange

proto = "models/deploy.prototxt.txt" 
weights = "models/res10_300x300_ssd_iter_140000.caffemodel" 

net = cv2.dnn.readNetFromCaffe(proto, weights) 
cap = cv2.VideoCapture(0) 
start = time.time() 

coordinates = False
score = 0 

def circleHit(rectX1, rectY1, rectX2, rectY2, circleWidth, circleHeight):
    xRange = range(rectX1, rectX2) 
    yRange = range(rectY1, rectY2) 
    if((circleWidth in xRange) and (circleHeight in yRange)):
        return True

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    h, w = frame.shape[:2] 
    frame[0:40, 0:w] = (0,0,0)

    blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0,177.0,123.0))
    net.setInput(blob)
    faces = net.forward() 

    for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5: 
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x1, y1, x2, y2) = box.astype("int")
                face = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 3)

    end = time.time() 
    elapsed = end - start 
    timer = int(60 - elapsed) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    if timer > 0:
        cv2.putText(frame, 'Timer:' + str(timer), (5,30), font, 1, (255,255,255), 1, cv2.LINE_AA)
        if coordinates == False:
            h, w = frame.shape[:2] 
            randomWidth = randrange(30, w-30)
            randomHeight = randrange(70, h-30)
            coordinates = (randomWidth, randomHeight)
        circle = cv2.circle(frame, coordinates, 30, (0,0,255), -1) 
        if circleHit(x1, y1, x2, y2, coordinates[0], coordinates[1]):
            score += 1
    else:
        cv2.putText(frame, 'ROUND OVER', (5,30), 
        font, 1, (255,255,255), 2, cv2.LINE_AA)
    
    cv2.putText(frame, 'Score:' + str(score), 
    (int(w*0.72),30), font, 1, (255,255,255), 1, cv2.LINE_AA)

    cv2.imshow('webcam', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()