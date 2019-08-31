import cv2
import numpy as np
import os
from PIL import Image
import box_extraction
from matplotlib import pyplot as plt


def match_template(img_path, left=r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\left_temp.PNG", right=r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\template2.PNG"):
    img_rgb = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template_right = cv2.imread(right, 0)
    template_left = cv2.imread(left, 0)
    wr, hr = template_right.shape[::-1]
    wl, hl = template_left.shape[::-1]

    res_right = cv2.matchTemplate(img_gray, template_right, cv2.TM_CCOEFF_NORMED)
    res_left = cv2.matchTemplate(img_gray, template_left, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc_right = np.where(res_right >= threshold)

    for pt in zip(*loc_right[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + wr, pt[1] + hr), (0, 0, 255), 1)

    loc_left = np.where(res_left >= threshold)
    for pt in zip(*loc_left[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + wl, pt[1] + hl), (255, 0, 0), 1)

    # for debugging
    cv2.imwrite('res.png', img_rgb)


