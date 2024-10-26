from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Verzeichnis für heruntergeladene Videos
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download(output_path=DOWNLOAD_FOLDER)
        
        # Nach dem Herunterladen wird der Benutzer zur Download-Seite weitergeleitet
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
