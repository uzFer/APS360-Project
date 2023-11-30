import cv2
import os
from yolo.yolov8 import YOLOv8Wrapper
import torch

# Splitting Video into Frames
def split_video_into_frames(video_path, output_folder):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(os.path.join(output_folder, f"frame_{count}.jpg"), image)
        success, image = vidcap.read()
        count += 1

# Processing Frames
def process_frames(input_folder, output_folder):
    model = YOLOv8Wrapper(checkpoint='C:/Users/tanus/OneDrive/Documents/GitHub/APS360-Project/runs/segment/train-medium-newclassesflipped-default-batch8/weights/best.pt')

    for filename in os.listdir(input_folder):
        result = model.model(os.path.join(input_folder + '/' + filename), save=True, boxes = False, show_conf = False, show_labels = False)

# Combining Frames into Video
def frames_to_video(input_folder, output_video_path):
    frames = []
    for filename in sorted(os.listdir(input_folder), key=lambda x: int(x.split('_')[1].split('.')[0])):
        if filename.endswith(".jpg"):
            frames.append(cv2.imread(os.path.join(input_folder, filename)))

    height, width, layers = frames[0].shape
    video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    for frame in frames:
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()


video_path = 'C:/Users/tanus/Downloads/democlip.mp4'
frames_folder = os.getcwd() +'/demoframes/original'
processed_frames_folder = 'C:/Users/tanus/OneDrive/Documents/GitHub/APS360-Project/runs/segment/predict5'
output_video_path = os.getcwd() + '/output_video.mp4'
cur_dir = os.getcwd()


split_video_into_frames(video_path, frames_folder)
process_frames(frames_folder, processed_frames_folder)
frames_to_video(processed_frames_folder, output_video_path)