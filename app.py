from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Accueil")

@app.route('/regles')
def regles():
    return render_template('regles.html', title="Règles du jeu")

@app.route('/strategies')
def strategies():
    return render_template('strategies.html', title="Stratégies")

@app.route('/jouer')
def jouer():
    return render_template('jouer.html', title="Jouer")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

if __name__ == '__main__':
    app.run(debug=True)
