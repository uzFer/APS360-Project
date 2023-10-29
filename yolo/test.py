from yolov8 import YOLOv8Wrapper

# Load a model

def main():
    model = YOLOv8Wrapper()

    model.train(model.model, datasetyaml='bddins_seg.yaml',batch_size=1,num_epochs=1)

    model.model('datasets/testtrain/images/random-street-canada-gray-day-random-street-canada-270091361 copy.png', save=True)

if __name__ == '__main__':
    main()