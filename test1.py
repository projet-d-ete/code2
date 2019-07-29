from PIL import Image
import numpy as np
import cv2
import math
imgpil=Image.open("obj94__0.png")
imgpil2=Image.open("obj94__5.png")
imgpil3=Image.open("obj94__10.png")
imgpil.show()
imgpil2.show()
imgpil3.show()
img0=imgpil.convert('L')
img00=imgpil2.convert('L')
img000=imgpil3.convert('L')
img0.show()
img00.show()
img000.show()
img=np.array(img0)
img2=np.array(img00)
img3=np.array(img000)
#pour la 1ère image
print("pour la 1ére image:")
moments=cv2.moments(img)
print("les moments :",moments)
huMoments=cv2.HuMoments(moments)
print("\n")
for i in range(0,7):
    huMoments[i]=-1*math.copysign(1.0,huMoments[i])*math.log10(abs(huMoments[i]))
print("les humoments:",huMoments)
print("\n")

#pour la 2ème image
print("pour la 2eme image:")
moments=cv2.moments(img2)
print("les moments :",moments)
huMoments=cv2.HuMoments(moments)
print("\n")
for i in range(0,7):
    huMoments[i]=-1*math.copysign(1.0,huMoments[i])*math.log10(abs(huMoments[i]))
print("les humoments:",huMoments)
print("\n")

#pour la 3ème image
print("pour la 3eme image:")
moments=cv2.moments(img3)
print("les moments :",moments)
huMoments=cv2.HuMoments(moments)
print("\n")
for i in range(0,7):
    huMoments[i]=-1*math.copysign(1.0,huMoments[i])*math.log10(abs(huMoments[i]))
print("les humoments:",huMoments)
