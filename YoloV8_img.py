from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt","V8")
detection_output = model.predict(source = r"E:\\Image-Data\\Yolo-Detection-1.jpg",conf = 0.25,save = True)
print(detection_output)
# print(detection_output[0].numpy())q