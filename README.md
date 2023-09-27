# yolov8-tensorrt-conversion
With the help of this repo you can convert the trained yolov8 model to tensorrt.

## Steps:

  1. Install dependencies:
     Run this command: `pip install -r requirements.txt`
  
  2. Convert trained yolov8 model to onnx:
     Run this command : `python export-onnx.py --model /path/to/best.pt`

  3. Convert onnx model to tensorrt:
     Run this command : `python build-trt.py --weights /path/to/best.onnx --iou-thres 0.65 --conf-thres 0.25 --topk 100 --fp16  --device cuda:0`

     Note: you can change the parameters like floating point (fp) as per you requirements like (fp32, fp16, int8).
