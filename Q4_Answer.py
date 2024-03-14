"""
EG/2019/3774
Weerawanni W.M.C.R.
"""

import cv2
import numpy as np

def calculate_block_average(image, blockSize):
    #Getting image dimensions
    height, width = image.shape[:2]

    #Here calculating the number of blocks considering both height and width
    numHeightBlocks = height // blockSize
    numWidthBlocks = width // blockSize

    #Reshaping the image into blocks
    blocks = (image[:numHeightBlocks * blockSize, :numWidthBlocks * blockSize].reshape
        (numHeightBlocks, blockSize, numWidthBlocks, blockSize, -1))

    #Calculating the average of each block
    blockAverage = np.mean(blocks, axis=(1, 3)).astype(np.uint8)

    #Repeat block averages to get full image
    result = np.repeat(np.repeat(blockAverage, blockSize, axis=0), blockSize, axis=1)

    return result

def main():
    #Here image is reading from the TstImage folder
    FILE_PATH = "TestImage/Image.png"
    #Image is reading as gray image
    img = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)

    # Apply block averaging for each block size
    imageAveraged_3x3 = calculate_block_average(img, 3)
    imageAveraged_5x5 = calculate_block_average(img, 5)
    imageAveraged_7x7 = calculate_block_average(img, 7)

    # Here Im saving the filtered images
    cv2.imwrite('Results/Q4/Img_3x3_block_averaged.jpg', imageAveraged_3x3)
    cv2.imwrite('Results/Q4/Img_5x5_block_averaged.jpg', imageAveraged_5x5)
    cv2.imwrite('Results/Q4/Img_7x7_block_averaged.jpg', imageAveraged_7x7)

    # Here Im displaying the reduced image
    cv2.imshow('3x3 block averaged image.jpg', imageAveraged_3x3)
    cv2.imshow('5x5 block averaged image.jpg', imageAveraged_5x5)
    cv2.imshow('7x7 block averaged image.jpg', imageAveraged_7x7)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()