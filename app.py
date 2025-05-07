from flask import Flask, render_template
import requests
import asyncio
import time
app = Flask(__name__)

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
@app.route('/echquier')
def echquier():
    # code pour afficher l'échiquier
    return render_template('echquier.html')
async def keep_alive():
    requests.get(URL)
    await asyncio.sleep(60)
if __name__ == "__main__":
    app.run(debug=True)
    keep_alive()
