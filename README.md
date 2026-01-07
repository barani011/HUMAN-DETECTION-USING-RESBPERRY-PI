# Human Detection Using Raspberry Pi

This project implements a real-time human detection system using a Raspberry Pi and OpenCV. It is designed to identify and locate human figures in video streams instantly with minimal delay, utilizing object detection algorithms like Haar Cascade classifiers.

## 📖 Overview

[cite_start]**Real-time human detection** refers to the ability to identify and locate human figures in images or video streams instantly or with minimal delay[cite: 2].

While this project focuses on human detection, it utilizes concepts similar to **Haar Cascade classifiers**, a type of object detection algorithm used to identify objects in images or video streams. [cite_start]They are particularly known for face detection but can be trained to detect various types of objects[cite: 3, 4].

## ⚙️ Requirements

### [cite_start]1. Hardware Requirements [cite: 31]
* [cite_start]**Raspberry Pi Model:** Raspberry Pi 4 is recommended due to its improved processing power and memory[cite: 33].
* **Camera:** A good quality camera module is essential. [cite_start]The **Raspberry Pi Camera Module V2** or a USB webcam with good resolution will suffice[cite: 37, 38].
* **Peripherals:** Monitor (HDMI), Keyboard, Mouse.
* [cite_start]**Storage:** MicroSD card (at least 8 GB recommended)[cite: 43].

### [cite_start]2. Software & Libraries [cite: 6]
* [cite_start]**OS:** Raspberry Pi OS (formerly Raspbian)[cite: 41].
* [cite_start]**Language:** Python 3 (Recommended for modern applications)[cite: 11].
* **Libraries:**
    * OpenCV (`opencv-python3`)

### [cite_start]3. Data Requirements (For Custom Training) [cite: 13]
If you intend to train a custom model, you need a substantial dataset of annotated images including:
* [cite_start]**Varied Poses:** People in different orientations[cite: 18].
* [cite_start]**Lighting:** Various lighting conditions for robustness[cite: 19].
* [cite_start]**Environments:** Diverse backgrounds[cite: 20].
* [cite_start]**Annotations:** Bounding boxes (Pascal VOC XML or COCO JSON)[cite: 21, 22].

#### [cite_start]Dataset Structure [cite: 23-30]
```text
dataset/
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── annotations/
    ├── image1.xml
    ├── image2.xml
    └── ...
