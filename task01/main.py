import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open web camera")

ESC = 27

while True:
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Input', frame_gray)

    c = cv2.waitKey(1)
    if c == ESC:
        break

cap.release()
cv2.destroyAllWindows()
