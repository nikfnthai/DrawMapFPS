import sys
import tkinter as tk

# Leggi la modalità passata dal launcher (default: FFA)
mode = sys.argv[1] if len(sys.argv) > 1 else "FFA"

# Configurazione della finestra di gioco
root = tk.Tk()
root.title(f"DrawMap FPS - Modalità: {mode}")
root.geometry("800x600")
root.configure(bg="#1e1e28")

# Titolo della modalità in alto
lbl_mode = tk.Label(
    root,
    text=(
        f"MODALITÀ: {mode} | Trascina il mouse per disegnare i muri della mappa"
    ),
    font=("Helvetica", 12, "bold"),
    bg="#1e1e28",
    fg="#00ffc8",
)
lbl_mode.pack(pady=10)

# Canvas per disegnare la mappa e muoversi
canvas = tk.Canvas(root, bg="#14141c", width=760, height=450, highlightthickness=0)
canvas.pack(pady=10)

# Posizione iniziale del "giocatore"
player = canvas.create_oval(380, 220, 400, 240, fill="#ffff00", outline="")

# Variabili per il disegno
start_x, start_y = None, None


def on_press(event):
  global start_x, start_y
  start_x, start_y = event.x, event.y


def on_drag(event):
  # Disegna linee in tempo reale mentre trascini il mouse
  if start_x and start_y:
    canvas.create_line(
        start_x,
        start_y,
        event.x,
        event.y,
        fill="#00ffc8",
        width=4,
        tags="map_line",
    )
    canvas.update()


canvas.bind("<Button-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)

# Controlli di movimento con i tasti WASD
player_speed = 10


def move(event):
  key = event.keysym.lower()
  if key == "w":
    canvas.move(player, 0, -player_speed)
  elif key == "s":
    canvas.move(player, 0, player_speed)
  elif key == "a":
    canvas.move(player, -player_speed, 0)
  elif key == "d":
    canvas.move(player, player_speed, 0)


root.bind("<KeyPress>", move)

# Pulsante per chiudere o resettare
btn_frame = tk.Frame(root, bg="#1e1e28")
btn_frame.pack(pady=5)

lbl_info = tk.Label(
    btn_frame,
    text="Usa i tasti W, A, S, D per muovere il giocatore sulla mappa disegnata!",
    font=("Helvetica", 10),
    bg="#1e1e28",
    fg="white",
)
lbl_info.pack()

root.mainloop()
