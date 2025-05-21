import random


anyag_arak = {"PLA": 10, "ABS": 5, "PETG": 3}

megrendelesek = [
    {"targy": "Kulcstartó", "anyag": "PLA", "haszon": 20},
    {"targy": "Telefonállvány", "anyag": "ABS", "haszon": 35},
    {"targy": "Fogaskerék", "anyag": "PETG", "haszon": 30}
]

penz = 100
keszlet = {"PLA": 3, "ABS": 2, "PETG": 1}

def allapot_kiiras():
    print(f"\nPénzed: {penz} Ft")
    print("Készleted:")
    for anyag, db in keszlet.items():
        print(f"- {anyag}: {db} db")