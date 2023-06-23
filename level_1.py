import json
import cv2
import numpy as np
import csv
f=open('D:\KLA Workshop\Level_1_Input_Data\input.json')
data=json.load(f)
print(data)
img1=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_1.png",0)
img2=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_2.png",0)
img3=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_3.png",0)
img4=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_4.png",0)
img5=cv2.imread("D:\KLA Workshop\Level_1_Input_Data\wafer_image_5.png",0)
defect=[]
m=[]
m.append(img1)
m.append(img2)
m.append(img3)
m.append(img4)
m.append(img5)
res=[]
d=0

for x in m:
    for i in range(len(x)):
        for j in range(len(x[i])):
            c=0
            for l in range(data["die"]["columns"]):
                if(l!=d):
                    if(x[i][j]==m[l][i][j]):
                        c+=1
            if(c<=1):
                defect.append([(d+1),j,599-i])
    d+=1

#print(defect)
file = open('output1a.csv', 'w', newline ='')
with file:   
    write = csv.writer(file)
    write.writerows(defect)


"""res=[]
for i in range(10,15):
    l=[]
    for j in range(10,15):
        l.append(img2[i][j])
    res.append(l)
print(res)

for x in m:
    for i in range(0,5):
        for j in range(0,5):
            c=0
            for l in range(5):
                if(l!=d):
                    if(x[i][j]==m[l][i][j]):
                        c+=1
            if(c<1):
                defect.append([(d+1),j,599-i])
    d+=1
print(defect)
file = open('output1a.csv', 'w', newline ='')
with file:   
    write = csv.writer(file)
    write.writerows(defect)
"""

