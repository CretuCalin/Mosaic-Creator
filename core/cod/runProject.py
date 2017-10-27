import buildMosaic
from params import Params
import cv2

Params.refImage = cv2.imread(Params.refImagePath, cv2.IMREAD_COLOR)

imgMozaic = buildMosaic.buildMosaic()

cv2.imwrite('mozaic.jpg', imgMozaic)
cv2.imshow('image',imgMozaic)
cv2.waitKey(0)

