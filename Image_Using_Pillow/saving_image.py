import PIL
import os
import sys

from PIL import ImageFilter, Image

img = Image.open("lol.jpg")

img_sharp = img.filter(ImageFilter.SHARPEN)
img_blur = img.filter(ImageFilter.BLUR)

img_sharp.save("lol_sharp.jpg")
img_blur.save("lol_blur.jpg")