from PIL import Image
v = 0

class vsegmentation:

    def __init__(self,image):
        self.image = image

    def create_chars(self):
        pix = self.image.load()
        characters = []

        for x in range(self.image.size[0]):
            thereIsNoWhitePixel = True
            for y in range(self.image.size[1]):
                if(pix[x,y] != (0,0,0)):
                    thereIsNoWhitePixel = False
            if thereIsNoWhitePixel:
                characters.append(x)

        counter = 0
        vsegments = []


        while counter+1 < len(characters):
            if characters[counter]+1 == characters[counter+1]:
                counter = counter + 1
            else:
                vsegments.append((characters[counter]+1,characters[counter+1]))
                counter = counter + 1

        
        
	global v
        for x in vsegments:
            vcropped = self.image.crop((x[0],0,x[1],self.image.size[1]))
            vcropped.save("../temp/vsegments/"+str(v)+".png")
            v = v+1

        
	
