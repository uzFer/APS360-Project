from yolov8 import YOLOv8Wrapper
import torch
# Load a model

def main():
    model = YOLOv8Wrapper()
    torch.cuda.set_device(0)
    model.train(model.model, datasetyaml='bddins_seg.yaml', batch_size=8, num_epochs=200, checkpointFreq=40)

if __name__ == '__main__':
    main()