#===============================================================================
# This is the starting phase of Mizhi OCR. This code reads the filename from the user.
# Then the image is divided into lines and is stored in the folder "../temp/lines".
# Each line is further split into characters and is stored in the folder "../temp/chars"
# Then the signature of all the individual characters is found out.
# Classification stage is still to be done.
#===============================================================================


from PIL import Image
import os
import sys
from classify2 import *
 
#This functions accepts a filename. Convert the image into binary and store it in
#../temp/
def binary(filename):
    a=Image.open(filename)
    pix=a.load()

    for i in range(a.size[0]):
        for j in range(a.size[1]):
            if(pix[i,j][0]>127 or pix[i,j][1]>127 or pix[i,j][2]>127):
                pix[i,j]=(0,0,0)
            else:
                pix[i,j]=(255,255,255)
    a.save("../temp/binary.png")
    
def purge(l):
    i=0
    b=[]
    while i+1<len(l):
        if l[i]+1==l[i+1]:
            i=i+1
        else:
            b.append((l[i],l[i+1]))
            i=i+1
    return b

#Divides the converted binary image into lines and stores it in the location 
#../temp/lines/
def horizontal():
    a=Image.open("../temp/binary.png")
    pix=a.load()
    lines = []

    for i in range(a.size[1]):
        thereIsNoWhitePixel = True
        for j in range(a.size[0]):
            if(pix[j, i] != (0, 0, 0)):
                thereIsNoWhitePixel = False
        if thereIsNoWhitePixel:
            lines.append(i)
        
    newlines = purge(lines)
#    print newlines
    j=0
    for i in newlines:
        q=a.crop((0, i[0], a.size[0], i[1]))
        q.save("../temp/lines/"+str(j)+".png")
        j=j+1

#Opens each file in "../temp/lines/" and divide it into individual characters.
#The images are stored in ../temp/chars/
#This function returns the last file name.
def vertical(filename,newname):
    a = Image.open("../temp/lines/"+filename)
    pix = a.load()

    lines = []

    for i in range(a.size[0]):
        thereIsNoWhitePixel = True
        for j in range(a.size[1]):
            if(pix[i,j] != (0, 0, 0)):
                thereIsNoWhitePixel = False
        if thereIsNoWhitePixel:
            lines.append(i)
        
    newlines = purge(lines)

    for i in newlines:
        q=a.crop((i[0],0,i[1],a.size[1]))
        q.save("../temp/chars/"+str(newname)+".png")
        newname=newname+1
    return newname  #This is a crude way to ensure that the images of characters are
                    #named in sequence. It would be better if a static variable is used here

# opens each file in ../temp/chars and crops it to a fitting box
def horizontal2(filename):
    a=Image.open("../temp/chars/"+filename)
    pix=a.load()
    lines = []

    for i in range(a.size[1]):
        thereIsNoWhitePixel = True
        for j in range(a.size[0]):
            if(pix[j, i] != (0, 0, 0)):
                thereIsNoWhitePixel = False
        if thereIsNoWhitePixel:
            lines.append(i)
        
    newlines = purge(lines)
    j=0
    for i in newlines:
        q=a.crop((0, i[0], a.size[0], i[1]))
        q.save("../temp/chars/"+filename)
        j=j+1
        
#Helper function to horizontal2
def horizontalagain():
    for i in os.listdir("../temp/chars/"):
        horizontal2(i)

#Resizes each image in ../temp/chars to 20X20 and finds out the signature of each.
#Then based on the signature the corresponding character is found
def extract_feature(filename):
    a = Image.open("../temp/chars/"+filename)
    reduceto20 = a.resize((20,20),Image.NEAREST)
    reduceto20.save("reducedto20.png")

    b = Image.open("reducedto20.png")
    pix = b.load()
    signature = [0]*16
    whitepixelarray=[]
    for i in range(20):
        for j in range(20):
            if(pix[i,j] == (255,255,255)):
                whitepixelarray.append((i,j))
                signature[j/5 + (i/5)*4] = signature[j/5 + (i/5)*4] + 1
    print classify(signature) 
    
        
if __name__=="__main__":
    if len(sys.argv)==1:
        name=raw_input("Enter filename : ")
        binary(name)
    else:
        binary(sys.argv[1])
    horizontal()
    j=0
    filelist=os.listdir("../temp/lines/")
    filelist.sort()
    for i in filelist:
        j=vertical(i,j)
        j=j+1
    horizontalagain()
    for i in os.listdir("../temp/chars/"):
        extract_feature(i)
    print "done"