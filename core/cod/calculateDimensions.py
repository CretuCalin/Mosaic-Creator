import numpy as np
import cv2
from params import Params

def calculateDimensions():
    [piesaH,piesaW,canal] = \
        np.shape(Params.pieseMozaic[0])
    [refH,refW,canal] = np.shape(Params.refImage)

    rezW = Params.numberMosaicPartsHorizontal*piesaW
    scara = rezW / refW
    rezH = refH*scara
    
    Params.numberMosaicPartsVertical = int (np.floor(rezH/piesaH))
    H = Params.numberMosaicPartsVertical * piesaH
    W = Params.numberMosaicPartsHorizontal * piesaW
    Params.imgReferintaRedimensionata = cv2.resize(Params.refImage, (W,H))
