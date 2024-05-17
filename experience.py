import pygame

class Experience:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 0)  # 黃色
        self.experience_value = 10  # 經驗值的數量，可以根據需要調整
    
    def draw(self, screen):
        """Draw the experience on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
