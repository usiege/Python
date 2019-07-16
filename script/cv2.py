# cv2相关

import cv2
# opencv图片上画矩形框
image = cv2.imread('image.jpg')
cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
cv2.imwrite('savepath.jpg', image)
