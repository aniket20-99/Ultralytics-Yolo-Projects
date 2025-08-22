import cv2
from ultralytics import YOLO

# Load the Yolov8 model trained for customer detection
model = YOLO('yolov8n.pt','V8')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Perform inference on the frame
    results = model(frame)
    
    # Annotate the frame with detection results
    annotated_frame = results[0].plot()
    
    # Display the annotated frame
    cv2.imshow('YOLOv8 Custom Detection', annotated_frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()