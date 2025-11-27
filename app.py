from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", active_page="home")


@app.route("/servicos")
def servicos():
    return render_template("servicos.html", active_page="servicos")


@app.route("/tours")
def tours():
    return render_template("tours.html", active_page="tours")


@app.route("/sobre")
def about():
    return render_template("about.html", active_page="about")


@app.route("/contactos")
def contactos():
    return render_template("contactos.html", active_page="contactos")


if __name__ == "__main__":
    # Apenas para correr em local
    app.run(debug=True)
