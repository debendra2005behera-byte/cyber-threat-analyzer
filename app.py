from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Replace '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' with your actual Groq key (starts with gsk_)
import os
client = Groq(api_key='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')

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/analyze/email', methods=['POST'])
def analyze_email():
    data = request.get_json()
    email_text = data.get('text', '')
    if not email_text:
        return jsonify({'error': 'No email text provided'}), 400
    prompt = """You are a senior cybersecurity analyst specializing in phishing detection.
Analyze the following email for phishing indicators and threats.

EMAIL TO ANALYZE:
""" + email_text + """

Respond in this EXACT format:

THREAT LEVEL: [SAFE / LOW / MEDIUM / HIGH / CRITICAL]

SUMMARY:
[2-3 sentences about this email]

RED FLAGS FOUND:
[List each red flag starting with - ]

RECOMMENDATION:
[What should the user do?]

CONFIDENCE: [percentage]"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        result = response.choices[0].message.content
        return jsonify({'analysis': result, 'type': 'email'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze/url', methods=['POST'])
def analyze_url():
    data = request.get_json()
    url_text = data.get('text', '')
    if not url_text:
        return jsonify({'error': 'No URL provided'}), 400
    prompt = """You are a senior cybersecurity analyst specializing in malicious URL detection.
Analyze the following URL for security threats.

URL TO ANALYZE:
""" + url_text + """

Respond in this EXACT format:

THREAT LEVEL: [SAFE / LOW / MEDIUM / HIGH / CRITICAL]

SUMMARY:
[2-3 sentences about this URL]

RED FLAGS FOUND:
[List each red flag starting with - ]

RECOMMENDATION:
[Should the user visit this URL?]

CONFIDENCE: [percentage]"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        result = response.choices[0].message.content
        return jsonify({'analysis': result, 'type': 'url'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze/log', methods=['POST'])
def analyze_log():
    data = request.get_json()
    log_text = data.get('text', '')
    if not log_text:
        return jsonify({'error': 'No log data provided'}), 400
    prompt = """You are a senior cybersecurity analyst and network security expert.
Analyze the following network log for security threats.

NETWORK LOG TO ANALYZE:
""" + log_text + """

Respond in this EXACT format:

THREAT LEVEL: [SAFE / LOW / MEDIUM / HIGH / CRITICAL]

SUMMARY:
[2-3 sentences about this log]

SUSPICIOUS ACTIVITY FOUND:
[List each suspicious event starting with - ]

RECOMMENDATION:
[What security actions should be taken?]

CONFIDENCE: [percentage]"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        result = response.choices[0].message.content
        return jsonify({'analysis': result, 'type': 'log'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("  Cyber Threat Analyzer is RUNNING!")
    print("  Open your browser and go to:")
    print("  http://localhost:5000")
    print("=" * 50)
    app.run(host='0.0.0.0', port=10000)
