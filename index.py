from PIL import Image

image = Image.open("img/hot-air-ballooning.jpg")
print(image.getpixel((200,200)) )

image.show()

#ROTACIONAR IMAGEM
def rotate():
    img = Image.open('img/hot-air-ballooning-small.jpg')
    img.rotate(45).show()

