import numpy as np
import cv2

GRAYSCALE=0
RGB = 1

Y=0
Cr=1
Cb=2

ROW=0
COLUMN=1

IN=0
OUT=1

#4:4:4
MODE_4_4_4 = [1,1]
#4:1:1
MODE_4_1_1 = [4,1]
#4:2:2
MODE_4_2_2 = [2,1]
#4:2:0
MODE_4_2_2 = [2,2]

#COLOR_SYSTEM
LUV = [cv2.COLOR_BGR2Luv,cv2.COLOR_Luv2BGR] 
YCrCb = [cv2.COLOR_BGR2YCrCb,cv2.COLOR_YCrCb2BGR] 
YUV = [cv2.COLOR_BGR2YUV,cv2.COLOR_YUV2BGR] 

def apply_chroma_subsampling(img, MODE):
	return img[::MODE[0], ::MODE[1]]
	
def unapply_chroma_subsampling(img, MODE):
	rowDecompressed = np.repeat(img, MODE[0], axis=ROW)
	return np.repeat(rowDecompressed, MODE[1], axis=COLUMN)

#Implementar cálculo de multiplo de 4, senao nao consegue fazer os quadrado do calculo
imgBGR = cv2.resize(cv2.imread('colors.jpg',RGB),(1680, 1052))

print("Original %d" %(imgBGR.size))

#Implementar entrada de dados
chromaMode = MODE_4_1_1
colorSystem = LUV

imgYCrCb = cv2.cvtColor(imgBGR, colorSystem[IN])

(imageY,imageCr,imageCb) = cv2.split(imgYCrCb)

subsampleCb = apply_chroma_subsampling(imageCb, chromaMode)
subsampleCr = apply_chroma_subsampling(imageCr, chromaMode)

print("Aplicado subsampling: %d" %(imageY.size + subsampleCb.size + subsampleCr.size))

unsampledCr = unapply_chroma_subsampling(subsampleCr, chromaMode)
unsampledCb = unapply_chroma_subsampling(subsampleCb, chromaMode)

result = cv2.merge((imageY, unsampledCr, unsampledCb))

compressedBGR = cv2.cvtColor(result, colorSystem[OUT])

print("Novo RGB %d" %(compressedBGR.size))

# cv2.imshow('image', compressedBRG) #remover, apenas mostra a imagem
#cv2.imwrite('colors_subsampled.jpg',compressedBGR) #fazer um esquema que busque o nome da entrada e de append 'subsampled'
