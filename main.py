import pygame
import sys
from player import Player
from minion import Minion
from boss import Boss
from knife import Knife

# 初始化 Pygame
pygame.init()

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)

# 設置視窗大小
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS = 60

# 創建視窗
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("HOME SCREEN")
clock = pygame.time.Clock()

# 載入圖像
background_image = pygame.image.load("background.png")

# 定義文字類
class Text:
    def __init__(self, text, font_size, position, color):
        self.font = pygame.font.SysFont(None, font_size)
        self.text_surface = self.font.render(text, True, color)
        self.rect = self.text_surface.get_rect(center=position)
    
    def draw(self, screen):
        screen.blit(self.text_surface, self.rect)

def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)  # 2是外框像素值

# 主畫面迴圈
def main_menu():
    while True:
        clock.tick(FPS)
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                    # 切換到遊戲畫面
                    return "game"
        
        # 繪製背景
        screen.fill(WHITE)
        
        # 創建並繪製按鈕
        start_button = Text("START", 50, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), BLACK)
        start_button.draw(screen)
        
        # 更新畫面
        pygame.display.update()

# 遊戲畫面迴圈
def game_screen():
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    weapons = pygame.sprite.Group()
    player = Player()  # 創建玩家物件
    all_sprites.add(player)
    for i in range(5):
        minion = Minion()  # 創建小兵
        enemies.add(minion)
    boss = Boss()      # 創建Boss
    enemies.add(boss)
    knife = Knife(player)    # 創建刀物件
    weapons.add(knife)

    while True:
        clock.tick(FPS)
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # 切換回主畫面
                    return "main_menu"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 玩家攻擊
                    player.attack(enemies)
        
        # 更新遊戲
        all_sprites.update()
        enemies.update(player)
        weapons.update(player)

        # 刀子碰到敵人且正在攻擊，則敵人扣血，
        # 判斷敵人血量，若小於0則死亡()
        # 若weapon碰到enemies，都不刪掉(False、False)
        hits = pygame.sprite.groupcollide(weapons, enemies, False, False)
        if player.isattack:
            for hit in hits:
                pass
            "knife""gun"
 
        # 敵人之間要判斷是否碰撞，不然會重疊

        # 敵人碰到玩家要扣血(敵人加攻擊力屬性)
        # 用spritecollide應該沒什麼問題

        # 更新畫面
        screen.fill(WHITE)
        screen.blit(background_image, (0,0))
        all_sprites.draw(screen)
        enemies.draw(screen)
        weapons.draw(screen)
        draw_health(screen, player.health, 5, 15)
        pygame.display.update()

# 主迴圈
if __name__ == "__main__":
    current_screen = "main_menu"
    while True:
        if current_screen == "main_menu":
            current_screen = main_menu()
        elif current_screen == "game":
            current_screen = game_screen()
