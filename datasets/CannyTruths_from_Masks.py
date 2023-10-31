import cv2
import numpy as np
import os

def CannyTruths_from_Masks(colormapDir, inputimageDir, outputPath):
    # Apply Canny edge detection to the colormap to extract edges
    threshold1 = 50
    threshold2 = 150
    colormap_files = os.listdir(colormapDir)
    inputimage_files = os.listdir(inputimageDir)

    for colormap_file, inputimage_file in zip(colormap_files,inputimage_files):
        colormap = cv2.imread(os.path.join(colormapDir, colormap_file), cv2.IMREAD_GRAYSCALE)
        
        #bilateral_blurred = cv2.bilateralFilter(colormap, d=20, sigmaColor=75, sigmaSpace=75)
        colormapmaskedges = cv2.Canny(colormap, threshold1, threshold2)

        # Create a blank mask with the same size as the colormap
        colormapmask = np.zeros_like(colormap)

        # Set the detected edges in the mask with thicker and blurred edges
        colormapmask[colormapmaskedges > 0] = 255
        #blur_kernel_size = 9
        #colormapmask = cv2.GaussianBlur(colormapmask, (blur_kernel_size, blur_kernel_size), 0)  # Apply Gaussian blur to make edges thicker

    
        # Read the colormap image
        realimage = cv2.imread(os.path.join(inputimageDir, inputimage_file), cv2.IMREAD_GRAYSCALE)

        # Apply Canny edge detection to the colormap to extract edges
        realimageedges = cv2.Canny(realimage, threshold1, threshold2)

        # Create a blank mask with the same size as the colormap
        realimagemask = np.zeros_like(realimage)

        # Set the detected edges in the mask with thicker and blurred edges
        realimagemask[realimageedges > 0] = 255
        #blur_kernel_size = 5
        #realimagemask = cv2.GaussianBlur(realimagemask, (blur_kernel_size, blur_kernel_size), 0)  # Apply Gaussian blur to make edges thicker



        # Add the two edge maps pixel-wise
        summed_masks = cv2.add(realimagemask, colormapmask)

        # Save the result
        
        cv2.imwrite(os.path.join(outputPath,inputimage_file), summed_masks)