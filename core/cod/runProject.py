import buildMosaic
import cv2


class PhotoTypes:
    FLOWER = 0
    PLANE = 1
    CAR = 2
    BIRD = 3
    CAT = 4
    DEER = 5
    DOG = 6
    FROG = 7
    HORSE = 8
    SHIP = 9
    TRUCK = 10

#set params for the function

#read image that will be converted into mosaic

params = {}
params['refImage'] = cv2.imread('../data/imaginiTest/poza1.jpg', cv2.IMREAD_COLOR)


params['imageType'] = 'png'

#set the number of pieces on the horizontal axis

params['numberMosaicPartsHorizontal'] = 300


params['showMosaicParts']= 0


params['arrangingWay'] = 'caroiaj'


params['criterion'] = 'distantaCuloareMedie'
params['identicalMatchingPieces'] = 1


params['category'] = PhotoTypes.DOG

imgMozaic = buildMosaic.buildMosaic(params)

cv2.imwrite('mozaic.jpg', imgMozaic)
cv2.imshow('image',imgMozaic)
#cv2.waitKey(0)


class PhotoTypes:
    FLOWER = 0
    PLANE = 1
    CAR = 2
    BIRD = 3
    CAT = 4
    DEER = 5
    DOG = 6
    FROG = 7
    HORSE = 8
    SHIP = 9
    TRUCK = 10

