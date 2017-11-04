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
	arrangingWay = 'aleator'

	#the criterion on which the pieces will be arranged on the mozaic - 'distantaCuloareMedie' or 'aleator'
	criterion = 'distantaCuloareMedie'

	# the criterion on which we choose to stop when assigning random pieces : 'stochastic' or 'tryHard'
	# if stochastic, script will make a specific number of traversals of the matrix pixels, trying to 
	#match them all with randoms. 
	# if tryHard, script will run until all positions are filled, no exceptions. Needs lots of twitching. 
	#not running at practical speeds
	randCriterion = 'tryHard'

	# applies to stochastic randCriterion. 6 or 8 is a pretty good number, with a 95% fill rate.
	# 20 will go at almost 100% ( Avg. 30 minutes)
	nrTraversari = 1
	
	identicalMatchingPieces = 1

	#the category for the photo types
	category = PhotoTypes.FLOWER
