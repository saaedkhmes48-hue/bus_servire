from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return "Server is running"

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No image", 400

    img = request.files["image"]
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    img.save(os.path.join(UPLOAD_FOLDER, filename))

    print(f"Image received: {filename}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
