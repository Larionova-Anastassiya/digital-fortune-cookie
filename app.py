import os
import random

from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_MOOD = os.getenv("APP_MOOD", "mysterious").lower()
PORT = int(os.getenv("PORT", "5000"))


FORTUNES = {
    "mysterious": [
        "A forgotten idea will return when you need it the most.",
        "The answer you are looking for is closer than it appears.",
        "A quiet decision will change more than a loud one.",
        "Something lost will find its way back to you.",
        "The next door will open only after you stop watching it.",
        "A stranger's words will soon make unexpected sense.",
        "Your next mistake will hide an opportunity.",
        "What seems like an ending is only changing its name.",
        "A small coincidence will lead you somewhere important.",
        "The thing you are avoiding knows the way forward.",
        "You will soon understand why something had to wait.",
        "An unexpected message will change your plans.",
    ],

    "funny": [
        "Your code will work perfectly... immediately after the deadline.",
        "Today is an excellent day to blame the cache.",
        "A mysterious bug will disappear when someone else looks at your screen.",
        "You will find what you lost exactly where you already looked twice.",
        "Your next coffee will contain at least 37% more productivity.",
        "Someone will ask you a question that could have been an email.",
        "You will open the fridge and forget why. Again.",
        "A semicolon somewhere is currently plotting against you.",
        "Your Wi-Fi senses fear. Stay confident.",
        "You will solve a difficult problem five minutes after giving up.",
        "An update will arrive exactly when you don't have time for it.",
        "Your greatest achievement today may be closing unnecessary browser tabs.",
    ],

    "motivational": [
        "Small progress is still progress.",
        "The skill you struggle with today may become your strength tomorrow.",
        "You are closer to your goal than yesterday.",
        "A difficult beginning does not predict the ending.",
        "Your future is built from ordinary decisions made consistently.",
        "Do one thing today that your future self will appreciate.",
        "You do not need perfect conditions to make meaningful progress.",
        "Every expert once had to learn the basics.",
        "The next attempt may be the one that changes everything.",
        "Consistency will take you places motivation cannot.",
        "Your ideas deserve the chance to become real.",
        "Keep going. Progress is often invisible before it becomes obvious.",
    ],
}


@app.route("/")
def home():
    return render_template("index.html", mood=APP_MOOD)


@app.route("/api/fortune")
def get_fortune():
    mood = APP_MOOD

    # Fallback in case an unsupported mood is provided.
    if mood not in FORTUNES:
        mood = "mysterious"

    fortune = random.choice(FORTUNES[mood])
    fortune_id = random.randint(1000, 9999)

    return jsonify(
        {
            "fortune": fortune,
            "mood": mood,
            "id": fortune_id,
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "application": "Digital Fortune Cookie",
            "mood": APP_MOOD,
        }
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=False,
    )