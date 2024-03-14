"""
EG/2019/3774
Weerawanni W.M.C.R.
"""

from PIL import Image
import cv2
import numpy as np

def main():
    #Here image is reading from the TestImage folder
    FILE_PATH = "TestImage/Image.png"
    image = Image.open(FILE_PATH)

    #Rotate the image by 45 degrees & 90 degrees
    rotatedImage_45 = image.rotate(45, expand=True)  # Use expand=True to avoid cropping
    rotatedImage_90 = image.rotate(90, expand=True)  # Use expand=True to avoid cropping

    #Here saving the rotated images
    rotatedImage_45.save('Results/Q3/Img_rotated_45.jpg')
    rotatedImage_90.save('Results/Q3/Img_rotated_90.jpg')

    #Here displaying the rotated images
    cv2.imshow('Rotated 45 Degrees', cv2.cvtColor(np.array(rotatedImage_45), cv2.COLOR_RGB2BGR))
    cv2.imshow('Rotated 90 Degrees', cv2.cvtColor(np.array(rotatedImage_90), cv2.COLOR_RGB2BGR))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
