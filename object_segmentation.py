import cv2
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video v stram.")
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: could not read frame.")
        break
    
    results = model(frame)
    
    annotated_frame = results[0].plot()
    cv2.imshow('YOLOV8 Object segementation', annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    