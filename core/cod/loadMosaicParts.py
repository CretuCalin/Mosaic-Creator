import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

def loadMosaicParts(params):


    dirPath = '../data/colectie'

    print ('Incarcam piesele pentru mozaic din director \n')

    if (params['category'] == 0) :
        dirPath = '../data/colectie'
    if (params['category'] != 0) :
        dirPath = '../data/cifar-images/' + str(params['category'])

    files = os.listdir(dirPath)

    imPiesa= cv2.imread(dirPath + '/' + files[0])


    [H , W , C] = np.shape(imPiesa)
    pieseMozaic = np.zeros([len(files),H,W,C],np.uint8)
    index = 0

    for myFile in files:
        image = cv2.imread(dirPath + '/' + myFile)
        assert np.shape(image) == (H , W , C), "img %s has shape %r" % (myFile, image.shape)

        image = np.asarray(image)

        # print np.shape(image)
        # print np.shape(pieseMozaic[index][:][:][:])

        pieseMozaic[index][:][:][:] = image

        # cv2.imshow('image',pieseMozaic[index][:][:][:])
        # cv2.waitKey(0)

        index += 1


    if params['showMosaicParts'] != 0:
        #afiseaza primele 100 de piese ale mozaicului
        plt.figure()
        plt.title('Primele 100 de piese ale mozaicului sunt:')
        idxImg = 0
        for i in range(1, 10):
            for j in range(1, 10):
                idxImg = idxImg + 1
                plt.subplot(10, 10, idxImg)
                plt.imshow(pieseMozaic[:, :, :, idxImg])
                #drawnow(pieseMozaic[:,:,:,idxImg])
                plt.pause(2)

    params['pieseMozaic'] = pieseMozaic
    return params
