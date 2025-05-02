from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Mon Site SEO", description="Un site Flask déployé sur Render et référencé sur Google.")

if __name__ == "__main__":
    app.run(debug=True)
