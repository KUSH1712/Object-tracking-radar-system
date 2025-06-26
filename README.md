# 📡 Object Tracking Radar System using ESP32

A real-time object detection and radar-style tracking system using an **ESP32** microcontroller, **ultrasonic sensor**, and a live **web-dashboard powered by Flask and Streamlit**. The project simulates a sweeping radar to track objects' distance and angular position.
---

## 🎯 Project Purpose

This project demonstrates how **IoT and real-time visualization** can be combined for **object tracking** and **smart sensing**. The radar system mimics military or industrial radar, sweeping across angles and logging detected objects’ distances. Ideal for:
- Smart obstacle detection
- Robotic navigation
- Factory automation

---

## 🧰 Components Used

| Component              | Description                                |
|------------------------|--------------------------------------------|
| ESP32 Dev Module       | WiFi-enabled microcontroller               |
| Ultrasonic Sensor (HC-SR04) | For distance measurement                 |
| Jumper wires           | To connect components                      |
| Breadboard             | For prototyping                            |


---

## 💻 Software Used

| Tool/Library    | Purpose                          |
|------------------|----------------------------------|
| Arduino IDE      | Programming ESP32                |
| Python 3.8+      | Backend and dashboard            |
| Flask            | REST API to receive sensor data  |
| Streamlit        | Dashboard to display live data   |
| Pandas, Plotly   | Data handling and radar chart    |
| Git & GitHub     | Version control and sharing      |

---

## ⚙️ Workflow

1. **ESP32** measures distance from ultrasonic sensor.
2. It simulates a radar sweep using an array of angles.
3. At each angle, the ESP32 sends a **JSON POST** request via WiFi to the **Flask server**.
4. Flask logs data into a `.csv` file.
5. **Streamlit** reads the data and renders a live **radar-style polar plot** showing object positions based on angle and distance.

---

## 📡 Working of Ultrasonic Sensor (HC-SR04)

- Sends a 40kHz ultrasonic pulse using the **trigger pin**.
- Measures the time for the **echo** to return.
- Calculates distance using the formula:

distance = (time × speed of sound) / 2

- Range: **2 cm to 400 cm**  
- Accuracy: ±3 mm  
- Works best in a cone-like directional field

---

## 🖼️ Project Visuals

### 🔌 Circuit Diagram
![Circuit Diagram](project-visuals/ckt-diagram.png)

### 📊 Web Dashboard (Streamlit)
![Web Dashboard](project-visuals/web-dashboard.png)

---

## 🌟 Impact & Real-World Applications

- Demonstrates **real-time data streaming** from hardware to dashboard
- Can be expanded to include **alerts** (SMS, buzzer) if objects are too close
- Teaches **network communication**, **sensor interfacing**, and **data visualization**
- Forms the base for **autonomous robots**, **smart security systems**, and **industrial automation**

---

## 🚀 Future Enhancements

✅ Servo motor integration for physical radar sweeping  
✅ Add object classification using **IR sensors or ML models**  
✅ Upgrade visualization to **3D or rotating radar display**  

---

## 📂 Folder Structure

Ultrasonic_radar_system/
├── esp32_code.ino
├── radar_flask.py
├── radar_streamlit.py
├── radar_data.csv
├── project-visuals/
│ ├── ckt-diagram.png
│ └── web-dashboard.png
├── README.md
└── requirements.txt

