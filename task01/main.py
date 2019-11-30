import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open web camera")

ESC = 27


def draw_circle(x, frame):
    cv2.circle(frame, center=(int(x[1]), int(x[0])), radius=5, color=[0, 0, 255], thickness=-1)


while True:
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_gray = np.float32(frame_gray)
    dst = cv2.cornerHarris(frame_gray, 2, 3, 0.04)

    idx1, idx2 = np.where(dst > 0.01 * dst.max())
    index = np.column_stack((idx1, idx2))

    np.apply_along_axis(lambda row: draw_circle(row, frame), axis=1, arr=index)

    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == ESC:
        break

cap.release()
cv2.destroyAllWindows()
