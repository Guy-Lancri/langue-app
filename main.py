import json
import time

# Charger les fruits
with open("content/fruits.json", "r", encoding="utf-8") as f:
    fruits = json.load(f)

print("Début de la session")

for fruit in fruits:
    mot = fruit["target"]
    traduction = fruit["source"]

    # Bernard parle
    print("\nB:", mot)

    # Attendre réponse utilisateur
    reponse = input("Toi: ")

    # Vérification
    if traduction.lower() in reponse.lower():
        print("B: bien")
        continue

    # Si erreur
    print("B: No.", mot, "≠", reponse)

    # Attente naturelle
    time.sleep(2)

    # Donner réponse
    print("B:", mot, "est", traduction)

    # Reposer la question
    print("B:", mot)
    reponse = input("Toi: ")

    if traduction.lower() in reponse.lower():
        print("B: bien")
    else:
        print("B: on continue")

print("\nFin de session")