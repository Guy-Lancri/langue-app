from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

with open("content/fruits.json", "r", encoding="utf-8") as f:
    fruits = json.load(f)

index = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global index
    message = ""

    if request.method == "POST":
        reponse = request.form["reponse"]
        traduction = fruits[index]["source"]
        mot = fruits[index]["target"]

        if traduction.lower() in reponse.lower():
            message = "bien"
            index = (index + 1) % len(fruits)
        else:
            message = f"No. {mot} = {traduction}"

    mot = fruits[index]["target"]
    return render_template("index.html", mot=mot, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False, use_reloader=False)
