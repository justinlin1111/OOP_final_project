# player.py
import pygame
import settings

BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.WINDOW_WIDTH / 2
        self.rect.centery = settings.WINDOW_HEIGHT / 2
        self.radius = 30
        self.velocity = 3
        self.health = 10000
        self.max_health = 10000
        self.attack_power = 1000
        self.isattack = False

        self.experience = 0
        self.level = 1
        self.needed_experience = 50
        pygame.draw.circle(self.image, settings.BLUE, (self.rect.width // 2, self.rect.height // 2), self.radius, 0) 
    
    def update(self):
        # 隨著時間1秒+1點經驗
        # 因為FPS = 60
        self.experience += 1/60
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
        
        # 避免超出螢幕
        if (self.rect.top < 0):
            self.rect.top = 0
        if (self.rect.bottom > settings.WINDOW_HEIGHT - 20):
            self.rect.bottom = settings.WINDOW_HEIGHT - 20
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > settings.WINDOW_WIDTH):
            self.rect.right = settings.WINDOW_WIDTH

        # 處理升級資訊
        # 升級時會增加攻擊力並且回血
        if self.experience >= self.needed_experience:
            self.experience -= self.needed_experience
            self.level += 1
            self.attack_power += 3
            self.health += 10
            self.needed_experience += self.level * 10
            print(f"level up! now your level is {self.level}")

    def set_knife(self, knife):
        self.knife = knife

    def attack(self, enemies):
        if self.knife:
            self.knife.attack(enemies)

    def draw(self, screen):
        """Draw the experience on the screen."""
        screen.blit(self.image, self.rect)