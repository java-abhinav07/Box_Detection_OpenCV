import cv2
import numpy as np

img = cv2.imread(r"C:\Users\javaa\OneDrive\Pictures\Screenshots\spongebob.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (80, 80), (255,255,255), 1) # BGR in open cv
cv2.rectangle(img, (15, 25), (100, 50), (2, 255, 0), 7)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

pts = np.array([[10,5], [70,20], [200,30], [500,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False, (0, 255, 255), 9) # true to connect the final and initial points

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'SpongeBob', (00, 130), font, 1, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()