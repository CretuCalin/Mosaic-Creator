import numpy as np
from random import randint
import cv2
from params import Params

indexMatrix = None

def adaugaPieseMozaicPeCaroiaj():

    global indexMatrix
    imgMozaic = np.uint8(np.zeros(np.shape(Params.imgReferintaRedimensionata)))
    indexMatrix = [[-1 for x in range(Params.numberMosaicPartsHorizontal + 2)] for y in range(Params.numberMosaicPartsVertical + 2)]
    indexMatrix = np.asarray(indexMatrix)

    imgMozaic = np.asarray(imgMozaic)

    [N,H,W,C] = np.shape(Params.pieseMozaic)
    [h,w,c] = np.shape(Params.imgReferintaRedimensionata)


    nrTotalPiese = Params.numberMosaicPartsHorizontal * Params.numberMosaicPartsVertical
    nrPieseAdaugate = 0


    if Params.criterion == 'aleator':


        for i in range(1,Params.numberMosaicPartsVertical):
            for j in range(1,Params.numberMosaicPartsHorizontal):
                #alege un indice aleator din cele N

                indice = randint(0,N-1)


                imgMozaic[(i-1)*H : i*H ,(j-1)*W : j*W, :] = \
                    Params.pieseMozaic[indice][:][:][:]


 
                nrPieseAdaugate = nrPieseAdaugate+1

            print ("Construim mozaic ... #2.2f## \n",100*nrPieseAdaugate/nrTotalPiese)

    elif Params.criterion == 'distantaCuloareMedie':
        avgColorList = computeAverageColorForAList()
        for i in range(1,Params.numberMosaicPartsVertical + 1):
            for j in range(1,Params.numberMosaicPartsHorizontal + 1):

                if Params.identicalMatchingPieces == 1:
                    indice = findAverageColor(Params.imgReferintaRedimensionata[(i-1)*H : i*H ,(j-1)*W : j*W, :]
                                              ,avgColorList)
                else :
                    indice = findAverageColor(Params.imgReferintaRedimensionata[(i-1)*H : i*H ,(j-1)*W : j*W, :]
                                          ,avgColorList,i-1,j-1)

                imgMozaic[(i-1)*H : i*H ,(j-1)*W : j*W, :] = \
                    Params.pieseMozaic[indice][:][:][:]

                nrPieseAdaugate = nrPieseAdaugate+1

            print ("Construim mozaic ...%i % \n",100*nrPieseAdaugate/nrTotalPiese)

    else :
        print ("EROARE, optiune necunoscuta \n")

    return imgMozaic

def adaugaPieseMozaicModAleator() :

    imgMozaic = np.uint8(np.zeros(np.shape(Params.imgReferintaRedimensionata)))

    imgMozaic = np.asarray(imgMozaic)

    [N,H,W,C] = np.shape(Params.pieseMozaic)
    [h,w,c] = np.shape(Params.imgReferintaRedimensionata)

    nrPieseAdaugate = 0

    avgColorList = computeAverageColorForAList()

    nrTraversari = Params.nrTraversari

    rangeH = h - H
    rangeW = w - W

    if Params.randCriterion == 'tryHard':
        
        mozaicEmpty = {(row * rangeW + col) : (row,col) for row in range(0,rangeH) for col in range(0,rangeW)}

        pixelsToFill = rangeH * rangeW

        while mozaicEmpty :


            #get a random block to fill from the empty blocks list
            randomIndex = randint(0,pixelsToFill)

            if randomIndex not in mozaicEmpty:
                continue

            (i, j) = mozaicEmpty[randomIndex]

            indice = findAverageColor(Params.imgReferintaRedimensionata
                                      [i : i + H, j : j + W, :],avgColorList)

            imgMozaic[i : i + H, j : j + W, :] = \
                Params.pieseMozaic[indice][:][:][:]

            #mark the previously empty block as full
            for row in range(i ,(i + H + 1)) :
                for col in range(j, (j + W + 1)) :
                    if randomIndex in mozaicEmpty :
                        del(mozaicEmpty[randomIndex])

            print("Construim mozaic \n", len(mozaicEmpty) )

    elif Params.randCriterion == 'stochastic':

        nrTotalPiese = Params.numberMosaicPartsHorizontal * Params.numberMosaicPartsVertical

        numarTotalGenerari = nrTotalPiese * nrTraversari

        for i in range(0, numarTotalGenerari):

            i = randint(0,rangeH)
            j = randint(0,rangeW)

            indice = findAverageColor(Params.imgReferintaRedimensionata
                                      [i : i + H, j : j + W, :],avgColorList)

            imgMozaic[i : i + H, j : j + W, :] = \
                Params.pieseMozaic[indice][:][:][:]

            nrPieseAdaugate = nrPieseAdaugate + 1

            print ("Construim mozaic \n",100*nrPieseAdaugate/numarTotalGenerari)
    else :
        print ("EROARE, optiune necunoscuta \n")

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

def computeAverageColorForAList():

    [N,H,W,C] = np.shape(Params.pieseMozaic)
    average_color = []

    for i in range(0,N - 1):

            image = Params.pieseMozaic[i][:][:][:]
            avg_color = [image[:, :, i].mean() for i in range(image.shape[-1])]

            average_color.append(avg_color)

    return average_color