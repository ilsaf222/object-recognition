from asyncio.windows_events import NULL
from cProfile import label
from itertools import count
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2
import os

mode = 0
prototxt = "MobileNetSSD_deploy.prototxt.txt"
model = "MobileNetSSD_deploy.caffemodel"
defaultConfidence = 0.2
imageName = "bird.jpg"
imagesFolderURL = "all"

def detect(frame):
    label = 0
    (h, w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > defaultConfidence:
            print(detections)
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = f"{CLASSES[idx]} {round(confidence * 100, 2)}%"

            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    return [frame, label]


CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "tree", "sheep",
           "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
net = cv2.dnn.readNetFromCaffe(prototxt, model)

if(mode == 0):
    frame = cv2.imread(imageName)
    frame = detect(frame)
    cv2.imwrite(f"detected\{imageName}-{frame[1]}.jpg", frame[0])

elif(mode == 1):
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    fps = FPS().start()
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=700)

        frame = detect(frame)

        cv2.imshow("Frame", frame[0])
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        fps.update()

    fps.stop()
    vs.stop()

elif(mode == 2):
    for filename in os.listdir(imagesFolderURL):
        frame = cv2.imread(f"{imagesFolderURL}\{filename}")
        frame = detect(frame)
        labelText = ""
        if(frame[1] != 0):
            labelText = frame[1]
        else:
            labelText = "Undefined"
        urlStr = f"sortedImg\{filename}-{labelText}.jpg"
        cv2.imwrite(urlStr, frame[0])
        #cv2.imwrite(f"detected\{labelText}.jpg", frame[0])

cv2.destroyAllWindows()
print("FINISHED")      

