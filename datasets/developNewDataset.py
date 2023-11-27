import json
import os
import cv2 as cv
import matplotlib as plt
import matplotlib as mpimg
import shutil

def BDDLabel_to_YOLO(input_file, output_folder):
    # Function to create a text file for each object
    os.makedirs(output_folder, exist_ok=True)


    with open(input_file, 'r') as json_file:
        objects_array = json.load(json_file)
    
    # classes = ['person', 'rider', 'car', 'caravan', 'truck', 'bus','motorcycle', 'bicycle', 'large-vehicle', 'small-vehicle']
    classes = ['person', 'car', 'large-vehicle', 'small-vehicle']
    for obj in objects_array:
        name, _  = os.path.splitext(obj['name'])
        labels = obj['labels']

        file_name = os.path.join(output_folder,f"{name}.txt")

        with open(file_name, 'w') as txt_file:
           for label in labels:
                class_name = label['category']
                class_index = 0
                # print("className: ",class_name)
                
                if class_name == "trailer" or class_name == "train":
                    continue
                
                elif class_name == "rider" or class_name == "person":
                    # print("person")
                    class_index = classes.index("person")
                elif class_name == "car":
                    class_name = classes.index("car")
                elif class_name == "truck" or class_name == "bus" or class_name == "caravan":
                    # print("large-vehicle")
                    class_index = classes.index("large-vehicle")
                elif class_name == "bike" or class_name == "bicycle":
                    # print("small-vehicle")
                    class_index = classes.index("small-vehicle")
                
                    
                poly2d_list = label['poly2d']
                for poly_dict in poly2d_list:
                    vertices = poly_dict['vertices']
                    coordinates_str = ""
                    for x, y in vertices:
                        xCoords = (1280-x)/1280
                        yCoords = y/720
                        if xCoords > 1:
                            xCoords = 1
                        if yCoords > 1:
                            yCoords = 1
                        coordinates_str += f"{xCoords} {yCoords} "
                    content = f"{class_index} {coordinates_str}\n"
                    txt_file.write(content)

    print(f"File {file_name} created successfully.")
    
def BDDFlippedImages(trainTxt, trainImg, flippedFolder):
    os.makedirs(flippedFolder, exist_ok=True)
    trainTxtFiles = [file.split('.')[0] for file in os.listdir(trainTxt)]
    trainImgFiles = [file.split('.')[0] for file in os.listdir(trainImg)]
    commonFiles = []
    for file in trainTxtFiles:
        if file in trainImgFiles:
            commonFiles.append(file)
            txtFile = os.path.join(trainTxt, file+'.txt')
            if os.path.exists(txtFile):
                destPng = r"C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\flippedTrainTxt"
                shutil.move(txtFile, os.path.join(destPng, file+'.txt'))
                
    
    # for img in commonFiles:
    #     src = cv.imread(os.path.join(trainImg, img+'.jpg'))
    #     flipped = cv.flip(src, 1)
    #     flippedPath = os.path.join(flippedFolder, img+'.jpg')
    #     # cv.imshow(flipped)
    #     cv.imwrite(flippedPath, flipped)
        
    
    
    

BDDLabel_to_YOLO(r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\ins_seg_val.json', r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\newValTxt')
BDDLabel_to_YOLO(r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\ins_seg_train.json', r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\newTrainTxt')
BDDFlippedImages(r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\newTrainTxt', r'C:\Users\desai\Downloads\bdd100k_images_10k\bdd100k\images\10k\train', r'C:\Users\desai\Downloads\bdd100k_images_10k\bdd100k\images\10k\trainFlipped')
