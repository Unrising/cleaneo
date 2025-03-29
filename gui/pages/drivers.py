import tkinter as tk

def creer_onglet_drivers(parent):
    frame = tk.Frame(parent, bg="white")
    parent.add(frame, text="Pilotes")

    titre = tk.Label(frame, text="Onglet Pilotes", font=("Helvetica", 14, "bold"), bg="white")
    titre.pack(pady=20)
