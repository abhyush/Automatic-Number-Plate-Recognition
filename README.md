# License Plate Recognition using OpenCV and Tesseract

This project implements an automatic license plate recognition (ALPR) system using **OpenCV** for image processing and **Tesseract OCR** for optical character recognition. The system detects and extracts a license plate from an input image and reads the text on it.

---

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [References](#references)

---

## 🌟 Overview
The objective of this project is to develop a Python-based solution that:
1. Detects license plates in vehicle images.
2. Extracts the license plate region.
3. Reads the text on the license plate using **Tesseract OCR**.

This can be used in applications such as vehicle monitoring systems, parking management, and traffic surveillance.

---

## ✨ Features
- **License Plate Detection**: Locates the license plate in the image using contour detection.
- **Image Preprocessing**: Enhances image quality using grayscale conversion, filtering, and edge detection.
- **Text Recognition**: Reads text from the extracted license plate using **Tesseract OCR**.
- **Error Handling**: Handles scenarios where no license plate is detected.

---

## 🛠 Requirements
- Python 3.x
- OpenCV
- imutils
- pytesseract

---

## 🖥 Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/abhyush/license-plate-recognition.git
   cd license-plate-recognition
