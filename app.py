from flask import Flask, request, render_template
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("static/voice.mp3")
    return "success"

if __name__ == '__main__':
    app.run(debug=True)
