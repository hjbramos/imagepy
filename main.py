from PIL import Image


img = Image.open("pizza.png")
print(img.format, img.size, img.mode)