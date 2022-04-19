import numpy as np
import cv2

img_root='Images'
img_name='ipin.jpg'

# Reading the Image
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

lowPass = cv2.filter2D(img,-1, kernel)
lowPass = img - lowPass
cv2.imshow("Low Pass",np.hstack((img, lowPass)))

highPass = img - gaussBlur
cv2.imshow("High Pass",np.hstack((img, highPass)))
cv2.waitKey(0)
cv2.destroyAllWindows()

