import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture


os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture("DAMBALASIK 住所確認 v3.2")

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

cv.destroyAllWindows()
print("done")
