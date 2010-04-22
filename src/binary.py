from PIL import Image

class binary:
#The constructor for class binary.The paramenter (image_name) is
#the name of the .jpeg image(i.e a string)
    def __init__(self,image):
        self.image = image

#the code that binarises the image object(a .jpeg file)and saves
#the same as a .png file in the name binary_image.png
    def binarize(self):
        pix = self.image.load()
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                if(pix[x,y][0]>127 or pix[x,y][1]>127 or pix[x,y][2]>127):
                    pix[x,y] = (0,0,0)
                else:
                    pix[x,y] = (255,255,255)
        self.image.save("../temp/binary_image.png")
        print "Image Binarised...."







