# 🛒 Smart Retail Shelf Monitoring with YOLOv8  

This project uses **YOLOv8 (Ultralytics)** for real-time **retail shelf monitoring**.  
It detects products in a video feed, counts them, and provides **low-stock alerts** via a simple **Tkinter GUI**.  

---

## 📌 Features  
- 🎥 Plays a retail shelf **video feed** (looped playback).  
- 🤖 Uses **YOLOv8 object detection** to recognize and count products.  
- 📊 Displays a **live stock report** with product counts.  
- ⚠️ Highlights low stock with **orange** and out-of-stock with **red**.  
- ⏯️ **Pause/Play** video option.  
- ❌ **Quit** button to close the application.  

---

## 🛠️ Requirements  

Make sure you have Python 3.8+ installed. Install dependencies with:  

```bash
pip install ultralytics opencv-python pillow
```
## For Tkinter:

It comes pre-installed with most Python distributions.

On Linux, you may need to install it manually:
```bash
sudo apt-get install python3-tk
```
## 📂 Project Structure  

```bash
smart-retail-shelf
 ├── sample_video.mp4                  # Sample retail shelf video
 ├── SmartRetailShelfMonitoringSystem.py   # Main Python script
 ├── yolov8n.pt                        # YOLOv8 pretrained model (auto-download hota hai agar missing ho)
 └── README.md                         # Project documentation
```
##  🚀 Usage

Place your video file in the project folder and rename it sample_video.mp4 (or update video_filename in the script).

 ## Run the program:
```bash

python SmartRetailShelfMonitoringSystem.py  
```

## The GUI will open with:

Left: Video with YOLO detections

Right: Product count report

 ## 📊 Example Output

✅ Green → Normal stock

🟠 Orange → Low stock (≤ threshold)

🔴 Red → Out of stock

## 📌 Future Improvements

✅ Live CCTV / webcam feed support.

✅ Export stock reports as CSV/Excel.

✅ Integration with alerts (email/SMS) for out-of-stock.

👨‍💻 Author

Developed by Sara Manzoor ✨ kesi h
