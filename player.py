# player.py
from typing import Any
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

    def attack(self, enemies):
        """Player attacks enemies."""
        # 這裡因為跟武器有關，所以到時候可能要重寫

        self.isattack = True
        for enemy in enemies:
            # 檢測武器與敵人的碰撞
            if self.weapon.rect.colliderect(enemy.rect):
                # 將敵人的生命值減少（這裡假設敵人有一個 hp 屬性）
                enemy.hp -= 10  # 假設每次攻擊造成 10 點傷害
                if enemy.health <= 0:
                    enemy.die(enemy)
