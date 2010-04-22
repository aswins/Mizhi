#Code for conversion starts here
from PIL import Image
import os,sys
from binary import *
from horizontal_segmentation import *
from vertical_segmentation import *
from hchar_segmentation import *
from feature_extraction import *

#Entering scanned image
print "Enter the scanned image:"
input_image = raw_input()

#Entering binarisation phase

ocr_input = Image.open(input_image)
binary_image = binary(ocr_input)
binary_image.binarize()

#Entering horizontal segmentation phase
#Segmented output is obtained as "\temp\hsegments" folder

h_segmentation_input =  Image.open("../temp/binary_image.png")
hsegments = hsegmentation(h_segmentation_input)
hsegments.addlines()


#Entering vertical segmentation phase
#Segmented output is obtained in "\temp\vsegments" folder

hsegment_list = os.listdir("../temp/hsegments")
hsegment_list.sort()

for i in hsegment_list:
    v_segmentation_input = Image.open("../temp/hsegments/"+i)
    vsegments = vsegmentation(v_segmentation_input)
    vsegments.create_chars()
    
    
print "Vertical Segmentation Completed..."

#Entering horizontal segmentation again to cut of unwanted black pixels in the images obtained 
#after vertical segmentation
#Segmented charcters replace images in /temp/vsegments folder

vsegment_list = os.listdir("../temp/vsegments")
vsegment_list.sort()


for i in vsegment_list:
    hchar_segmentation_input = hchar_segmentation(i)
    hchar_segmentation_input.makesize()

print "Characters reduced to fit-size..."

#Entering feature-extraction stage...This phase reduces each character segment to a size of 20X20
#and generates a signature for each character 
vsegment_list = os.listdir("../temp/vsegments")
#print vsegment_list
for i in range(len(vsegment_list)):
	#print i
	feature=extraction("../temp/vsegments/"+str(i)+".png")
	feature.extract_feature()



