import json
import os
import cv2 as cv
import matplotlib as plt
import matplotlib as mpimg
import shutil

dir1 = r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\valTxt'
dir2 = r'C:\Users\desai\Downloads\bdd100k_images_10k\bdd100k\images\10k\APS360ImgData\val'

dir1Files = [file.split('.')[0] for file in os.listdir(dir1) if file.endswith('.txt')]
dir2Files = [file.split('.')[0] for file in os.listdir(dir2) if file.endswith('.jpg')]
print(len(dir1Files))
print(len(dir2Files))
allFiles = dir1Files + dir2Files
print(len(allFiles))
common = set(allFiles)
print(len(common))