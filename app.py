from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# مفتاحك الجديد اللي شغال
API_KEY = "AIzaSyCz301UpllEDgFOD5vp-9Iay8-8THJ_L-E"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_data = request.json
    user_message = user_data.get("message")
    
    payload = {
        "contents": [{"parts": [{"text": f"أنت BOGY AI، مساعد ذكي من تطوير الإمبراطور بوجي. أجب بالعربية على: {user_message}"}]}]
    }
    
    try:
        response = requests.post(GEMINI_URL, json=payload)
        return jsonify(response.json())
    except:
        return jsonify({"error": "سيرفر بوجي واجه مشكلة"})

if __name__ == '__main__':
    app.run(debug=True)

