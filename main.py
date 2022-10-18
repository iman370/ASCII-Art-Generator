import numpy as np
from PIL import Image

imageX = 32
imageY = 32

#ascii_alphabet = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #length: 70
ascii_alphabet = "@%#*+=-:. "
#ascii_alphabet = " .:-=+*#%@"

# Turn this image into ASCII art
def getImage():
    imageName = input("Please enter the image file name: ")

    return imageName

def loadImage(image, resizeX=imageX, resizeY=imageY):
    return np.array(Image.open(image).convert('L').resize((resizeX,resizeY)))

def showImage(image):
    from matplotlib import pyplot as plt
    plt.imshow(image, interpolation='nearest')
    plt.show()

def main():
    image = loadImage(getImage())
    image = (image/255) * (len(ascii_alphabet))
    showImage(image)
    ascii_image = ""
    for i in range(imageX):
        for j in range(imageY):
            ascii_image += ascii_alphabet[round(image[i][j]) - 1]
        ascii_image += "\n"
    #print(ascii_image)
    with open("ascii-art.txt", 'w') as f:
        f.write(ascii_image)

    

if __name__ == '__main__':
    main()