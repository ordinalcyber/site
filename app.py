from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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

if __name__ == "__main__":
    app.run(debug=True)
