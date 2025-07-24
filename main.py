import time
import threading
from datetime import datetime
import requests
from flask import Flask

# Telegram credentials
BOT_TOKEN = '8347188783:AAF0IMvlnvvY6RI2nh6LClyntfi7OZr0u9c'
CHAT_ID = 6441176243

# Messages personnalisés
messages = {
    "lust_control": (
        "CONTROL YOURSELF ! PLEASE\n"
        "Est-ce que tu ressens une envie ? Respire calmement 3 secondes… expire 3 secondes… récite ton mantra.\n"
        "Ce n’est pas une dépendance, c’est ta force qui reprend le dessus. Tu veux être libre, tu contrôles ça, pas l’inverse.\n"
        "Reste dans ta forme idéale. 💪"
    ),
    "sport": (
        "DO SPORTS ! YOU ARE SKINNY ASF\n"
        "Regarde-toi dans le miroir : tu construis un corps fort, pas juste mince.\n"
        "Chaque mouvement aujourd’hui est un investissement pour ta longévité.\n"
        "Tu veux vivre pleinement. Lève-toi, bouge, ressens ton pouvoir. 🏋️‍♂️"
    ),
    "project_time": (
        "WANNA FAIL YOUR DREAMS ? THEN WORK !!\n"
        "Astrophysicien en devenir : chaque minute que tu consacres te rapproche de ton rêve.\n"
        "Construis tes projets comme un architecte de ta vie, le succès suivra.\n"
        "Gagne en focus, avance pas à pas. 🚀"
    )
}

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    res = requests.post(url, data=payload)
    now = datetime.now().strftime('%H:%M:%S')
    print(f"[{now}] {res.status_code} - Sent: {text[:30]}...")
    if res.status_code != 200:
        print("Error:", res.text)

def reminder_loop():
    counter = 0
    while True:
        time.sleep(60)
        counter += 1

        if counter % 15 == 0:
            send_message(messages["project_time"])
        elif counter % 10 == 0:
            send_message(messages["sport"])
        elif counter % 5 == 0:
            send_message(messages["lust_control"])

        if counter >= 60:
            counter = 0

# Start reminder thread
threading.Thread(target=reminder_loop, daemon=True).start()

# Flask healthcheck endpoint
app = Flask(__name__)

@app.route('/')
@app.route('/healthz')
def health_check():
    return "Bot is alive! ✅", 200
