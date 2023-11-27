import json
import os


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
                
                if class_name == "trailer" or class_name == "train":
                    continue
                elif class_name == "car":
                    class_index = classes.index("car")
                elif class_name == "rider" or class_name == "person":
                    class_index = classes.index("person")
                elif class_name == "truck" or class_name == "bus" or class_name == "caravan":
                    class_index = classes.index("large-vehicle")
                elif class_name == "bike" or class_name == "bicycle":
                    class_index = classes.index("small-vehicle")
                
                    
                poly2d_list = label['poly2d']
                for poly_dict in poly2d_list:
                    vertices = poly_dict['vertices']
                    coordinates_str = ""
                    for x, y in vertices:
                        xCoords = x/1280
                        yCoords = y/720
                        if xCoords > 1:
                            xCoords = 1
                        if yCoords > 1:
                            yCoords = 1
                        coordinates_str += f"{xCoords} {yCoords} "
                    content = f"{class_index} {coordinates_str}\n"
                    txt_file.write(content)

    print(f"File {file_name} created successfully.")

BDDLabel_to_YOLO(r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\ins_seg_val.json', r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\valTxt')
BDDLabel_to_YOLO(r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\ins_seg_train.json', r'C:\Users\desai\Downloads\bdd100k_ins_seg_labels_trainval\bdd100k\labels\ins_seg\polygons\trainTxt')
