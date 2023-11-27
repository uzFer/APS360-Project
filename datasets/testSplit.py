import os
import shutil

# Function to find 2000 same named files in different folders with different extensions
def find_same_files(folder_1, folder_2):
    txt_files = [file.split('.')[0] for file in os.listdir(folder_1) if file.endswith('.txt')]
    png_files = [file.split('.')[0] for file in os.listdir(folder_2) if file.endswith('.png')]
    all_files = txt_files+png_files
    common_files = set(all_files)
    print(common_files)
    testCommonFiles = []
    count = 0
    for name in common_files:
        if count < 2000:
            print(name)
            testCommonFiles.append(name)
            count+=1
        else:
            break
    print(len(testCommonFiles))
    return testCommonFiles

# Paths for the folders containing .txt and .png files
folder_txt = r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\trainTxt'
folder_png = r'C:\Users\desai\Downloads\bdd100k_images_10k\bdd100k\images\10k\APS360ImgData\train'

# Paths for the folders to move .txt and .png files
destination_txt = r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\testTxt'
destination_png = r'C:\Users\desai\Downloads\bdd100k_images_10k\bdd100k\images\10k\APS360ImgData\testSplit'

# Find 2000 same named files with different extensions
common_files = find_same_files(folder_txt, folder_png)
print(len(common_files))

# Move .txt files to a different folder
if len(common_files) == 2000:
    for file in common_files:
        txt_file = os.path.join(folder_txt, file + '.txt')
        if os.path.exists(txt_file):
            shutil.move(txt_file, os.path.join(destination_txt, file + '.txt'))

    # Move .png files to a different folder
    for file in common_files:
        png_file = os.path.join(folder_png, file + '.jpg')
        if os.path.exists(png_file):
            print("exists")
            shutil.move(png_file, os.path.join(destination_png, file + '.jpg'))
