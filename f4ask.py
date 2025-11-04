from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Gesamtkilometer():
    with open("fahrtenbuch.txt", "r", encoding="utf-8") as f:
        daten = f.read()

    übergabe_daten = []
    for zeile in daten.strip().split("\n"):
        teile = zeile.split(";")
        übergabe_daten.append(
            {"name": teile[0], "kilometer": teile[1], "auto": teile[2]}
        )
    return render_template("index.html", daten=übergabe_daten)


if __name__ == "__main__":
    app.run(debug=True)
