Import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()
# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
# Initialize video capture
cap = cv2.VideoCapture(0)
while True:
ret, frame = cap.read()
if not ret:
break
# Preprocess the image
input_data = np.expand_dims(frame, axis=0).astype(np.float32)
# Set input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)
# Run inference
interpreter.invoke()
# Get output tensor
boxes = interpreter.get_tensor(output_details[0]['index'])
classes = interpreter.get_tensor(output_details[1]['index'])
scores = interpreter.get_tensor(output_details[2]['index'])
# Post-process and display results
for i in range(len(scores[0])):
if scores[0][i] > 0.5: # Confidence threshold
box = boxes[0][i]
class_id = int(classes[0][i])
y1, x1, y2, x2 = box
(h, w, _) = frame.shape
y1, x1, y2, x2 = int(y1 * h), int(x1 * w), int(y2 * h), int(x2 * w)
cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.putText(frame, f'Class {class_id} ({scores[0][i]:.2f})', (x1, y1 - 10),
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
# Display the resulting frame
cv2.imshow('Human Detection', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release()
cv2.destroyAllWindows()
