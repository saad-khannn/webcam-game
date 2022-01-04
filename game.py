import cv2
import numpy as np
import time

proto = "models/deploy.prototxt.txt"
weights = "models/res10_300x300_ssd_iter_140000.caffemodel"

net = cv2.dnn.readNetFromCaffe(proto, weights)
cap = cv2.VideoCapture(0) 
timer = 10 

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    h, w = frame.shape[:2] 
    
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0,177.0,123.0))
    net.setInput(blob) 
    faces = net.forward() 

    for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5: 
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                cv2.rectangle(frame, (x,y), (x1,y1), (0,0,255), 3)
    
    if timer > 0: 
        time.sleep(1)
        timer -= 1 
        cv2.putText(frame, str(timer), (200,h-10), 
        cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 5, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'DONE', (200,h-10), 
        cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 5, cv2.LINE_AA)
    
    cv2.imshow('webcam', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()