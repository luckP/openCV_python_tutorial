import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../imgs/lagart-ceni.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGE = -1


# show img with cv2
def showCv2():
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# show img with matplotlib
def showPlt():
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([50,100], [80,100], 'c', linewidth=5)
    plt.show()

# save img in local directory
def saveCv2Gray(name):
    cv2.imwrite(name+'.png', img)

def main():
    print('(0) close')
    print('(1) show img with cv2')
    print('(2) show img with matplotlib')
    print('(3) save img in local directory')

    cmd = int(input('command: '))
    while(cmd != 0):
        if(cmd == 1):
            showCv2()
        elif(cmd == 2):
            showPlt()
        elif(cmd == 3):
            saveCv2Gray(input('name: '))
        else:
            print('ERROR')
        cmd = int(input('cmmand: '))




if __name__ == '__main__':
    main()
