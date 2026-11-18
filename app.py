from flask import Flask, send_from_directory, jsonify, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
D = "music"
CODE = "change-moi"   # <- change ce code !
EXT = (".mp3", ".m4a", ".ogg", ".wav")
os.makedirs(D, exist_ok=True)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()

@app.route("/api/songs")
def songs():
    return jsonify(sorted(f for f in os.listdir(D) if f.lower().endswith(EXT)))

@app.route("/music/<path:f>")
def music(f):
    return send_from_directory(D, f)

@app.route("/api/upload", methods=["POST"])
def upload():
    if request.form.get("code") != CODE:
        return jsonify(error="Code incorrect"), 403
    f = request.files.get("file")
    if not f or not f.filename.lower().endswith(EXT):
        return jsonify(error="Fichier invalide"), 400
    f.save(os.path.join(D, secure_filename(f.filename)))
    return jsonify(ok=True)

app.run(host="0.0.0.0", port=5000)
