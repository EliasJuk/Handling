from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.open(in_path("hot-air-ballooning.jpg"))
print(image.getpixel((200,200)) )

image.show()

