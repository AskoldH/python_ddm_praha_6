Hádej co se zobrazí když spustíme obrazovku:

### 1)
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((135, 206, 235))

pygame.draw.rect(screen, (34, 139, 34), (0, 400, 800, 200))

pygame.draw.circle(screen, (255, 255, 0), (400, 150), 80)

pygame.display.flip()
```

### 2)
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((169, 169, 169))

pygame.draw.rect(screen, (255, 0, 0), (250, 200, 100, 100))

pygame.draw.rect(screen, (255, 0, 0), (450, 200, 100, 100))

pygame.draw.rect(screen, (0, 0, 0), (300, 400, 200, 50))

pygame.display.flip()
```

### 3)
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((0, 0, 0))

font = pygame.font.SysFont('Arial', 100)
text = font.render("VYHRAL JSI!", True, (0, 255, 0))

screen.blit(text, (100, 250))

pygame.display.flip()
```

### 4)
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((255, 255, 255))

pygame.draw.circle(screen, (0, 255, 0), (400, 300), 40)

pygame.draw.rect(screen, (0, 0, 0), (200, 150, 400, 20)) 

pygame.draw.rect(screen, (0, 0, 0), (200, 450, 400, 20)) 

pygame.draw.rect(screen, (0, 0, 0), (200, 150, 20, 320)) 

pygame.draw.rect(screen, (0, 0, 0), (580, 150, 20, 320))

pygame.display.flip()
```

### 5)
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (0, 0, 255), (300, 300, 200, 200))

pygame.draw.polygon(screen, (255, 0, 0), [(300, 300), (500, 300), (400, 150)])

pygame.display.flip()
```

### BONUS: Extra těžké
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

ball_pos = [400, 300]
ball_speed = [5, 5]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= 40 or ball_pos[0] >= 760:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 40 or ball_pos[1] >= 560:
        ball_speed[1] = -ball_speed[1]

    pygame.draw.circle(screen, (0, 0, 255), ball_pos, 40)

    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()
```
