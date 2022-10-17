import numpy as np
from PIL import Image

# Turn this image into ASCII art
img = 'amongus.png'

ascii_alphabet = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #length: 70

def loadImage(image, resizeX=64, resizeY=64):
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
    for i in range(64):
        for j in range(64):
            ascii_image += ascii_alphabet[round(image[i][j]) - 1]
        ascii_image += "\n"
    print(ascii_image)




if __name__ == '__main__':
    main()