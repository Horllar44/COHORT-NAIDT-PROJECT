# ============AHMED RIDWANULLAHI============= 
# NAIDT PROJECT
# PROJECT TOPIC: ¬¬¬¬¬¬¬"IMAGE CONVERTER"¬¬¬¬¬¬¬¬

# I'm using two different methods to convert image to a PDF for this project.

# Method_One: Working
# Firstly, I implement the PIL (Pillow or Python Imaging Library) 
# module/package in Python to combine several images into a single PDF file.

# Secondly, The Image.open method is used in this code to open each image first. 
# I then use the convert method to convert each image to RGB.
# Then, I compile a list of the pictures, omitting the first one.

# Lastly, I use the save method to save the images to a PDF, 
# with the parameters append_images=image_list 
# to append the images in the list to the PDF and save_all=True to save all images.

print("¬¬¬¬¬¬¬¬¬¬Imagees¬¬¬¬¬¬¬¬¬¬")
from PIL import Image

# Open the images
image_1 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/A New Design - Made with PosterMyWall (7).png')
image_2 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/IMG_20231130_185702_871.jpg')
image_3 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/IMG_20231130_214104_381.jpg')
image_4 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/IMG_20231130_225828_655.jpg')
image_5 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/Restaurant Menu - Made with PosterMyWall.jpg')
image_6 = Image.open(r'C:/Users/B-YINKER/Desktop/project file/Screenshot_20231121-151505_Chrome-transformed.jpeg')

#Convert the images to RGB
im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
im_3 = image_3.convert('RGB')
im_4 = image_4.convert('RGB')
im_5 = image_5.convert('RGB')
im_6 = image_6.convert('RGB')

#Create a list of the images
image_list = [im_2, im_3, im_4, im_5, im_6]

#Save the images to a PDF
im_1.save(r'C:/Users/B-YINKER/Desktop/project file/Pdf/Method1/images.pdf', save_all=True, append_images=image_list)



# Method_Two:
# import os
# from PIL import Image # pip install pillow

# output_dir = 'C:/Users/SEUN ADELEYE/Desktop/Lappy/16th/Concepts/2019 Art/References/ig/Logos/Figma/Img2PDF/Method4'
# source_dir = 'C:/Users/SEUN ADELEYE/Desktop/Lappy/16th/Concepts/2019 Art/References/ig/Logos/Figma/Img2PDF'

# for file in os.listdir(source_dir):
#     if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
#         image = Image.open(os.path.join(source_dir, file))
#         image_converted = image.convert('RGB')
#         image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))
