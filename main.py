import numpy as np
from PIL import Image

ascii_alphabet = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def loadImage(image):
    return np.array(Image.open(image).convert('L').resize((200,200)))

def main():
    print(loadImage('amongus.png'))
    return 0


if __name__ == '__main__':
    main()