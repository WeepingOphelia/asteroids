import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

def main():

  # Print stuff (from first exercise)
  if False:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

  # Init pygame
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Init clock 
  clock = pygame.time.Clock()
  dt = 0

  # Instantiate player
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  # Instantiate asteroids
  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  # Handle shots
  shots = pygame.sprite.Group()
  Shot.containers = (shots, updatable, drawable)

  # Main loop
  while True:
    # Enable quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    # Update player and render
    for item in updatable:
      item.update(dt)
    for rock in asteroids:
      if rock.collide(player):
        print("Game over!")
        sys.exit()
      for shot in shots:
        if shot.collide(rock):
          shot.kill()
          rock.split()
    screen.fill("black")
    for item in drawable:
      item.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()