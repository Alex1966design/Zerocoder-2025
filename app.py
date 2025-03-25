from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "7598269211:AAH5zTrpyfQ5R1fGUS6M8rSi_vD-GgE_DOI"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route('/')
def index():
    return "Привет от Flask на Render! 🚀"

@app.route('/', methods=['POST'])  # Webhook для Telegram
def webhook():
    data = request.get_json()
    print("Получено сообщение:", data)

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        reply = f"Вы написали: {text}"
        send_message(chat_id, reply)

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)








