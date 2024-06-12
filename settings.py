import pygame
from player import Player
from minion import Minion
from boss import Boss
from knife import Knife

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 設置視窗大小
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS = 60



# 用來存放所有的精靈類別(角色、敵人)
all_sprites = pygame.sprite.Group()
# 用來存放所有敵人
enemies = pygame.sprite.Group()
# 用來存放所有武器
weapons = pygame.sprite.Group()
# 用來存放經驗值 在knife生成
experiences = pygame.sprite.Group()

# 創建玩家物件 
# 在外面是因為如果在函式裡面的話在跑完game_init的當下，
# 在裡面的player就已經沒辦法存取了，
# 而player是一個需要獨立去判斷的物件，
# 因此另外在外面令出
player = Player()  

def game_init():
    # 清空所有的Group
    all_sprites.empty()
    enemies.empty()
    weapons.empty()
    experiences.empty()

    # 初始化
    player.__init__()
    all_sprites.add(player)
    for _ in range(10):
        minion = Minion()  # 創建小兵
        enemies.add(minion)
    boss = Boss()      # 創建Boss
    enemies.add(boss)
    knife = Knife(player)    # 創建刀物件
    weapons.add(knife)
    all_sprites.add(knife)
    player.set_knife(knife)
