# boss.py
import random
import pygame
import math
import settings


RED = (255, 0, 0)

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = 900
        self.rect.centery = 300
        self.radius = 40
        self.velocity = 1

        self.level = 1
        self.max_health = 150
        self.health = 150
        self.attack_power = 20
        pygame.draw.circle(self.image, settings.RED, (self.rect.width // 2, self.rect.height // 2), self.radius, 0) 
    

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

    def stayAwayFrom(self, something):
        if self.rect.colliderect(something.rect):
            dx = self.rect.centerx - something.rect.centerx
            dy = self.rect.centery - something.rect.centery
            dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
            self.rect.x += dx / dist * 20  # 调整反弹力度
            self.rect.y += dy / dist * 20  # 调整反弹力度
            
    def level_up(self):
        self.level += 1
        self.max_health += 25
        self.health = self.max_health
        self.attack_power += 5
        self.velocity += 0.1

        if random.random() < 0.33:
            self.rect.centerx = random.choice([0, settings.WINDOW_WIDTH])
            self.rect.centery = random.randrange(0,settings.WINDOW_HEIGHT)
        elif random.random() < 0.67:
            self.rect.centerx = random.randrange(0,settings.WINDOW_WIDTH)
            self.rect.centery = random.choice([0, settings.WINDOW_HEIGHT])
        else:
            self.rect.centerx = random.randrange(0,settings.WINDOW_WIDTH)
            self.rect.centery = random.randrange(0,settings.WINDOW_HEIGHT)

        # 檢查他的等級決定它的顏色
        # 紅 ->  1 ~  3
        # 橙 ->  4 ~  6
        # 黃 ->  7 ~  9
        # 綠 -> 10 ~ 12
        # 藍 -> 13 ~ 15
        # 靛 -> 16 ~ 18
        # 紫 -> 19 ~ 
        if self.level >= 19:
            pygame.draw.circle(self.image, settings.PURPLE, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
        elif self.level >= 16:
            pygame.draw.circle(self.image, settings.INDIGO, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
        elif self.level >= 13:
            pygame.draw.circle(self.image, settings.BLUE, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
        elif self.level >= 10:
            pygame.draw.circle(self.image, settings.GREEN, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
        elif self.level >= 7:
            pygame.draw.circle(self.image, settings.YELLOW, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
        elif self.level >= 4:
            pygame.draw.circle(self.image, settings.ORANGE, (self.rect.width // 2, self.rect.height // 2), self.radius, 0)
    
    def draw(self, screen):
        """Draw the experience on the screen."""
        screen.blit(self.image, self.rect)
