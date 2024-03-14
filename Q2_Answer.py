"""
EG/2019/3774
Weerawanni W.M.C.R.
"""

import cv2
import numpy as np

def average_filter(image, kernelSize):
    #Here creating a kernel with the desired size
    kernel = np.ones((kernelSize, kernelSize), np.float32) / (kernelSize * kernelSize)

    #Apply the filter using OpenCV filter2D
    filteredImage = cv2.filter2D(image, -1, kernel)
    return filteredImage

def main():
    #Here image is reading from the TestImage folder
    FILE_PATH = "TestImage/Image.png"
    image = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Unable to load image")
        return

    #Apply 3x3 average filter
    avg_3x3 = average_filter(image, 3)

    #Apply 10x10 average filter
    avg_10x10 = average_filter(image, 10)

    #Apply 20x20 average filter
    avg_20x20 = average_filter(image, 20)

    #Here saving the filtered images
    cv2.imwrite('Results/Q2/Img_with_3x3_filter.jpg', avg_3x3)
    cv2.imwrite('Results/Q2/Img_with_10x10_filter.jpg', avg_10x10)
    cv2.imwrite('Results/Q2/Img_with_20x20_filter.jpg', avg_20x20)

    #Here displaying the reduced image
    cv2.imshow("3x3 Average Filter", avg_3x3)
    cv2.imshow("10x10 Average Filter", avg_10x10)
    cv2.imshow("20x20 Average Filter", avg_20x20)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
