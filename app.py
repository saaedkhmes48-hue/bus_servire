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

    image = request.files["image"]
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    image.save(os.path.join(UPLOAD_FOLDER, filename))

    print("Image received")
    return "OK", 200


app.run(host="0.0.0.0", port=10000)
