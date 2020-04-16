from PIL import Image

img = Image.open('img/hot-air-ballooning-small.jpg')
img.rotate(45).show()

