from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model',
                type=str,
                required=True,
                help='path to best.pt')
                
args = parser.parse_args()

print(args.model)

model = YOLO(args.model) 
model.export(format="onnx", imgsz=[960,147])
