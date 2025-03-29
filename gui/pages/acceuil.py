import tkinter as tk

def creer_onglet_accueil(parent):
    frame = tk.Frame(parent, bg="white")
    parent.add(frame, text="Accueil")

    titre = tk.Label(frame, text="Onglet Accueil", font=("Helvetica", 14, "bold"), bg="white")
    titre.pack(pady=20)
