from filecmp import cmp
import cv2
import matplotlib.pyplot as plt
# open cv 설치
# pip install opencv-python

img = cv2.imread("D:\\poly.bmp", cv2.IMREAD_GRAYSCALE)



plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()
#cv2.waitKey(0)


#cv2.imshow("img", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()