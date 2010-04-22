from PIL import Image
charn = 0


class hchar_segmentation:
    def __init__(self,image):
        self.image = Image.open("../temp/vsegments/"+image)
	self.filename = image



    def makesize(self):
        pix = self.image.load()
        flag = 0

        lines = []
        for y in range(self.image.size[1]):
            thereIsNoWhitePixel = True
            for x in range(self.image.size[0]):
                    if(pix[x, y] != (0, 0, 0)):
                            thereIsNoWhitePixel = False
            if thereIsNoWhitePixel:
                lines.append(y)

        counter = 0
        hsegments = []

        while counter+1 < len(lines):
            if lines[counter]+1 == lines[counter+1]:
                counter=counter+1
            else:
                hsegments.append((lines[counter],lines[counter+1]))
                counter=counter+1
	
	global charn
        for x in hsegments:
            hcropped = self.image.crop((0, x[0], self.image.size[0], x[1]))
            hcropped.save("../temp/vsegments/"+self.filename)
            charn = charn + 1
        
	
