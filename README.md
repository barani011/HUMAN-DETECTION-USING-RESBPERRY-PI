Here is a comprehensive `README.md` file incorporating all the details from your document, including the hardware setup, installation steps, code implementation logic, and references found in the later pages of the PDF.

You can copy this directly into GitHub.

```markdown
# Human Detection Using Raspberry Pi

A real-time human detection system implemented on a Raspberry Pi using OpenCV and TensorFlow Lite. [cite_start]This project aims to identify and locate human figures in video streams instantly with minimal delay[cite: 70, 71].

## 📖 Project Overview
[cite_start]Real-time human detection involves identifying human figures in video streams instantly[cite: 2]. [cite_start]While traditional methods use Haar Cascade classifiers for object detection [cite: 3][cite_start], this implementation leverages a **TensorFlow Lite (`.tflite`)** model for efficient inference on edge devices like the Raspberry Pi[cite: 83, 85].

## 🛠️ Hardware Requirements
[cite_start]To replicate this project, the following hardware is required[cite: 31, 72]:
* [cite_start]**Raspberry Pi 4:** Recommended for its improved processing power and memory[cite: 33].
* [cite_start]**Camera Module:** Raspberry Pi Camera Module V2 or a high-quality USB webcam[cite: 37, 38, 76].
* [cite_start]**Monitor:** HDMI monitor for display[cite: 60, 74].
* [cite_start]**Peripherals:** Keyboard, Mouse, and HDMI cable[cite: 47, 62].
* [cite_start]**Storage:** MicroSD card (8 GB minimum)[cite: 43].

## 💻 Software & Libraries
* [cite_start]**Operating System:** Raspberry Pi OS (formerly Raspbian)[cite: 41].
* [cite_start]**Language:** Python 3[cite: 11].
* **Key Libraries:**
    * [cite_start]`cv2` (OpenCV) [cite: 80]
    * [cite_start]`numpy` [cite: 82]
    * [cite_start]`tflite_runtime` [cite: 83]

## ⚙️ Installation & Setup

### 1. OS Installation
1.  [cite_start]Download the **Raspberry Pi OS** image from the [official website](https://www.raspberrypi.com/software/)[cite: 55].
2.  [cite_start]Use **Raspberry Pi Imager** to write the OS to your microSD card[cite: 48, 49].
3.  [cite_start]Insert the SD card into the Raspberry Pi and power it on[cite: 46].

### 2. Hardware Connection
1.  [cite_start]**Monitor:** Connect the Raspberry Pi to the monitor using an HDMI cable[cite: 60, 66].
2.  [cite_start]**Power:** Ensure connections are secure before powering on the device to avoid damage[cite: 65].

### 3. Library Installation
[cite_start]Open the terminal on your Raspberry Pi and run the following commands[cite: 8, 12]:
```bash
sudo apt update
sudo apt install python3-opencv  # Install OpenCV
sudo apt install python3-pip     # Install Pip

```

## 🧠 Dataset & Training

If training a custom model, ensure your dataset follows this structure :

* 
**Images:** Varied poses, lighting, and environments .

* 
**Annotations:** Pascal VOC XML or COCO JSON formats.


```text
dataset/
├── images/
│   ├── image1.jpg
│   └── ...
└── annotations/
    ├── image1.xml
    └── ...

```
* 
**Reference Dataset:** [Kaggle Human Detection Dataset](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset).


## 🚀 Implementation Logic

The system uses a `.tflite` model to process video frames. Below is the core logic flow found in the project script :

1. **Load Model:** The TensorFlow Lite interpreter loads `model.tflite` and allocates tensors.


2. **Capture Video:** `cv2.VideoCapture(0)` initiates the webcam stream.


3. **Preprocessing:** Frames are resized and dimensions expanded to match the model input.


4. **Inference:** The interpreter runs the model on the input frame.


5. **Post-Processing:**
* The script extracts bounding boxes, classes, and confidence scores.
* It filters results using a confidence threshold (e.g., > 0.5).
* Green bounding boxes are drawn around detected humans using `cv2.rectangle`.

6. **Display:** The processed frame is shown in a window named 'Human Detection'.

### Running the Code
Save your Python script (e.g., `main.py`) and the `.tflite` model in the same directory, then run:

```bash
python3 main.py

```
(Press 'q' to exit the video loop )

## 🔗 References & Credits

**Pi OS Software:** [raspberrypi.com/software](https://www.raspberrypi.com/software/) 

**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset) 

* **Video Tutorials:**
 
[YouTube Ref 1](https://www.google.com/search?q=https://youtu.be/kX6zWqMP9U4) 

* 
[YouTube Ref 2](https://www.google.com/search?q=https://youtu.be/iOTWZI4RHA8) 

* 
[YouTube Ref 3](https://www.google.com/search?q=https://youtu.be/HnjGunbK4u8) 

## 📄 License

This project is open for educational use.

```
