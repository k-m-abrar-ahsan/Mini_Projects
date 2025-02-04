from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the script directory

@app.route('/run-music-player', methods=['POST'])
def run_music_player():
    music_path = os.path.join(BASE_DIR, "Music_Player", "music_player.py")
    if os.path.exists(music_path):
        subprocess.Popen(["python", music_path], shell=True)
        return jsonify({"message": "Music Player Started"}), 200
    return jsonify({"error": "Music Player script not found"}), 404

@app.route('/run-ttt', methods=['POST'])
def run_ttt():
    ttt_path = os.path.join(BASE_DIR, "TTT", "ttt.py")
    if os.path.exists(ttt_path):
        subprocess.Popen(["python", ttt_path], shell=True)
        return jsonify({"message": "Tic-Tac-Toe Started"}), 200
    return jsonify({"error": "Tic-Tac-Toe script not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
