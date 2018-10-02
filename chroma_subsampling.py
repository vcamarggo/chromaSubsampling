import numpy as np
import cv2
import function_errors as fe

mode = { '4:4:4': [1, 1],'4:4:0': [1,2], '4:2:2': [2,1],  '4:2:0': [2,2], '4:1:1': [4,1]}

subsampling = lambda img, mode : img[::mode[0], ::mode[1]]
upsampling	= lambda img, mode : np.repeat(np.repeat(img, mode[0], axis=0), mode[1], axis=1)
in_pic		= 'daronco' 
bgr_img 	= cv2.imread('in/' + in_pic + '.jpg', 1)
ycbcr_img	= cv2.cvtColor(bgr_img , cv2.COLOR_BGR2YCrCb)
y, cr, cb 	= cv2.split(ycbcr_img)

for key, value in mode.items():
	cb_sub = subsampling(cb, value)
	cr_sub = subsampling(cr, value)

	print('[' + key +'] Pre  sample: ' + str(y.size + cb.size + cr.size))
	print('[' + key +'] Post sample: ' + str(y.size + cb_sub.size + cr_sub.size))
	cb_unsub = upsampling(cb_sub, value)
	cr_unsub = upsampling(cr_sub, value)
	
	result 	= cv2.merge((y, cr_unsub, cb_unsub))
	
	bgr_out = cv2.cvtColor(result, cv2.COLOR_YCrCb2BGR)

	cv2.imwrite('out/' + in_pic + '_subsample_' + str(key) +'.jpg', bgr_out) 

	print('[' + key +'] Mean Squared Error: ' + str(fe.mse(bgr_img, bgr_out)))
	print('[' + key +'] Peak Signal-to-Noise Ratio: ' + str(fe.psnr(bgr_img, bgr_out)),'\n')
