from flask import Flask, render_template

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
def fahrer_liste():
    with open("fahrtenbuch.txt", "r", encoding="utf-8") as f:
        daten = f.read()

    übergabe_daten = []
    for zeile in daten.strip().split("\n"):
        teile = zeile.split(";")
        übergabe_daten.append(
            {"name": teile[0], "kilometer": float(teile[1]), "auto": teile[2]}
        )
    return render_template("index.html", daten=übergabe_daten)


@app.route("/kilometer")
def gesamt_kilometer():
    gesamt_werte = {}
    with open("fahrtenbuch.txt", "r", encoding="utf-8") as f:
        for zeile in f:
            teile = zeile.strip().split(";")
            fahrername = teile[0]
            kilometer = float(teile[1])
            if fahrername in gesamt_werte:
                gesamt_werte[fahrername] += kilometer
            else:
                gesamt_werte[fahrername] = kilometer
    return str(gesamt_werte)


if __name__ == "__main__":
    app.run(debug=True)
