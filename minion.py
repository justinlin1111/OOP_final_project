# minion.py
import pygame
import math
import random

RED = (255, 0, 0)

class Minion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0,1080)
        self.rect.centery = random.randrange(0,720)
        self.radius = 30
        self.velocity = 2

    def update(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist

        self.rect.centerx += dx * self.velocity
        self.rect.centery += dy * self.velocity
    
    def check_collision(self, player):
        """Check collision with the player."""
        enemy_center = (self.x, self.y)
        player_center = (player.x, player.y)
        distance = math.hypot(player_center[0] - enemy_center[0], player_center[1] - enemy_center[1])
        return distance <= self.radius + player.radius
    
    def die(self, enemies):
        """Handle enemy's death."""
        enemies.remove(self)