from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# retorna o endereço reativo dentro da pasta 'input'
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def triangulo(size):
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)

    image = Image.new("RGB", (size, size), YELLOW)
    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), BLACK)
    
    return image

def bandeira_franca(height):
    width = (3 * height // 2)
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    image = Image.new("RGB", (width, height), WHITE)

    offset = width//3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2 * offset, y), RED)
    return image


if __name__ == "__main__":
    #t = triangulo(700)
    #t.show()
    bandeira = bandeira_franca(700)
    bandeira.show()
    
