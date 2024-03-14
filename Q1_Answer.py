"""
EG/2019/3774
Weerawanni W.M.C.R.
"""

import cv2

def reduce_intensity_levels(image, numLevels):
    factor = 256 // numLevels
    quantizedImage = (image // factor) * factor
    return quantizedImage

def main():
    #Here image is reading from the TestImage folder
    FILE_PATH = "TestImage/Image.png"
    #Image is reading as gray image
    img = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)

    #Here getting the desired number of intensity levels from user
    numOfLevels = int(input("Enter the number of intensity levels (as power of 2): "))

    #Here checking user givven number of intensity levels is a power of 2
    if numOfLevels <= 0 or not (numOfLevels & (numOfLevels - 1) == 0):
        print("Number of levels must be a power of 2!")
        return

    #Reducing the number of intensity levels using a function
    reducedImage = reduce_intensity_levels(img, numOfLevels)

    #Here saving the reduced image
    cv2.imwrite('Results/Q1/Img_with_intensity_levels_{}.jpg'.format(numOfLevels), reducedImage)

    #Here displaying the reduced image
    cv2.imshow('Reduced Image', reducedImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
