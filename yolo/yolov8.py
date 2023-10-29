from ultralytics import YOLO
import cv2
import numpy as np
import torch

class YOLOv8Wrapper():
    #yolov8n-seg.pt is the default pretrained model (Transfer learning)
    def __init__(self, checkpoint='pretrained/yolov8n-seg.pt'):
        self.model = YOLO(checkpoint) 

    def train(self, model, datasetyaml, batch_size=128, num_epochs=5, checkpointFreq=1):
        # Train the model
        model.train(data=datasetyaml, batch=batch_size, epochs=num_epochs, save=True, save_period=checkpointFreq, seed=0)

    def getConfusionMatrix(self):
        metrics = self.model.val()
        return metrics.confusion_matrix