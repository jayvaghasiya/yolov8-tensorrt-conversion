# yolov8-tensorrt-conversion
With the help of this repo you can convert the trained yolov8 model to tensorrt.

## Steps:

  1. Install dependencies:
     1. Install `CUDA` follow [`CUDA official website`](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#download-the-nvidia-cuda-toolkit).

       🚀 RECOMMENDED `CUDA` >= 11.4

    2. Install `TensorRT` follow [`TensorRT official website`](https://developer.nvidia.com/nvidia-tensorrt-8x-download).

       🚀 RECOMMENDED `TensorRT` >= 8.4
       
    3. Install python requirements.

      ``` shell
      pip install -r requirements.txt
      ```
  
  2. Convert trained yolov8 model to onnx:
     Run this command : ```python3 export-det.py --weights path/to/best.pt --iou-thres 0.65 --conf-thres 0.25 --topk 100 --opset 11 --sim --input-shape 1 3 480 736 --device cuda:0```

  3. Convert onnx model to tensorrt:
     Run this command : ```python3 export.py -o path/to/best.onnx -e ./best.trt -p fp16```

     Note: you can change the floating point (fp) as per you requirements like (fp32, fp16, int8).
