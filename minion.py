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
        self.health = 50
        self.attack_power = 10

    def update(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist

        self.rect.centerx += dx * self.velocity
        self.rect.centery += dy * self.velocity
    
    # 這個函式是用來讓小兵遠離一個東西的
    # something 表示一個想要遠離的物件
    def stayAwayFrom(self, something):
        if self.rect.colliderect(something.rect):
            dx = self.rect.centerx - something.rect.centerx
            dy = self.rect.centery - something.rect.centery
            dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
            self.rect.x += dx / dist * 20  # 调整反弹力度
            self.rect.y += dy / dist * 20  # 调整反弹力度

    def die(self, enemies):
        """Handle enemy's death."""
        enemies.remove(self)