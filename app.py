from flask import Flask, request, send_file, render_template
from flask_cors import CORS
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv
import tempfile
import os

# โหลด .env และตั้ง API KEY
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
    voice = data.get("voice", "Bella")  # รับ voice จาก request
    speed = float(data.get("speed", 1.0))

    # สร้างไฟล์เสียงชั่วคราว
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "output.wav")

        # สร้างเสียงด้วย ElevenLabs
        audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")
        save(audio, output_path)

        return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run()
