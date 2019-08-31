import cv2
import numpy as np
import os
from PIL import Image
import box_extraction
from matplotlib import pyplot as plt


def return_matrix(path, centre=r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\blank_template.PNG", left=r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\left_temp.PNG", right=r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\template2.PNG"):
    img_rgb = cv2.imread(path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # i, j = box_extraction.box_extraction(path, path_for_cropped_image)

    template_right = cv2.imread(right, 0)
    template_left = cv2.imread(left, 0)
    template_centre = cv2.imread(centre, 0)
    wr, hr = template_right.shape[::-1]
    wl, hl = template_left.shape[::-1]
    wc, hc = template_centre.shape[::-1]

    res_centre = cv2.matchTemplate(img_gray, template_centre, cv2.TM_CCOEFF_NORMED)
    res_right = cv2.matchTemplate(img_gray, template_right, cv2.TM_CCOEFF_NORMED)
    res_left = cv2.matchTemplate(img_gray, template_left, cv2.TM_CCOEFF_NORMED)
    threshold = 0.98
    loc_centre = np.where(res_centre >= threshold)
    loc_left = np.where(res_left >= threshold)
    loc_right = np.where(res_right >= threshold)
    lleft = []
    lright = []
    l = []

    for pt in zip(*loc_centre[::-1]):
        l.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + wc, pt[1] + hc), (0, 255, 0), 1)

    for pt in zip(*loc_right[::-1]):
        lright.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + wr, pt[1] + hr), (0, 0, 255), 1)

    for pt in zip(*loc_left[::-1]):
        lleft.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + wl, pt[1] + hl), (255, 0, 0), 1)
    count1 = 0
    count2 = 0
    # % 24 to get row number, % 80 for column change these values to adjust with the type of image given
    for i in range(len(l)):
        x = (l[i][1] // 24)
        y = (l[i][0] // 80)
        if x == 0:
            count1 += 1
        if y == 0:
            count2 += 1
        l[i] = x, y
    for i in range(len(lleft)):
        x = (lleft[i][1] // 24)
        y = (lleft[i][0] // 80)
        if x == 0:
            count1 += 1
        if y == 0:
            count2 += 1
        lleft[i] = x, y
    for i in range(len(lright)):
        x = (lright[i][1] // 24)
        y = (lright[i][0] // 80)
        if x == 0:
            count1 += 1
        if y == 0:
            count2 += 1
        lright[i] = x, y
    l.extend(lleft)
    l.extend(lright)
    final = np.ndarray([count2, count1], dtype=object)
    for coordinate in l:
        if coordinate in lleft:
            final[coordinate[0]][coordinate[1]] = '\\'
        elif coordinate in lright:
            final[coordinate[0]][coordinate[1]] = '/'
        else:
            final[coordinate[0]][coordinate[1]] = ' '

    return final

    # for debugging
    # cv2.imwrite('res.png', img_rgb)


# print(return_matrix(r"C:\Users\javaa\PycharmProjects\uas_task\Test Cases\testcase2.PNG"))












