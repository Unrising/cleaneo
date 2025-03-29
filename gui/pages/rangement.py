import tkinter as tk

def creer_onglet_rangement(parent):
    frame = tk.Frame(parent, bg="white")
    parent.add(frame, text="Rangement")

    titre = tk.Label(frame, text="Onglet Rangement", font=("Helvetica", 14, "bold"), bg="white")
    titre.pack(pady=20)



