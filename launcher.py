import subprocess
import sys
import tkinter as tk
from tkinter import messagebox


def launch_game(mode):
  root.destroy()
  try:
    # Avvia il file del gioco passando la modalità scelta
    subprocess.run([sys.executable, "game.py", mode])
  except Exception as e:
    messagebox.showerror("Errore", f"Impossibile avviare il gioco: {e}")


# Creazione della finestra del Launcher
root = tk.Tk()
root.title("DrawMap Launcher")
root.geometry("400x350")
# (Riga rimossa per evitare l'errore TclError)

# Titolo
title_label = tk.Label(
    root, text="DRAW MAP FPS", font=("Helvetica", 18, "bold")
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root, text="Seleziona la modalità di gioco", font=("Helvetica", 11)
)
subtitle_label.pack(pady=5)

# Bottoni per le modalità ispirate al video
btn_4v4 = tk.Button(
    root,
    text="4v4 - Draw the Map",
    font=("Helvetica", 12),
    bg="#ff5722",
    fg="white",
    width=25,
    height=2,
    command=lambda: launch_game("4v4"),
)
btn_4v4.pack(pady=10)

btn_ffa = tk.Button(
    root,
    text="Free For All (Tutti contro tutti)",
    font=("Helvetica", 12),
    bg="#2196F3",
    fg="white",
    width=25,
    height=2,
    command=lambda: launch_game("FFA"),
)
btn_ffa.pack(pady=10)

# Crediti
footer_label = tk.Label(
    root, text="Project GitHub Ready", font=("Helvetica", 8), fg="gray"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
