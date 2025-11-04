from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Gesamtkilometer():
    with open("Fahrtenbuch.txt", "r", encoding="utf-8") as f:
        daten = f.read()
    return render_template("index.html", daten=daten)


if __name__ == "__main__":
    app.run(debug=True)
