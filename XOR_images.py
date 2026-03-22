import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img 
import os 
from PIL import Image

list_format_utilisable = [".jpg", ".jpeg", ".bmp", ".ppm",".pgm"]

path1 = r'path\to\image1'
path2 = r'path\to\image2'

photo1 = img.imread(path1)
photo2 = img.imread(path2)

########################################## Problème avec le format #############################################

ext1 = os.path.splitext(path1)
ext2 = os.path.splitext(path2)

if ext1 not in list_format_utilisable :  
    im = Image.open(path1).convert("RGB") 
    photo1 = np.array(im)

if ext2 not in list_format_utilisable :  
    im = Image.open(path2).convert("RGB") 
    photo2 = np.array(im)

###############################################################################################################


####################################### Génération de l'image XOR #############################################

xor_image = [[[0,0,0] for j in range(len(photo1[0]))] for i in range(len(photo1))]

for i in range(len(photo1)):
    for j in range(len(photo1[0])) :
        xor_image[i][j] = [photo1[i][j][0] ^ photo2[i][j][0], photo1[i][j][1] ^ photo2[i][j][1], photo1[i][j][2] ^ photo2[i][j][2]]

plt.imshow(xor_image)       
plt.axis("off")  
plt.savefig(f"xor_image.jpg", dpi=300, bbox_inches="tight")     
plt.show()

###############################################################################################################