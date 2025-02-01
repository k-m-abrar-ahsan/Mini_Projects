from flask import Flask
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Requests

@app.route('/run-music-player', methods=['POST'])
def run_music_player():
    subprocess.Popen(["python", "Music_Player/music_player.py"])  # Corrected path
    return "Music Player Started", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
