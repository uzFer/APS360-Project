# APS360-Project

## Overview
Our team is interested in using deep learning techniques to create an object segmentation and recognition model for self-driving vehicles. Our goal is to have this autonomous vehicle correctly use object segmentation to identify obstacles such as cars, traffic lights and stop signs (i.e. without any human input). The team is passionate about this idea and believes that there is potential for self-driving vehicles to make our roads a safer place for all drivers. It is approximated that 1.3 million people die from road crashes each year, which autonomous safety systems could help alleviate. At the end of our project, the team expects an accurate model that could be used in vehicular or rover safety sensors or systems, and in turn, reduce human error when driving. We believe that deep learning is an appropriate tool for the task due to its ability to learn in dynamic, moving environments and be tested and validated on diverse training sets such as real-world images. 

## Architecture
To tackle the object detection and feature extraction of our input images, we plan to integrate the YOLOv8 architecture. We propose to first use the YOLOv8 for initial image processing and object detection, as it is fast and accurate through grid processing of the input image. We have integrated a default YOLO model with results shown below. Further steps are to undergo hyperparameter tuning and measure our F1 Score and other metrics of success after doing so.

![image](https://github.com/uzFer/APS360-Project/assets/109243682/aa030d45-ad70-4477-8e49-8cef451afa3f)
