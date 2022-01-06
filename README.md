# Webcam Game

## Summary
A game made using Python and OpenCV. This game uses the user's webcam and utilizes face detection in order to keep track of the user's face by drawing a red square around it while it's within the range of the webcam. Circles spawn at random positions within the game's window and the user must move their face, thereby moving their face detection square, in order to collect as many circles as they can within 60 seconds.

## Prerequisites
* [Python 3](https://www.python.org/downloads/)
* OpenCV

Once you have Python 3 installed on your machine, install OpenCV by running the following command: ```pip install opencv-python```. This will install ```numpy``` as well.

If you have both Python 2 and Python 3 on your machine, use ```pip3 install opencv-python``` instead. 

## Install
There are 2 ways for you to get Webcam Game on your machine: with [Git](https://git-scm.com/downloads) and without Git. 

### With Git
Clone the repository by running the following command: ```git clone https://github.com/saad-khannn/webcam-game.git```

### Without Git
1. Click the green "Code" dropdown button at the top of this page
2. Click "Download ZIP"
3. Unzip the folder 

## Run
To start the game, run the script by using the following command:
```python game.py```

If you used ```pip3``` to install OpenCV, use the following command instead: ```python3 game.py```

### For macOS
Open the Terminal and run ```python3 game_mac.py```

* If you get an error stating ```OpenCV: camera access has been denied```, complete the following steps: 

  1. Run ```tccutil reset Camera```
  2. Run ```python3 game_mac.py``` again
  3. You should get a pop-up which says ```"Terminal" would like to access the camera```; click "OK" 
  5. Run ```python3 game_mac.py``` one more time and this should start the game

## Instructions
There are 4 features that you must focus on while playing this game.
1. The face detection square
2. The red cirlce 
3. The timer 
4. The score

The face detection square will be shown as long as your face is clearly visible to the webcam. <br/>
The red circle spawns at a random position at the beginning of every round. Every time you collect a circle, a new circle will spawn at another random position. <br/>
The timer shows how many seconds are left for the round. Each round lasts 60 seconds. <br/>
The score shows the number of circles you have collected in the round. <br/>

To exit the game, make sure Caps Lock is turned off and press the "Q" key. 

#### Tips
* Play the game in a well-lit area. 
* Ensure that you have enough room to comfortably move around while still staying within the range of the webcam.