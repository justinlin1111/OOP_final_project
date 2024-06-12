import pygame
import math
from experience import Experience
import settings

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Knife(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.Surface((100, 10), pygame.SRCALPHA)  # 创建一个透明的表面
        pygame.draw.polygon(self.original_image, RED, [(0, 5), (90, 5), (95, 0), (100, 5), (95, 10), (90, 5), (0, 5)])
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.player = player
        self.offset = player.radius * 1.8
        self.repel = 5

    def update(self):
        """更新刀子的位置，使其跟隨滑鼠轉動"""
        
        # 計算从玩家到滑鼠的角度
        dx = pygame.mouse.get_pos()[0] - self.player.rect.centerx
        dy = pygame.mouse.get_pos()[1] - self.player.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))  # 计算旋转角度

        # 計算刀子的位置，使其位于玩家與滑鼠之間的線上，並與玩家保持一定距離
        rad_angle = math.radians(angle)
        self.rect.centerx = self.player.rect.centerx + int(self.offset * math.cos(rad_angle))
        self.rect.centery = self.player.rect.centery - int(self.offset * math.sin(rad_angle))

        # 旋转刀子使其尖端朝向鼠标
        self.image = pygame.transform.rotate(self.original_image, angle)
        # self.lastAngle = angle
        self.rect = self.image.get_rect(center=self.rect.center)

    def swing(self):
        """揮動刀的動作"""
        # 在這裡實現具體的揮動動作，例如播放揮動的動畫或者執行攻擊
        pass

    # 利用刀攻擊敵人，如果刀碰到敵人的話敵人會損血，
    # 並且會被擊退，同時判斷敵人的血是否歸零以移除
    # 在敵人死亡時會生成經驗值
    def attack(self, enemies):
        """刀子攻擊敵人"""
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                enemy.health -= self.player.attack_power
                repel(self, enemy)
                if enemy.health <= 0:
                    enemy.kill()
                    experience = Experience(enemy)
                    settings.experiences.add(experience)

    def draw(self, screen):
        """Draw the knife on the screen."""
        screen.blit(self.image, self.rect)

# 用武器去擊退enemy(會往後飛)
# 可能可以寫成一個屬性是擊退的等級
def repel(weapon, enemy):
    if enemy != weapon and weapon.rect.colliderect(enemy.rect):
        if weapon.player.rect.centerx < enemy.rect.centerx:
            enemy.rect.x += weapon.repel
        else:
            enemy.rect.x -= weapon.repel
        if weapon.player.rect.centery < enemy.rect.centery:
            enemy.rect.y += weapon.repel
        else:
            enemy.rect.y -= weapon.repel
