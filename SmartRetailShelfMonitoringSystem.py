# -----------------------------
# 2️⃣ Import Libraries
# -----------------------------
import cv2
from ultralytics import YOLO
import os
import tkinter as tk
from PIL import Image, ImageTk

# -----------------------------
# 3️⃣ Video File
# -----------------------------
video_filename = "sample_video.mp4"  # Your downloaded video file

# -----------------------------
# 4️⃣ Load Pre-trained YOLOv8 Model
# -----------------------------
model = YOLO("yolov8n.pt")  # Pre-trained YOLOv8 nano model
LOW_STOCK_THRESHOLD = 3  # Low stock alert threshold

# -----------------------------
# 5️⃣ GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Smart Retail Shelf Monitoring")
root.geometry("1000x600")

# Video frame
video_label = tk.Label(root)
video_label.pack(side="left")

# Sidebar for product counts
sidebar = tk.Frame(root, width=300)
sidebar.pack(side="right", fill="y")
sidebar_title = tk.Label(sidebar, text="Shelf Stock Report", font=("Arial", 16, "bold"))
sidebar_title.pack(pady=10)
product_text = tk.Text(sidebar, width=40, height=35, font=("Arial", 12))
product_text.pack()

# -----------------------------
# 6️⃣ Open Video
# -----------------------------
cap = cv2.VideoCapture(video_filename)
paused = False

def toggle_pause():
    global paused
    paused = not paused
    pause_btn.config(text="Play" if paused else "Pause")

def quit_app():
    cap.release()
    root.destroy()

pause_btn = tk.Button(sidebar, text="Pause", command=toggle_pause)
pause_btn.pack(pady=5)
quit_btn = tk.Button(sidebar, text="Quit", command=quit_app)
quit_btn.pack(pady=5)

# -----------------------------
# 7️⃣ Video Update Loop
# -----------------------------
def update_frame():
    if not paused:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))  # Resize for faster processing

            # YOLO Detection
            results = model(frame, verbose=False)
            annotated_frame = results[0].plot()

            # Shelf Monitoring Logic
            product_counts = {}
            for cls in results[0].boxes.cls:
                label = model.names[int(cls)]
                product_counts[label] = product_counts.get(label, 0) + 1

            # Update sidebar safely
            product_text.delete("1.0", tk.END)
            for product, count in product_counts.items():
                color = "green"
                if count <= LOW_STOCK_THRESHOLD:
                    color = "red" if count == 0 else "orange"
                product_text.insert(tk.END, f"{product}: {count}\n")

                # Create safe tag (replace spaces/special chars)
                safe_tag = "".join(c if c.isalnum() else "_" for c in product)
                line_start = f"{product_text.index('end')} linestart -1l"
                line_end = f"{product_text.index('end')} lineend -1c"
                product_text.tag_add(safe_tag, line_start, line_end)
                product_text.tag_config(safe_tag, foreground=color)

            # Convert frame to Tkinter image
            frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop video

    video_label.after(30, update_frame)  # Update every 30ms

update_frame()
root.mainloop()