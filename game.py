import sys
import pygame

# Inizializzazione di Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DrawMap FPS - Game Engine")
clock = pygame.time.Clock()

# Leggi la modalità passata dal launcher
mode = sys.argv[1] if len(sys.argv) > 1 else "FFA"

# Stati del gioco: 'DRAW' (disegni la mappa) o 'PLAY' (sparatutto)
game_state = "DRAW"

# Liste per tracciare le linee disegnate dai giocatori
lines = []
drawing = False
start_pos = None

# Posizione del giocatore
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_angle = 0

running = True
while running:
  screen.fill((30, 30, 40))  # Sfondo scuro stile arena spaziale

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Fase 1: Disegno della mappa (clicca e trascina per creare muri/strutture)
    if game_state == "DRAW":
      if event.type == pygame.MOUSEBUTTONDOWN:
        drawing = True
        start_pos = event.pos
      elif event.type == pygame.MOUSEBUTTONUP and drawing:
        drawing = False
        end_pos = event.pos
        lines.append((start_pos, end_pos))
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          # Premi INVIO per passare alla fase di gioco/sparo
          game_state = "PLAY"

    # Fase 2: Gioco FPS
    elif game_state == "PLAY":
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          game_state = "DRAW"  # Torna a disegnare premendo ESC

  # Logica di movimento nella fase PLAY
  if game_state == "PLAY":
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      player_y -= 5
    if keys[pygame.K_s]:
      player_y += 5
    if keys[pygame.K_a]:
      player_x -= 5
    if keys[pygame.K_d]:
      player_x += 5

  # --- DISEGNO A SCHERMO ---
  # Disegna tutte le linee create dai giocatori
  for line in lines:
    pygame.draw.line(screen, (0, 255, 200), line[0], line[1], 6)

  if drawing and start_pos:
    current_pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, (255, 100, 100), start_pos, current_pos, 4)

  # Interfaccia testuale a schermo
  font = pygame.font.SysFont(None, 24)
  if game_state == "DRAW":
    mode_text = font.render(
        f"MODALITA: {mode} | FASE: DISEGNO MAPPA (Trascina il mouse, premi"
        " INVIO per giocare)",
        True,
        (255, 255, 255),
    )
  else:
    mode_text = font.render(
        f"MODALITA: {mode} | FASE: FPS ACTION (Usa WASD per muoverti, ESC per"
        " modificare la mappa)",
        True,
        (255, 255, 255),
    )
    # Disegna il "giocatore" al centro
    pygame.draw.circle(
        screen, (255, 255, 0), (int(player_x), int(player_y)), 10
    )

  screen.blit(mode_text, (20, 20))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
sys.exit()
