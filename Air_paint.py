import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 360)

detector = HandDetector(maxHands=1, detectionCon=0.7)

canvas = np.zeros((360, 720, 3), dtype=np.uint8)

xp, yp = 0, 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    
    black = np.zeros((360, 720, 3), dtype=np.uint8)

    hands, img = detector.findHands(img, draw=False)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]

        
        x1, y1 = lmList[8][0], lmList[8][1]

        fingers = detector.fingersUp(hand)

        
        if fingers[1] == 1 and fingers[2] == 0:

        
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(canvas, (xp, yp), (x1, y1), (0, 255, 0), 5)

            xp, yp = x1, y1
        else:
            xp, yp = 0, 0

        
        for point in lmList:
            x, y = point[0], point[1]
            cv2.circle(black, (x, y), 6, (255, 255, 255), cv2.FILLED)

    

    imgResult = cv2.add(black, canvas)

    cv2.imshow("Air Drawing (Dots Only)", imgResult)

    key = cv2.waitKey(1)

    if key == ord('c'):
        canvas = np.zeros((360, 720, 3), dtype=np.uint8)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Hello Git")
