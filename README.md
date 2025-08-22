# Ultralytics YOLO Projects 🚀

This repository contains an implementation of **YOLOv8 (You Only Look Once, version 8)** for real-time object detection, tracking, segmentation, and pose estimation on images and videos.  
The project demonstrates how to use the **Ultralytics YOLO library** with custom Python scripts, **OpenCV integration**, and **COCO class labels**.

---

## 📂 Project Structure
Ultralytics-Yolo-Projects/
│── Utils/ # Utility files (e.g., coco.txt for class names)
│── runs/detect/ # YOLO detection outputs (saved images/videos)
│── weights/ # Pretrained YOLO model weights
│── YoloV8_Video.py # Object detection on video
│── YoloV8_img.py # Object detection on images
│── object_detection.py # Basic YOLO detection script
│── object_tracking.py # Multi-object tracking with YOLO
│── object_segmentation.py # Object segmentation using YOLO
│── object_counting.py # Object counting with YOLO
│── pose_estimation.py # Human pose estimation
│── workout_detection.ipynb # Example Jupyter Notebook
│── yolov8n.pt # YOLOv8 pretrained model
│── yolov8n-seg.pt # YOLOv8 segmentation model
│── yolov8n-pose.pt # YOLOv8 pose estimation model
│── LICENSE # MIT License

## ⚡ Features
- ✅ Real-time object detection (images & videos)  
- ✅ Object tracking with OpenCV  
- ✅ Object segmentation  
- ✅ Pose estimation (human joints & skeletons)  
- ✅ Object counting  
- ✅ Pre-trained YOLOv8 models included  

## 🔧 Installation
```bash
git clone https://github.com/aniket20-99/Ultralytics-Yolo-Projects.git
cd Ultralytics-Yolo-Projects
pip install ultralytics opencv-python numpy

📊 Results

- All detection results will be saved automatically in the runs/detect/ folder.

- Example outputs include bounding boxes, class labels, segmentation masks, and pose keypoints.

📜 License

- This project is licensed under the MIT License – see the LICENSE
  file for details.

🙌 Acknowledgements

- Ultralytics YOLOv8

- OpenCV community

- COCO dataset for class labels

🚀 Happy experimenting with YOLOv8!
