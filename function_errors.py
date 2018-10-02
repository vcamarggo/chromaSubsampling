import numpy as np
import math

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

def psnr(imageA, imageB):
    imageA_data = imageA.astype('float') 
    imageB_data = imageB.astype('float') 
    diff = imageB_data - imageA_data
    diff = diff.flatten('C')
    rmse = math.sqrt(np.mean(diff ** 2.))
    if rmse == 0:
        return float(0)
    return 20 * math.log10(255 / rmse)