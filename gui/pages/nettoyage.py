import tkinter as tk

def creer_onglet_nettoyage(parent):
    frame = tk.Frame(parent, bg="white")
    parent.add(frame, text="Nettoyage")

    titre = tk.Label(frame, text="Onglet Nettoyage", font=("Helvetica", 14, "bold"), bg="white")
    titre.pack(pady=20)
