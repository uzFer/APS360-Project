# this file computes the f1 score using the input model with the test dataset
from ultralytics import YOLO
import os

# run inference on the test set
def test_validation():
    cur_dir = os.getcwd()

    # the path to the model used
    model_path = cur_dir + '/results/train-default-batch8/weights/best.pt'
    img_path = cur_dir + '/datasets/aps360data/test/images'

    model = YOLO(model_path)  # load a custom model
    results = model.val(split='test', save_json=False)


# Convert precision and recall of classes into f1 score saved as a dictionary
def f1_scores(object_class, recall, precision):
    f1 = {}
    
    for i in range(len(recall) - 1):
        cur_f1 = 2 * (precision[i]*recall[i]) / (precision[i] + recall[i])
        f1[object_class[i]] = cur_f1
        # print({{object_class[i]:>12}, " - f1 score: ", cur_f1})
        print(f"{object_class[i]:>12}{cur_f1 :>36}")
    return f1

classifiers = ['all', 'person', 'rider', 'car', 'caravan', 'truck', 'bus', 'train', 'trailer', 'motorcycle', 'bicycle']
precision = [0.46, 0.212, 0.235, 0.215, 1, 0.141, 0.137, 1, 1, 0.344, 0.32]
recall = [0.18, 0.357, 0.115, 0.607, 0, 0.264, 0.267, 0, 0, 0.105, 0.0827]
f1_scores(classifiers, recall, precision)


