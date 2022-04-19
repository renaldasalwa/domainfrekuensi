import cv2

img_root='Images'
img_name='ipin.jpg'

# Reading the Image
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

domainFilter = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6 )
cv2.imshow('Domain Filter',domainFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()