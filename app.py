from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

with open("content/fruits.json", "r", encoding="utf-8") as f:
    fruits = json.load(f)

with open("users/U0001.json", "r", encoding="utf-8") as f:
    user = json.load(f)

prenom = user["prenom"]

index = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global index

    if index == 0:
        message = f"Bonjour {prenom}, vous allez procéder à l’exercice {index + 1}"
    else:
        message = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "retour":
            index = (index - 1) % len(fruits)
            message = ""

        elif action == "stop":
            message = "Session arrêtée"

        else:
            reponse = request.form.get("reponse", "")
            traduction = fruits[index]["source"]
            mot = fruits[index]["target"]

            if traduction.lower() in reponse.lower():
                index = (index + 1) % len(fruits)
                if index == 0:
                    message = f"Bonjour {prenom}, vous allez procéder à l’exercice {index + 1}"
                else:
                    message = "bien"
            else:
                message = f"No. {mot} = {traduction}"

    mot = fruits[index]["target"]
    return render_template("index.html", mot=mot, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False, use_reloader=False)
