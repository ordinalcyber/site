from flask import Flask, render_template
import requests
import asyncio
import random
import time
app = Flask(__name__)
questions = [
    {
        "image": "static/screenshot/1.png",  # Le nom du fichier image
        "correct_answer": "rb1",  # La réponse correcte à cette image
    },
    {
        "image": "static/screenshot/2.png",
        "correct_answer": "qg2",
    },
    {
        "image": "static/screenshot/3.png",
        "correct_answer": "nxe4",
    },
    {
        "image": "static/screenshot/4.png",
        "correct_answer": "rc7",
    },
    {
        "image": "static/screenshot/5.png",
        "correct_answer": "rh3",
    },
    # Ajoute d'autres questions si besoin
]
@app.route("/")
def index():
    return render_template("index.html")
URL = "https://apprendre-les-echecs.onrender.com"
@app.route("/debutant")
def debutant():
    return render_template("debutant.html")

@app.route("/intermediaire")
def intermediaire():
    return render_template("intermediaire.html")

@app.route("/expert")
def expert():
    return render_template("expert.html")
@app.route("/ouvertures")
def ouvertures():
    return render_template("ouvertures.html")
@app.route("/coaching")
def coaching():
    return render_template("coaching.html")
@app.route('/echiquier', methods=["GET", "POST"])
def echiquier():
    question = random.choice(questions)

    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()

        if user_answer == question["correct_answer"].lower():
            random.shuffle(questions)
            message = "Bravo ! Votre réponse est correcte."
            next_question = random.choice(questions)
            return render_template(
                "echiquier.html",
                message=message,
                image_path=next_question["image"],
                answer="",
                question=next_question
            )
        else:
            message = "Dommage, essayez encore !"
            return render_template(
                "echiquier.html",
                message=message,
                image_path=question["image"],
                answer="",
                question=question
            )

    return render_template(
        "echiquier.html",
        message="Quel est le meilleur coup ?",
        image_path=question["image"],
        answer="",
        question=question
    )
async def keep_alive():
    requests.get(URL)
    await asyncio.sleep(60)
if __name__ == "__main__":
    app.run(debug=True)
    keep_alive()
