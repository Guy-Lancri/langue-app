from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Charger les fruits
with open("content/fruits.json", "r", encoding="utf-8") as f:
    fruits = json.load(f)

index = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global index

    mot = fruits[index]["target"]
    traduction = fruits[index]["source"]
    message = ""

    if request.method == "POST":
        reponse = request.form["reponse"]

        if traduction.lower() in reponse.lower():
            message = "bien"
            index = (index + 1) % len(fruits)
        else:
            message = f"No. {mot} = {traduction}"

    return render_template("index.html", mot=mot, message=message)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)