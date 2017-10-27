import loadMosaicParts
import calculateDimensions
import addMosaicParts
from params import Params

def buildMosaic():

    loadMosaicParts.loadMosaicParts()

    calculateDimensions.calculateDimensions()

    if Params.arrangingWay == 'caroiaj':
        imgMozaic = addMosaicParts.adaugaPieseMozaicPeCaroiaj()
    elif params.arrangingWay == 'aleator':
        imgMozaic = addMosaicParts.adaugaPieseMozaicModAleator()
    else :
        print "Alege un mod de generare"

    return imgMozaic

