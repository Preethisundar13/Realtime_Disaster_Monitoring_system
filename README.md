# 🌍 Real-Time Disaster Monitoring System using YOLOv8

## 📌 Project Overview

The **Real-Time Disaster Monitoring System** is an AI-powered web application developed to detect natural disasters from aerial and satellite images using the **YOLOv8 object detection model**. The system provides real-time disaster classification, visualizes affected locations on an interactive map, and automatically sends SMS alerts to emergency contacts using **Twilio**.

The project is developed using **Python**, **Streamlit**, and **Google Colab**, providing an easy-to-use interface for disaster monitoring and emergency response.

---

## 🚀 Features

- 🌪️ Real-time disaster detection using **YOLOv8**
- 🛰️ Supports satellite and drone image analysis
- 📊 Interactive **Streamlit Dashboard**
- 📍 Live location mapping of detected disasters
- 📩 Automatic SMS alerts using **Twilio API**
- 📈 Detection confidence scores
- 📄 JSON-based storage of prediction results
- 🖼️ Upload and analyze custom images
- ⚡ Fast and user-friendly interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| AI Model | YOLOv8 |
| Framework | Streamlit |
| Computer Vision | OpenCV |
| Machine Learning | Ultralytics YOLO |
| Alert System | Twilio API |
| Mapping | Folium / Streamlit Map |
| Data Format | JSON |
| Development Environment | Google Colab |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
Real-Time-Disaster-Monitoring-System/
│
├── app.py
├── watcher.py
├── requirements.txt
├── Disaster_classifier.ipynb
├── run_dashboard.bat
├── locations.json
├── results.json
├── alert_log.txt
│
├── Datasets/
├── Test images/
├── Results/
├── Final results/
├── Yamls/
│
├── screenshots/
│
└── Project_Report.pdf
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Real-Time-Disaster-Monitoring-System.git
```

### Move to Project Folder

```bash
cd Real-Time-Disaster-Monitoring-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🔄 System Workflow

```
Input Image
      │
      ▼
YOLOv8 Disaster Detection
      │
      ▼
Disaster Classification
      │
      ▼
Display Results on Streamlit Dashboard
      │
      ├────────► Live Location Mapping
      │
      └────────► SMS Alert using Twilio
```

---

## 🎯 Supported Disaster Classes

- Flood
- Fire
- Landslide
- Cyclone
- Earthquake Damage
- Other disaster categories included in the trained dataset

---

## 📷 Project Screenshots

### Dashboard
(Add screenshot here)

### Disaster Detection Output
(Add screenshot here)

### Live Location Mapping
(Add screenshot here)

### SMS Alert
(Add screenshot here)

---

## 📊 Results

The trained YOLOv8 model successfully detects multiple disaster categories with confidence scores and provides:

- Accurate disaster localization
- Real-time visualization
- Instant SMS notification
- Interactive location mapping
- Efficient emergency response support

---

## 🔮 Future Enhancements

- Live CCTV integration
- Drone video streaming
- Weather API integration
- Mobile application
- Cloud deployment
- Real-time satellite image monitoring
- AI-based disaster severity prediction

---

## 👩‍💻 Developed By

**Preethi Sundar**

BE Electronics and Communication Engineering

AI & Python Developer

LinkedIn:
https://www.linkedin.com/in/preethi-sundar-a209a32b0

Email:
preethisundar2004@gmail.com

---

## 📜 License

This project was developed as a Final Year Engineering Project for academic and learning purposes.

