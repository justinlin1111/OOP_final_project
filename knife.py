import pygame
import math

BLUE = (0, 0, 255)

class Knife(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 10))  # 這裡可以使用刀的圖像
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.centerx = player.rect.centerx
        self.centery = player.rect.centery
        self.player_radius = player.radius
        # player is 50*50
        # 要把牠設到玩家的外圍那圈，而且跟滑鼠有關，詳細的可以看下面update這邊

    def update(self,player):
        """更新刀子的位置，使其跟隨滑鼠轉動"""
        # 這邊有點問題，我需要支援，中心想法就是讓他可以圍著角色的圓圈做旋轉，
        # 就像是滑鼠指到哪，刀子就會指到哪，我不確定player是不是一個需要的參數
        # 如果不用的話就把main裡面的weapons.update(player)的參數刪掉
        
        # 根據玩家的位置和滑鼠位置計算刀子的位置
        angle = math.atan2(pygame.mouse.get_pos()[1] - player.rect.centery, pygame.mouse.get_pos()[0] - player.rect.centerx)
        # 根據角度計算刀子的位置，假設刀子和玩家之間的距離是 player_radius * 2
        knife_x = player.rect.centerx + (self.player_radius * 2) * math.cos(angle)
        knife_y = player.rect.centery + (self.player_radius * 2) * math.sin(angle)
        self.rect.center = (knife_x, knife_y)

    def swing(self):
        """揮動刀的動作"""
        # 在這裡實現具體的揮動動作，例如播放揮動的動畫或者執行攻擊
        pass

    def draw(self, screen):
        """Draw the knife on the screen."""
        screen.blit(self.image, self.rect)