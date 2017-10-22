import numpy as np
import cv2

def calculateDImensions(params):



    [piesaH,piesaW,canal] = \
        np.shape(params['pieseMozaic'][0])
    [refH,refW,canal] = np.shape(params['refImage'])

    rezW = params['numberMosaicPartsHorizontal']*piesaW
    scara = rezW / refW
    rezH = refH*scara
    
    params['numberMosaicPartsVertical'] = int (np.floor(rezH/piesaH))
    H = params['numberMosaicPartsVertical'] * piesaH
    W = params['numberMosaicPartsHorizontal'] * piesaW
    params['imgReferintaRedimensionata'] = cv2.resize(params['refImage'], (W,H))


    return params