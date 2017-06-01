import cv2
import sys

imgFile = "images\christopher-burns-189796.jpg" if len(sys.argv) <= 1 else sys.argv[1]
image = cv2.imread(imgFile)
print image.shape
rSize = 1000
r = float(rSize) / image.shape[1]
dim = (rSize, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)

