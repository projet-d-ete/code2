from PIL import Image
import numpy as np
import cv2
import math
imgpil=Image.open("obj94__0.png")
img0=imgpil.convert('L')

img=np.array(img0)
moments=cv2.moments(img)
print(moments)
huMoments=cv2.HuMoments(moments)
print(huMoments)
for i in range(0,7):
    huMoments[i]=-1*math.copysign(1.0,huMoments[i])*math.log10(abs(huMoments[i]))
print(huMoments)
