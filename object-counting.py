import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt",'V8')

# Initialize the video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Error: Could not open video stream.')
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        print('Error: Could not read frame.')
        break
    
    # Perform inference on the frame
    results = model(frame)
    
    # Count the number of detected objects
    object_num = len(results[0].boxes)
    
    # Annotate the frame with the count
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame,f'Count:{object_num}',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.imshow('YOLOv8 Object Counting', annotated_frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 

https://github.com/aniket20-99/Ultralytics-Yolo-Projects.git