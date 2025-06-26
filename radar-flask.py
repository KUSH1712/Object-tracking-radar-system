# app.py

# app.py
from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)
DATA_FILE = "radar_data.csv"

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.get_json(force=True)
        angle = data.get("angle")
        distance = data.get("distance")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"📨 Received: Angle={angle}, Distance={distance}cm at {timestamp}")

        df = pd.DataFrame([[timestamp, angle, distance]], columns=["timestamp", "angle", "distance"])
        df.to_csv(DATA_FILE, mode='a', header=not os.path.exists(DATA_FILE), index=False)
        return jsonify({"status": "ok"})
    
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
