import loadMosaicParts
import calculateDimensions
import addMosaicParts

def buildMosaic(params):


    params = loadMosaicParts.loadMosaicParts(params)


    params = calculateDimensions.calculateDImensions(params)


    if params['arrangingWay'] == 'caroiaj':
        imgMozaic = addMosaicParts.adaugaPieseMozaicPeCaroiaj(params)
    elif params['arrangingWay'] == 'aleator':
        imgMozaic = addMosaicParts.adaugaPieseMozaicModAleator(params)
    else :
        print "Alege un mod de generare"



    return imgMozaic

