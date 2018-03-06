import PIL

from PIL import Image, ImageFilter

img = Image.open("lol.jpg")

# Applying Blur filter to the image
img_sharp = img.filter(ImageFilter.SHARPEN)

img_sharp.show()