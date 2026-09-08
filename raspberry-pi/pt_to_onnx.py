from ultralytics import YOLO

# Load a model
model = YOLO('D:/Library_seat _query/yoloruns/train3/weights/best.pt')  # load a custom trained model

# Export the model
model.export(format='onnx', save_dir='D:/Library_seat _query/rassberyypi')
