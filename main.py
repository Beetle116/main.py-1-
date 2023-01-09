import pygame

# Připravíme PyGame
pygame.init()
pygame.display.set_caption(".....")
velikost = (700, 400)
screen = pygame.display.set_mode(velikost)
cas = pygame.time.Clock()

def game_to_screen(x, y):
    return (x * 45, y * 45)

# Připravíme si obrázek
background = (150, 220, 250)
zelva = pygame.image.load("zelvazhora.png")
zelva = pygame.transform.scale(zelva, (40, 40))
color = (255 , 255, 255)
rotated_zelva = pygame.transform.rotate(zelva, 90)

WIDTH = 12
HEIGHT = 7

zx = 0
zy = 0

def animate(nx,ny):
  global zx,zy


  duration = 1000
  t = 0
# obrazovkove souradnice
  sx,sy = game_to_screen(zx,zy)
  ex,ey = game_to_screen(nx,ny)
  while t < duration:
    #.........
    new = t / duration
    old = 1 - new
    x = old * sx + new * ex
    y = old * sy + new * ey
    screen.fill(background)
    screen.blit(rotated_zelva,(x,y))
    pygame.display.update()
    t = t + cas.tick(60)
  
  zx = nx
  zy = ny

while True:
    # Vykreslíme
    screen.fill(background)
    for x in range(WIDTH):
        for y in range (HEIGHT):
          rect = ((x * 45, y * 45), (40, 40))
          pygame.draw.rect(screen, color, rect)
    screen.blit(rotated_zelva, game_to_screen(zx,zy))
    
    screen.blit(rotated_zelva, (zx * 45, zy * 45))
    
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        rotated_zelva = pygame.transform.rotate (zelva, 270)
        if zx < WIDTH - 1:
           animate(zx+1,zy)
      elif event.key == pygame.K_UP:
        rotated_zelva = pygame.transform.rotate (zelva, 0)
        if zy > 0:
          animate (zx,zy-1)
      elif event.key == pygame.K_LEFT:
        rotated_zelva = pygame.transform.rotate (zelva, 90)
        if zx > 0:
          animate (zx -1,zy)
      elif event.key == pygame.K_DOWN:
        rotated_zelva = pygame.transform.rotate (zelva, 180)
        if zy < HEIGHT - 1 :
          animate(zx,zy+1)