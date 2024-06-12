# minion.py
import pygame
import math
import random
import settings

RED = (255, 0, 0)

class Minion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        if random.random() > 0.5:
            self.rect.centerx = random.choice([0, settings.WINDOW_WIDTH])
            self.rect.centery = random.randrange(0,settings.WINDOW_HEIGHT)
        else:
            self.rect.centerx = random.randrange(0,settings.WINDOW_WIDTH)
            self.rect.centery = random.choice([0, settings.WINDOW_HEIGHT])

        self.radius = 30
        self.velocity = 1
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

        # 避免超出螢幕
        if (self.rect.top < 0):
            self.rect.top = 0
        if (self.rect.bottom > settings.WINDOW_HEIGHT - 20):
            self.rect.bottom = settings.WINDOW_HEIGHT - 20
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > settings.WINDOW_WIDTH):
            self.rect.right = settings.WINDOW_WIDTH
    
    # 這個函式是用來讓小兵遠離一個東西的
    # something 表示一個想要遠離的物件
    def stayAwayFrom(self, something):
        if self.rect.colliderect(something.rect):
            dx = self.rect.centerx - something.rect.centerx
            dy = self.rect.centery - something.rect.centery
            dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
            self.rect.x += dx / dist * 20  # 调整反弹力度
            self.rect.y += dy / dist * 20  # 调整反弹力度

