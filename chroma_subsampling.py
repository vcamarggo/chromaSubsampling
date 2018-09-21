import numpy as np
import cv2

GRAYSCALE=0
RGB = 1

Y=0
Cr=1
Cb=2

ROW=0
COLUMN=1
#4:1:1
MODE_4_1_1 = [4,1]

def apply_chroma_subsampling(img, MODE):
	return img[::MODE[0], ::MODE[1]]
	
def unapply_chroma_subsampling(img, MODE):
	rowDecompressed = np.repeat(img, MODE[0], axis=ROW)
	return np.repeat(rowDecompressed, MODE[1], axis=COLUMN)
	
#Implementar cálculo de multiplo de 4, senao nao consegue fazer os quadrado do calculo
imgBGR = cv2.resize(cv2.imread('colors.jpg',RGB),(1680, 1052))

#Implementar entrada de dados

imgYCrCb = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YCrCb)

# imageY = imgYCrCb[:,:,Y]  #Remover se não for obrigatório fazer na mão
# imageCr = imgYCrCb[:,:,Cr]
# imageCb = imgYCrCb[:,:,Cb]

(imageY,imageCr,imageCb) = cv2.split(imgYCrCb)

subsampleCb = apply_chroma_subsampling(imageCb, MODE_4_1_1)
subsampleCr = apply_chroma_subsampling(imageCr, MODE_4_1_1)

print(len(imageY))#Remover depois
print(len(subsampleCb))
print(len(subsampleCr))

unsampledCr = unapply_chroma_subsampling(subsampleCr, MODE_4_1_1)
unsampledCb = unapply_chroma_subsampling(subsampleCb, MODE_4_1_1)

print(len(imageY))#Remover depois
print(len(unsampledCr))
print(len(unsampledCb))
result = np.dstack((imageY, unsampledCr, unsampledCb))

compressedBGR = cv2.cvtColor(result, cv2.COLOR_YCrCb2BGR)

# cv2.imshow('image', compressedBRG) #remover, apenas mostra a imagem
cv2.imwrite('colors_subsampled.jpg',compressedBGR) #fazer um esquema que busque o nome da entrada e de append 'subsampled'
