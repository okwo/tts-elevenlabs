import os
from flask import Flask, request, send_file
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

app = Flask(__name__)

@app.route("/api/convert", methods=["POST"])
def convert_text():
    data = request.json
    text = data.get("text", "")
    voice = "Bella"  # สามารถเปลี่ยนเป็น "Antoni", "Rachel", "Adam" หรืออื่นๆ
    speed = float(data.get("speed", 1.0))

    audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")

    output_path = "output.wav"
    save(audio, output_path)
    return send_file(output_path, mimetype="audio/wav")
