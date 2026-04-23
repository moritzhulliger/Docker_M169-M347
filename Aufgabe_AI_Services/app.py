import os
import time
import requests
from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

OCR_SERVICE_URL = "http://DEINE_AUFGABE:5000/ocr"
LLM_CORRECTION_URL = "http://DEINE_AUFGABE:11434/api/generate"
LLM_TRANSLATION_URL = "http://DEINE_AUFGABE:11434/api/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "Kein Bild hochgeladen"}), 400
        
        file = request.files['image']
        file.seek(0)

        total_start = time.perf_counter()

        ocr_start = time.perf_counter()
        ocr_response = requests.post(
            OCR_SERVICE_URL,
            files={'file': (file.filename, file.stream, file.content_type)}
        )
        ocr_end = time.perf_counter()

        print(f"Status: {ocr_response.status_code}")
        print(f"Content: {ocr_response.text}") # Das zeigt dir, was wirklich zurückkam

        raw_text = None
        if ocr_response.status_code == 200:
            raw_text = ocr_response.json().get('text')

        if not raw_text:
            return jsonify({"error": "Kein Text im Bild erkannt"}), 500

        correction_start = time.perf_counter()
        correction_prompt = f"DEINE_AUFGABE {raw_text}"
        brain_response = requests.post(LLM_CORRECTION_URL, json={
            "model": "DEINE_AUFGABE",
            "prompt": correction_prompt,
            "stream": False
        })
        corrected_text = brain_response.json().get('response', '')
        correction_end = time.perf_counter()

        target_lang = 'German'
        translation_start = time.perf_counter()
        translation_prompt = f"DEINE_AUFGABE {target_lang}: {corrected_text}"
        tongue_response = requests.post(LLM_TRANSLATION_URL, json={
            "model": "DEINE_AUFGABE",
            "prompt": translation_prompt,
            "stream": False
        })
        final_translation = tongue_response.json().get('response', '')
        translation_end = time.perf_counter()

        total_end = time.perf_counter()

        return jsonify({
            "status": "success",
            "ocr": raw_text,
            "raw": raw_text,
            "corrected": corrected_text,
            "translated": final_translation,
            "times": {
                "ocr": f"{ocr_end - ocr_start:.2f}s",
                "correction": f"{correction_end - correction_start:.2f}s",
                "translation": f"{translation_end - translation_start:.2f}s",
                "total": f"{total_end - total_start:.2f}s"
            }
        })

    except requests.exceptions.ConnectionError as e:
        return jsonify({"error": f"Verbindungsfehler: Ein Container ist nicht erreichbar ({e})"}), 503
    except Exception as e:
        return jsonify({"error": f"Ein Fehler ist aufgetreten: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)