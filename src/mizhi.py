from PIL import Image
import os
 
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
            #b.append(l[i+1])
            i=i+1
    return b

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

#    j=0
    for i in newlines:
        q=a.crop((i[0],0,i[1],a.size[1]))
        q.save("../temp/chars/"+str(newname)+".png")
        newname=newname+1
    return newname  

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
#    print newlines
    j=0
    for i in newlines:
        q=a.crop((0, i[0], a.size[0], i[1]))
        q.save("../temp/chars/"+filename)
        j=j+1
def horizontalagain():
    for i in os.listdir("../temp/chars/"):
        horizontal2(i)

def classify(filename):
    a = Image.open("../temp/chars/"+filename)
    reduceto20 = a.resize((20,20),Image.NEAREST)
#for a single character.when thereis a bunch we will use a counter
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

#    print "Locations of white pixels"
#    print whitepixelarray
    print signature
    
        
if __name__=="__main__":
    binary("vya.png")
    horizontal()
    j=0
#    print os.listdir("../temp/lines/")
    filelist=os.listdir("../temp/lines/")
    filelist.sort()
#    print filelist
    for i in filelist:
        j=vertical(i,j)
        j=j+1
    horizontalagain()
    for i in os.listdir("../temp/chars/"):
        classify(i)
    print "done"