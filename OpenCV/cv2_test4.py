import numpy as np
import cv2

img = cv2.imread(r"C:\Users\javaa\OneDrive\Pictures\Screenshots\spongebob.jpg", cv2.IMREAD_COLOR)

px = img[55, 55] # color val of pixel
print(px)

img[55][55] = [255,255,255]
print(px)

# Region of Image-ROI

roi = img[100:150, 100:150] = [255, 255, 255]
print(roi)

sponge_face = img[37:111, 107:194] # 74 pixels and 87 pixels
img[0:74, 0:87] = sponge_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
