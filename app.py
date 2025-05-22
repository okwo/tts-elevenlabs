from flask import Flask, request, send_file, render_template
from flask_cors import CORS
import os
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv
import tempfile

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert_text():
    data = request.json
    text = data.get("text", "")
    voice = data.get("voice", "Bella")
    speed = float(data.get("speed", 1.0))

    audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        save(audio, tmp_file.name)
        return send_file(tmp_file.name, mimetype="audio/wav")
