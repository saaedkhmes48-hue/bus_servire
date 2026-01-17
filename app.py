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
    if not request.data:
        return "No image", 400
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    with open(os.path.join(UPLOAD_FOLDER, filename), "wb") as f:
        f.write(request.data)
    print("Image received")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
