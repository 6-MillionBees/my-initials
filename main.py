# Arden Boettcher
# 2/11/25
# Pygame Template

import pygame
from letters import a_letter, b_letter
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("PLACEHOLDER")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events():
  global running
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      running = False



# Main loop
def main():
  global running
  running = True
  while running:

    # Call events
    main_events()

    # Fills window
    screen.fill(config.WHITE)

    # Draws lines
    for line in a_letter:
      pygame.draw.line(screen, config.RED, line[0], line[1], config.weight)
    for line in b_letter:
      pygame.draw.line(screen, config.BLUE, line[0], line[1], config.weight)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)


  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()