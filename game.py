import cv2
import numpy as np
import time
from random import randrange

proto = "models/deploy.prototxt.txt" #model definition
weights = "models/res10_300x300_ssd_iter_140000.caffemodel" #trained model
net = cv2.dnn.readNetFromCaffe(proto, weights) #load network

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #record webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #set webcam window width to 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #set webcam window height to 480

start = time.time() #constant start time
coordinates = False #no coordinates for circle at start
score = 0 #keep score
x1, y1, x2, y2 = 0, 0, 1, 1 #initialize face detection box position variables 

def circleHit(rectX1, rectY1, rectX2, rectY2, circleWidth, circleHeight):
    width = range(circleWidth - 25, circleWidth + 25) #account for circle width
    height = range(circleHeight - 25, circleHeight + 25) #account for circle height
    xRange = range(rectX1, rectX2) #face detection box width
    yRange = range(rectY1, rectY2) #face detection box height
    #if face detection box is within range of the circle
    if(range(max(width[0], xRange[0]), min(width[-1], xRange[-1])) 
    and range(max(height[0], yRange[0]), min(height[-1], yRange[-1]))):
        return True 

while True:
    ret, frame = cap.read() #get live feed from webcam
    frame = cv2.flip(frame, 1) #flip/mirror webcam video across y-axis
    height, width = frame.shape[:2] #height and width of window
    #top 40 pixels of the screen are all black to show white text of timer and score
    frame[0:40, 0:width] = (0, 0, 0)
    
    #create 4d blob for each frame received from webcam
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0)) 
    net.setInput(blob) #pass blob to network
    faces = net.forward() #receive face detections
    for i in range(faces.shape[2]):
        confidence = faces[0, 0, i, 2]
        if confidence > 0.5: #if confidence is higher than 50%
            box = faces[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x1, y1, x2, y2) = box.astype("int")
            face = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3) #draw face detection box

    end = time.time() #incrementing end time
    elapsed = end - start #time elapsed in seconds
    timer = int(60 - elapsed) #countdown timer
    font = cv2.FONT_HERSHEY_SIMPLEX
    if timer > 0:
        cv2.putText(frame, 'Timer:' + str(timer), (5, 30), font, 1, (255, 255, 255), 1, cv2.LINE_AA) #show timer
        if coordinates == False: #get random coordinates for circle
            randomWidth = randrange(25, width - 25)
            randomHeight = randrange(65, height - 25)
            coordinates = (randomWidth, randomHeight) #random position in window
        circle = cv2.circle(frame, coordinates, 25, (0, 0, 255), -1) #draw circle at random position
        if circleHit(x1, y1, x2, y2, coordinates[0], coordinates[1]): #if face detection box hits circle
            coordinates = False #new random position for circle
            score += 1 #increase score when face detection box hits circle
    else:
        #show "game over" text when timer reaches 0
        cv2.putText(frame, "GAME OVER", (5, 30), font, 1, (255, 255, 255), 3, cv2.LINE_AA)
        #show score text with bold weight when round ends 
        cv2.putText(frame, 'Score:' + str(score), (int(width * 0.74), 30), font, 1, (255, 255, 255), 3, cv2.LINE_AA) 
    #show score with normal weight when round is ongoing
    cv2.putText(frame, 'Score:' + str(score), (int(width * 0.74), 30), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('webcam', frame) #show webcam window
    if cv2.waitKey(1) == ord('q'): #press 'q' to close window/game
        break

cap.release() 
cv2.destroyAllWindows()