import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open web camera")

ESC = 27

while True:
    ret, frame = cap.read()
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == ESC:
        break

cap.release()
cv2.destroyAllWindows()
