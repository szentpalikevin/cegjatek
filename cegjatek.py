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
def bolt(anyag):
    global penz
    ar = anyag_arak[anyag]
    if penz >= ar:
        keszlet[anyag] += 1
        penz -= ar
        tk.messagebox.showinfo("Bolt", f"Vettél 1 db {anyag}-t.")
    else:
        tk.messagebox.showwarning("Nincs pénz", "Nincs elég pénzed.")
    frissit()

def kovetkezo_nap():
    global nap
    nap += 1
    if nap > 5:
        tk.messagebox.showinfo("Vége", f"A játék véget ért.\nVégső pénzed: {penz} Ft")
        root.destroy()
    else:
        frissit()


root = tk.Tk()
root.title("Cégjáték")
root.geometry("800x600")

hatter_kep = Image.open("hatter_kep.png")  
hatter_kep = hatter_kep.resize((800, 600), Image.LANCZOS)
hatter = ImageTk.PhotoImage(hatter_kep)

hatter_label = tk.Label(root, image=hatter)
hatter_label.place(x=0, y=0, relwidth=1, relheight=1)

status = tk.Label(root, text="", font=("Arial", 12), bg="lightgray", justify="left")
status.place(x=20, y=20)

status_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 13, "bold"),
    fg="#ffffff",
    bg="#4e7ea5",
    justify="left",
    anchor="nw",
    bd=2,
    relief="groove",
    padx=10,
    pady=5
)
status_label.place(x=20, y=20, width=240, height=60)

keszlet_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#4e7ea5",
    justify="left",
    anchor="nw",
    bd=2,
    relief="groove",
    padx=5,
    pady=5
)
keszlet_label.place(x=225, y=475, width=240, height=100)


gomb_keret = tk.Frame(root)
gomb_keret.place(x=20, y=100)

tk.Button(
    root,
    text="Rendelés",
    command=rendel,
    width=20,
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg="#78A0CE",
    activebackground="#005A9E",
    activeforeground="white",
    relief="raised"
).place(x=40, y=150)

tk.Label(
    root,
    text="Bolt – válassz anyagot:",
    font=("Segoe UI", 11, "bold"),
    fg="#ffffff",
    bg="#4e7ea5"
).place(x=20, y=260)

tk.Button(
    root,
    text="PLA - 10 Ft",
    command=lambda: bolt("PLA"),
    width=20,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#000000",
    relief="flat"
).place(x=20, y=300)

tk.Button(
    root,
    text="ABS - 5 Ft",
    command=lambda: bolt("ABS"),
    width=20,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#000000",
    relief="flat"
).place(x=20, y=350)

tk.Button(
    root,
    text="PETG - 3 Ft",
    command=lambda: bolt("PETG"),
    width=20,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#000000",
    relief="flat"
).place(x=20, y=400)

tk.Button(root, text="Kilépés", command=root.destroy, width=20).place(x=20, y=500)



frissit()
root.mainloop()