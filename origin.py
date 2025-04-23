import cv2
import numpy as np

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)

# Set frame size
frameWidth = 640
frameHeight = 480

# Open webcam (0 for built-in, 1 for external)
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Define HSV color ranges and corresponding BGR values
myColors = [[5, 107, 0, 19, 255, 255],  # Orange
            [133, 56, 0, 159, 156, 255],  # Purple
            [57, 76, 0, 100, 255, 255],  # Green
            [90, 48, 0, 118, 255, 255]]  # Blue

myColorValues = [[51, 153, 255],  # BGR for drawing
                 [255, 0, 255],
                 [0, 255, 0],
                 [255, 0, 0]]

myPoints = []  # [x, y, colorId]


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
            cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
        count += 1
    return newPoints


def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

            # Shape recognition
            if len(approx) == 3:
                shape = "Triangle"
            elif len(approx) == 4:
                # Check for rectangle or square
                aspectRatio = float(w) / h
                shape = "Square" if 0.95 <= aspectRatio <= 1.05 else "Rectangle"
            elif len(approx) == 5:
                shape = "Pentagon"
            elif len(approx) == 6:
                shape = "Hexagon"
            else:
                shape = "Circle"

            # Draw the contour and the shape name
            cv2.drawContours(imgResult, [approx], -1, (0, 255, 0), 3)
            cv2.putText(imgResult, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    if not success:
        break
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if newPoints:
        myPoints.extend(newPoints)
    if myPoints:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()
