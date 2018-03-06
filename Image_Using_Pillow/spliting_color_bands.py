import PIL
import os
import sys

from PIL import ImageFilter, Image

img = Image.open("lol.jpg")

# Applying Blur filter to the image
img_sharp = img.filter(ImageFilter.SHARPEN)

r,g,b = img_sharp.split()

b.show()