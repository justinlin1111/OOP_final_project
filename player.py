# player.py
import pygame
import math
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 540
        self.rect.centery = 700
        self.radius = 50
        self.velocity = 3
        self.health = 100
        self.attack_power = 10
        self.isattack = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_d]:
            self.rect.x += self.velocity

    def set_knife(self, knife):
        self.knife = knife

    def attack(self, enemies):
        if self.knife:
            self.knife.attack(enemies)