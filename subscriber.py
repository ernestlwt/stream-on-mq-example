import time
import base64

import cv2
import numpy as np
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
subscriber = r.pubsub()

subscriber.subscribe('vid')
subscriber.get_message()

while True:
    message = subscriber.get_message()
    if message and not message['data'] == 1:
        image_str = message['data']
        buffer = base64.b64decode(image_str)
        buffer = np.frombuffer(buffer, dtype=np.uint8)
        frame = cv2.imdecode(buffer, flags=1)
        cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()