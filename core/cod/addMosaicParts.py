import numpy as np
from random import randint
import cv2

indexMatrix = None

def adaugaPieseMozaicPeCaroiaj(params):

    global indexMatrix
    imgMozaic = np.uint8(np.zeros(np.shape(params['imgReferintaRedimensionata'])))
    indexMatrix = [[-1 for x in range(params['numberMosaicPartsHorizontal'] + 2)] for y in range(params['numberMosaicPartsVertical'] +2)]
    indexMatrix = np.asarray(indexMatrix)

    imgMozaic = np.asarray(imgMozaic)

    [N,H,W,C] = np.shape(params['pieseMozaic'])
    [h,w,c] = np.shape(params['imgReferintaRedimensionata'])


    nrTotalPiese = params['numberMosaicPartsHorizontal'] *params['numberMosaicPartsVertical']
    nrPieseAdaugate = 0


    if params['criterion'] == 'aleator':


        for i in range(1,params['numberMosaicPartsVertical']):
            for j in range(1,params['numberMosaicPartsHorizontal']):
                #alege un indice aleator din cele N

                indice = randint(0,N-1)


                imgMozaic[(i-1)*H : i*H ,(j-1)*W : j*W, :] = \
                    params['pieseMozaic'][indice][:][:][:]



                nrPieseAdaugate = nrPieseAdaugate+1

            print ('Construim mozaic ... #2.2f## \n',100*nrPieseAdaugate/nrTotalPiese)

    elif params['criterion'] == 'distantaCuloareMedie':
        avgColorList = computeAverageColorForAList(params)
        for i in range(1,params['numberMosaicPartsVertical'] + 1):
            for j in range(1,params['numberMosaicPartsHorizontal'] + 1):

                if params['identicalMatchingPieces'] == 1:
                    indice = findAverageColor(params['imgReferintaRedimensionata'][(i-1)*H : i*H ,(j-1)*W : j*W, :]
                                              ,avgColorList)
                else :
                    indice = findAverageColor(params['imgReferintaRedimensionata'][(i-1)*H : i*H ,(j-1)*W : j*W, :]
                                          ,avgColorList,i-1,j-1)

                imgMozaic[(i-1)*H : i*H ,(j-1)*W : j*W, :] = \
                    params['pieseMozaic'][indice][:][:][:]

                nrPieseAdaugate = nrPieseAdaugate+1

            print ('Construim mozaic ...%i \% \n',100*nrPieseAdaugate/nrTotalPiese)

    else :
        print ('EROARE, optiune necunoscuta \n')

    return imgMozaic


def adaugaPieseMozaicModAleator(params) :

    imgMozaic = np.uint8(np.zeros(np.shape(params['imgReferintaRedimensionata'])))


    imgMozaic = np.asarray(imgMozaic)

    [N,H,W,C] = np.shape(params['pieseMozaic'])
    [h,w,c] = np.shape(params['imgReferintaRedimensionata'])


    nrTotalPiese = params['numberMosaicPartsHorizontal'] *params['numberMosaicPartsVertical']

    nrPieseAdaugate = 0


    if params['criterion'] == 'distantaCuloareMedie':
        avgColorList = computeAverageColorForAList(params)

        nrTraversari = 1

        rangeH = params['numberMosaicPartsVertical'] * H - H
        rangeW = params['numberMosaicPartsHorizontal'] * W - W

        numarTotalGenerari = nrTotalPiese * nrTraversari
        for i in range(0, numarTotalGenerari):

            i = randint(0,rangeH)
            j = randint(0,rangeW)

            indice = findAverageColor(params['imgReferintaRedimensionata']
                                      [i : i + H, j : j + W, :],avgColorList)


            imgMozaic[i : i + H, j : j + W, :] = \
                params['pieseMozaic'][indice][:][:][:]

            nrPieseAdaugate = nrPieseAdaugate+1

            print ('Construim mozaic \n',100*nrPieseAdaugate/numarTotalGenerari)
    else :
        print ('EROARE, optiune necunoscuta \n')

    return imgMozaic

def findAverageColor(img, avgImgList, indexH = -1, indexW = -1):

    _index = 1
    distance = float('inf')


    average_color_img = [img[:, :, i].mean() for i in range(img.shape[-1])]

    if indexW == -1 & indexH == -1 :
        id = 0
        for avg_color in avgImgList:

            dist = np.linalg.norm(np.array(average_color_img) - np.array(avg_color))
            if dist < distance :
                _index = id
                distance = dist
            id += 1
        return _index
    else :
        id = 0
        for avg_color in avgImgList:
            dist = np.linalg.norm(np.array(average_color_img) - np.array(avg_color))

            if dist < distance :

                if indexH==0 and indexW==0 :
                    _index = id
                    distance = dist
                if indexH > 0 and indexW == 0 and indexMatrix[indexH -1][indexW] != id:

                    _index = id
                    distance = dist
                elif indexH == 0 and indexW > 0 \
                        and indexMatrix[indexH ][indexW-1] != id:
                    _index = id
                    distance = dist
                elif indexH > 0 and indexW > 0 \
                        and indexMatrix[indexH -1][indexW] != id \
                        and indexMatrix[indexH][indexW-1] != id:

                    _index = id
                    distance = dist

            id += 1

        indexMatrix[indexH][indexW] = _index

        return _index


def computeAverageColorForAList(params):

    [N,H,W,C] = np.shape(params['pieseMozaic'])
    average_color = []

    for i in range(0,N - 1):

            image = params['pieseMozaic'][i][:][:][:]
            avg_color = [image[:, :, i].mean() for i in range(image.shape[-1])]

            average_color.append(avg_color)

    return average_color