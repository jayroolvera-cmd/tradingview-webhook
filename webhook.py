from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def recibir_alerta():
    data = request.json
    mensaje = data.get("message", "📈 ¡Alerta recibida desde TradingView!")
    enviar_mensaje_telegram(mensaje)
    return "OK", 200

def enviar_mensaje_telegram(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run()
