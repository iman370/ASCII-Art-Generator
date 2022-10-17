import numpy as np
from PIL import Image

# Turn this image into ASCII art
img = 'amongus.png'
imageX = 32
imageY = 32

ascii_alphabet = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #length: 70

def loadImage(image, resizeX=imageX, resizeY=imageY):
    return np.array(Image.open(image).convert('L').resize((resizeX,resizeY)))

def showImage(image):
    from matplotlib import pyplot as plt
    plt.imshow(image, interpolation='nearest')
    plt.show()

def main():
    image = loadImage(img)
    image = (image/255) * 70
    #showImage(image)
    ascii_image = ""
    for i in range(imageX):
        for j in range(imageY):
            ascii_image += ascii_alphabet[round(image[i][j]) - 1]
        ascii_image += "\n"
    print(ascii_image)

if __name__ == '__main__':
    main()