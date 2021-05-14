import time
import base64

import redis
import cv2

publisher = redis.Redis(host='localhost', port=6379)

# set below env var for udp in terminal
# export OPENCV_FFMPEG_CAPTURE_OPTIONS="rtsp_transport;udp"
cap = cv2.VideoCapture("rtsp://localhost:8554/vid")

while cap.isOpened():
    _, frame = cap.read()

    # send frame as base 64
    _, buffer = cv2.imencode('.jpg', frame) 
    image_str = base64.b64encode(buffer)

    publisher.publish('vid', image_str)

cap.release()
cv2.destroyAllWindows()
