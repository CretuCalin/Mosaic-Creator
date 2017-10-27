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


class Params(object):		
	###class for storing parameters of the script ###

	#read image that will be converted into mosaic
	refImagePath = '../data/imaginiTest/ferrari.jpeg'

	#refImage will be read by cv2.imread in the main runProject script
	refImage = [[]]

	#set the small image types
	imageType = 'png'

	#set the number of pieces on the horizontal axis
	numberMosaicPartsHorizontal = 100
	
	#if 1, script will show the mozaic photo pieces
	showMosaicParts= 0

	#how the pieces will be arranged on the mozaic - 'caroiaj' or 'aleator'
	arrangingWay = 'caroiaj'

	#the criterion on which the pieces will be arranged on the mozaic - 'distantaCuloareMedie' or 'aleator'
	criterion = 'distantaCuloareMedie'
	
	identicalMatchingPieces = 1

	#the category for the photo types
	category = PhotoTypes.FLOWER
