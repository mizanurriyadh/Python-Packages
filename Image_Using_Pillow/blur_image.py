import PIL

from PIL import Image, ImageFilter

img = Image.open("lol.jpg")

# Applying Blur filter to the image
im_blur = img.filter(ImageFilter.BLUR)

im_blur.show()