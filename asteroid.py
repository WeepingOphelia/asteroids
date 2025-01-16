import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  def draw(self, screen):
    pygame.draw.circle(screen, "cyan", center=self.position, radius=self.radius, width=2)
  def update(self, dt):
    self.position += self.velocity * dt
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    dr = random.uniform(20, 50)
    new_vector1 = self.velocity.rotate(dr)
    new_vector2 = self.velocity.rotate(-dr)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    spawn1 = Asteroid(self.position.x, self.position.y, new_radius)
    spawn2 = Asteroid(self.position.x, self.position.y, new_radius)
    spawn1.velocity = new_vector1 * 1.2
    spawn2.velocity = new_vector2 * 1.2

    