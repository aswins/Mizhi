from PIL import Image
from signature import *

class extraction:
	def __init__(self,image):
		self.image = Image.open(image)
		self.filename = image
	
	def extract_feature(self):
		#a = Image.open("../temp/chars/"+filename)
		reduceto20 = self.image.resize((20,20),Image.NEAREST)
		reduceto20.save(self.filename)

		b = Image.open(self.filename)
		pix = b.load()
		signature = [0]*16
		whitepixelarray=[]
		for i in range(20):
			for j in range(20):
				if(pix[i,j] == (255,255,255)):
					whitepixelarray.append((i,j))
					signature[j/5 + (i/5)*4] = signature[j/5 + (i/5)*4] + 1
		#print signature
		extract=classify(signature)
		extract.compare_signature() 
