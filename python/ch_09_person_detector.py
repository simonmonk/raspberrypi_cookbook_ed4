import argparse
import sys
import time, datetime

import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

model = 'efficientdet_lite0.tflite'
camera_id = 0
width = 640
height = 480
num_threads = 4

# Start capturing video input from the camera
cap = cv2.VideoCapture(camera_id)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Visualization parameters
row_size = 20  # pixels
left_margin = 24  # pixels
text_color = (0, 0, 255)  # red
font_size = 1
font_thickness = 1
fps_avg_frame_count = 10

# Initialize the object detection model
base_options = core.BaseOptions(
    file_name=model, use_coral=False, num_threads=num_threads)
detection_options = processor.DetectionOptions(
    max_results=3, score_threshold=0.3)
options = vision.ObjectDetectorOptions(
    base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)

last_detection_time = 0

# Continuously capture images from the camera and run inference
while cap.isOpened():
  success, image = cap.read()
  if not success:
    sys.exit(
        'ERROR: Unable to read from webcam. Please verify your webcam settings.'
    )
  image = cv2.flip(image, 1)

  # Convert the image from BGR to RGB as required by the TFLite model.
  rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # Create a TensorImage object from the RGB image.

  input_tensor = vision.TensorImage.create_from_array(rgb_image)

  # Run object detection estimation using the model.
  detection_result = detector.detect(input_tensor)

  # Draw keypoints and edges on input image
  image = utils.visualize(image, detection_result)

  for detection in detection_result.detections:
      object_type = detection.categories[0].category_name
      time_now = time.time()
      if object_type == 'person' and time_now > last_detection_time + 10:
        print("***********************************")
        print("Person Detected!")
        print("***********************************")
        # do your own thing here !
        last_detection_time = time_now
        ts = "{:%Y-%m-%d-%H-%M-%S}".format(datetime.datetime.now())
        cv2.imwrite(ts + ".png", image)

  # Stop the program if the ESC key is pressed.
  if cv2.waitKey(1) == 27:
    break

cap.release()
cv2.destroyAllWindows()