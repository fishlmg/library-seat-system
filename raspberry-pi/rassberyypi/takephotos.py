import cv2
import torch
from models import *  # set ONNX_EXPORT in models.py
from utils.datasets import *
from utils.utils import *

def load_model(weights_path, img_size=416):
    device = torch_utils.select_device(device='cpu')
    model = Darknet("cfg/yolov3.cfg", img_size)
    model.load_state_dict(torch.load(weights_path, map_location=device)['model'])
    model.to(device).eval()
    return model, device

def analyze_image(model, device, img_path):
    img = letterbox(cv2.imread(img_path))[0]
    img = img.transpose(2, 0, 1)
    img = torch.from_numpy(img).float().to(device).unsqueeze(0)

    pred = model(img)[0]
    pred = non_max_suppression(pred, 0.3, 0.6)

    for i, det in enumerate(pred):  # detections per image
        if det is not None and len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img.shape).round()

            for *xyxy, conf, cls in det:
                print(f"{conf.item():.2f} {int(cls.item())} {xyxy}")

if __name__ == "__main__":
    weights = "/path/to/your/custom/weights.pt"  # Specify your custom weights here
    model, device = load_model(weights)
    analyze_image(model, device, "/path/to/image.jpg")