import os
from flask import Flask, request, send_file, render_template
from flask_cors import CORS
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv

load_dotenv()  # โหลดค่าจาก .env
set_api_key(os.getenv("ELEVEN_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    data = request.get_json()
    text = data.get("text", "")
    speed = float(data.get("speed", 1.0))  # ยังไม่ได้ใช้ความเร็วตรงนี้ แต่เผื่อในอนาคต

    voice = "Bella"  # เปลี่ยนชื่อเสียงได้ เช่น Antoni, Rachel, Adam ฯลฯ

    audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")

    output_path = "output.wav"
    save(audio, output_path)

    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run()
