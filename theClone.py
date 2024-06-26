import math
from typing import Any
import pygame
import settings

class clone(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = player.image
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.WINDOW_WIDTH / 2
        self.rect.centery = settings.WINDOW_HEIGHT / 2
        self.radius = player.radius
        self.velocity = player.velocity
        self.health = player.health
        self.max_health = player.max_health
        self.attack_power = player.attack_power
        self.level = player.level
        pygame.draw.circle(self.image, settings.BLUE, (self.rect.width // 2, self.rect.height // 2), self.radius, 0) 
        
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

    # 這個函式是用來讓theClone遠離一個東西的
    # something 表示一個想要遠離的物件
    def stayAwayFrom(self, something):
        if self.rect.colliderect(something.rect):
            dx = self.rect.centerx - something.rect.centerx
            dy = self.rect.centery - something.rect.centery
            dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
            self.rect.x += dx / dist * 20  # 调整反弹力度
            self.rect.y += dy / dist * 20  # 调整反弹力度

    def draw(self, screen):
        """Draw the experience on the screen."""
        screen.blit(self.image, self.rect)