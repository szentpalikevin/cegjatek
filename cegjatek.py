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

def bolt():
    global penz
    print("\nBolt – anyagvásárlás")
    for anyag, ar in anyag_arak.items():
        print(f"{anyag}: {ar} Ft/db")
    valasztott_anyag = input("Melyik anyagot szeretnéd megvenni? (PLA/ABS/PETG): ").strip().upper()
    if valasztott_anyag in anyag_arak:
        try:
            db_szam = int(input("Hány darabot szeretnél vásárolni?: "))
        except ValueError:
            print('Hibás darabszám.')
            return
        osszeg = db_szam * anyag_arak[valasztott_anyag]
        if osszeg <= penz:
            keszlet[valasztott_anyag] += db_szam
            penz -= osszeg
            print(f"Sikeresen vásároltál {db_szam} db {valasztott_anyag} anyagot.")
        else:
            print('Nincs elég pénzed ehhez a vásárláshoz.')
    else:
        print("Ismeretlen anyag.")