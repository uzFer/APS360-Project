# APS360-Project

## Overview
Our team used deep learning techniques to create an object segmentation model for self-driving vehicles. Our goal is to have this autonomous vehicle correctly use object segmentation to identify obstacles such as cars and pedestrians, which can help to make our roads a safer place for all drivers. It is approximated that 1.3 million people die from road crashes each year and our team believes that autonomous safety systems could help alleviate this. We expect an accurate model that could be used in vehicular or rover safety sensors or systems, and in turn, reduce human error when driving. Deep learning is an appropriate tool for the task due to its ability to learn in dynamic, moving environments and be tested on diverse training sets such as real-world images. Our team has implemented a deep learning model utilizing YOLOv8, a framework that is ideal for real-time object segmentation. 

![sample2](https://github.com/user-attachments/assets/e2b22aa4-9451-441d-ae15-c29f5314968f)

## Data Processing
We opted for the 10k image data set from the BDD collection. As we used the YOLOv8 framework, we downloaded and processed the instance segmentation data in JSON format, available for 8,000 images. This resulted in a training:validation:test split of 5000:1000:2000. We also duplicated images that contained underrepresented classes (i.e. trucks, pedestrians, bikes, etc.) to increase its number of instances. We also applied traditional augmentations such as change in orientation and hue. 

## Architecture
YOLOv8 models typically require large amounts of data to train from scratch. Luckily, transfer learning can be applied to utilize the five pretrained models that YOLOv8 offers as a starting point, which are trained on the COCO data set and are categorized by the number of trainable weights. We chose to use the medium sized model, that contains 331 layers and over 27 million trainable parameters. To implement transfer learning and training of the YOLOv8 model, we created a wrapper class (YOLOv8Wrapper) to assists us in easily loading checkpoints and setting necessary training hyperparameters. 

## Baseline Model
Our team decided to implement a classical computer vision algorithm called the Canny Edge Detector as our baseline model. Prior to deep learning, edge detection was essential in tasks such as boundary detection and the early stages of image segmentation. Even with the onset of deep learning, edge processing is often used as an initial step to image segmentation, making the Canny Edge Detector a suitable baseline to compare with our project. 

![baseline output](https://github.com/user-attachments/assets/8cf0fe9a-28a6-4824-b57a-7d722b8b02ed)


