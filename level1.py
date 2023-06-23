import json
import cv2
import numpy as np
f=open('D:\KLA Workshop\Level_1_Input_Data\input.json')
data=json.load(f)
print(data)
img1=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_1.png",0)
img2=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_2.png",0)
img3=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_3.png",0)
img4=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_4.png",0)
img5=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_5.png",0)
number_of_white_pix = np.sum(img1 == 255)
print(img1.shape)
print(number_of_white_pix)
"""l1=[]

for i in range(0,len(img1[0])):
    if(img1[0][i]!=255):
        l1.append(i)
print(l1)
l2=[]
for i in range(0,len(img2[0])):
    if(img2[0][i]!=255):
        l2.append(i)
print(l2)
l3=[]
for i in range(0,len(img3[0])):
    if(img3[0][i]!=255):
        l3.append(i)
print(l3)
l4=[]
for i in range(0,len(img4[0])):
    if(img4[0][i]!=255):
        l4.append(i)
print(l4)
l5=[]
for i in range(0,len(img5[0])):
    if(img5[0][i]!=255):
        l5.append(i)
print(l5)"""

l1={}

for i in range(0,len(img1[2])):
    if(img1[2][i]!=128):
        l1[i]=img1[2][i]
print(l1)
l2={}
for i in range(0,len(img2[2])):
    if(img2[2][i]!=128):
        l2[i]=img2[2][i]
print(l2)
l3={}
for i in range(0,len(img3[2])):
    if(img3[2][i]!=128):
        l3[i]=img3[2][i]
print(l3)
l4={}
for i in range(0,len(img4[2])):
    if(img4[2][i]!=128):
       l4[i]=img4[2][i]
print(l4)
l5={}
for i in range(0,len(img5[2])):
    if(img5[2][i]!=128):
        l5[i]=img5[2][i]
print(l5)
print(img1[599][0])
cv2.destroyAllWindows()