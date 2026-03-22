import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.image as img
import time 
import threading  

photo=img.imread(r'C:\Users\DEL\Downloads\simple.jpeg')
#

#EXO1

'''red = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
green = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
blue = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
for i in range(len(photo)):
    for j in range(len(photo[0])) :
            red[i][j] = [photo[i][j][0],0,0]
            green[i][j] = [0,photo[i][j][1],0]
            blue[i][j] = [0,0,photo[i][j][2]]


aff = [photo, red, green, blue]
for i in range(4):
    plt.subplot(2, 2, i+1)   
    plt.imshow(aff[i])       
    plt.axis("off")  
    plt.savefig(f"img{i}.png", dpi=300, bbox_inches="tight")
        
plt.show()

#EXO2

#En couleur
tof_neg = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
for i in range(len(photo)):
    for j in range(len(photo[0])) :
        tof_neg[i][j] = [255 - photo[i][j][0],255 - photo[i][j][1],255 - photo[i][j][2]]
aff = [tof_neg]
for i in range(1):
    plt.subplot(1, 1, i+1)   
    plt.figure(figsize=(10, 8))
    plt.imshow(aff[i])       
    plt.axis("off") 
    plt.savefig(f"img{i+4}.png", dpi=300, bbox_inches="tight")         
plt.show()
'''
#En noir et blanc
#tof = img.imread(r'C:\Users\DEL\Downloads\classy-living-crest-modern-house-design-vector-icon-chic-habitat-vision-stylish-house-design-vector_706143-36306.avif')
'''tof_neg = [[[0,0,0] for j in range(len(tof[0]))] for i in range(len(tof))]
for i in range(len(tof)):
    for j in range(len(tof[0])) :
        tof_neg[i][j] = [255 - tof[i][j][0],255 - tof[i][j][1],255 - tof[i][j][2]]
aff = [tof, tof_neg]
for i in range(2):
    plt.subplot(2, 1, i+1)   
    plt.imshow(aff[i])       
    plt.axis("off")          
plt.show()
'''
#EXO3

deb = time.perf_counter()

gris_simple = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
gris_pond = [[[0,0,0] for j in range(len(photo[0]))] for i in range(len(photo))]
for i in range(len(photo)):
    for j in range(len(photo[0])) :
        gris_simple[i][j] = (int(photo[i][j][0]) + int(photo[i][j][1]) + int(photo[i][j][2]))/3
        gris_pond[i][j] = 0.2126*photo[i][j][0] + 0.7152*photo[i][j][1] + 0.0722*photo[i][j][2]
aff = [ gris_simple , gris_pond]
for i in range(2):
    plt.subplot(1, 2, i+1)   
    plt.imshow(aff[i],plt.cm.gray)       
    plt.axis("off")  
    plt.savefig(f"img{i+5}.png", dpi=300, bbox_inches="tight")        

plt.show()

end = time.perf_counter()

print(f"Without thred",end - deb)
