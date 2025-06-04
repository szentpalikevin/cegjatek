import tkinter as tk
import random
from PIL import Image, ImageTk
import tkinter.messagebox

penz = 100
nap = 1
keszlet = {"PLA": 3, "ABS": 2, "PETG": 1}
anyag_arak = {"PLA": 10, "ABS": 5, "PETG": 3}

megrendelesek = [
    {"targy": "Kulcstartó", "anyag": "PLA", "haszon": 20},
    {"targy": "Telefonállvány", "anyag": "ABS", "haszon": 35},
    {"targy": "Fogaskerék", "anyag": "PETG", "haszon": 30}
]

def frissit():
    status_text = f"Nap: {nap}/5\nPénz: {penz} Ft"
    status_label.config(text=status_text)

    keszlet_text = "Készlet:"
    for anyag in keszlet:
        keszlet_text += f"\n {anyag}: {keszlet[anyag]} db"
    keszlet_label.config(text=keszlet_text)


def rendel():
    global penz, nap
    if nap > 5:
        return

    rendeles = random.choice(megrendelesek)
    eredmeny = tk.messagebox.askyesno("Rendelés", f"{rendeles['targy']} ({rendeles['anyag']}) - {rendeles['haszon']} Ft\nElfogadod?")

    if eredmeny:
        if keszlet[rendeles["anyag"]] > 0:
            keszlet[rendeles["anyag"]] -= 1
            penz += rendeles["haszon"]
            tk.messagebox.showinfo("Siker", "Sikeres nyomtatás!")
        else:
            tk.messagebox.showwarning("Hiba", "Nincs elég anyagod!")
    else:
        tk.messagebox.showinfo("Info", "Elutasítottad a rendelést.")

    kovetkezo_nap()

