from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Accueil", description="Bienvenue sur mon site Flask !")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact", description="Nous contacter")

if __name__ == "__main__":
    app.run(debug=True)
