from flask import Flask, render_template
from collections import defaultdict

app = Flask(__name__)


fahrerliste = {}
gesamt_km = 0.0
with open("fahrtenbuch.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        teile = zeile.strip().split(";")
        if len(teile) >= 3:
            try:
                fahrer = teile[0]
                gesamt_km += float(teile[1])
            except ValueError:
                continue

gesamt_werte = {}
for fahrer in fahrerliste:
    if fahrer.name in gesamt_werte:
        gesamt_werte[fahrer.name] += fahrer.kilometer
    if fahrer.name not in gesamt_werte:
        gesamt_werte[fahrer.name] = fahrer.kilometer


@app.route("/")
def Gesamtkilometer():
    with open("fahrtenbuch.txt", "r", encoding="utf-8") as f:
        daten = f.read()

    übergabe_daten = []
    for zeile in daten.strip().split("\n"):
        teile = zeile.split(";")
        übergabe_daten.append(
            {"name": teile[0], "kilometer": float(teile[1]), "auto": teile[2]}
        )
    return render_template("index.html", daten=übergabe_daten)


def kilometer_pro_fahrer():
    summen = defaultdict(float)

    with open("Fahrtenbuch.txt", "r", encoding="utf-8") as f:
        for zeile in f:
            teile = zeile.strip().split(";")
            if len(teile) <= max(0, 1):
                continue
            key = teile[0].strip()
            try:
                wert = float(teile[1].strip())
                summen[key] += wert
            except ValueError:
                continue

    übergabe_daten = []
    for zeile in summen.strip().split("\n"):
        teile = zeile.split(";")
        übergabe_daten.append({"kilometer_pro_fahrer": float(summen)})
    return render_template("index.html", daten=übergabe_daten)


if __name__ == "__main__":
    app.run(debug=True)
