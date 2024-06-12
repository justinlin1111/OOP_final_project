import pygame
import settings

class Experience(pygame.sprite.Sprite):
    def __init__(self,enemy):
        pygame.sprite.Sprite.__init__(self)
        # 創建一個透明的平面，
        # 用於get_rect()，(沒有get_rect()無法判斷碰撞)，
        # 與避免一開始生成是一個黑色矩形(default)
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx
        self.rect.centery = enemy.rect.centery
        self.original_y  = self.rect.centery
        self.radius = 5
        self.value = 10 * enemy.level  # 經驗值的提升量，可以根據需要調整
        pygame.draw.circle(self.image, settings.YELLOW, (self.rect.width // 2, self.rect.height // 2), self.radius, 0) 
    
    def update(self):
        pass
        

    def draw(self, screen):
        """Draw the experience on the screen."""
        screen.blit(self.image, self.rect)
