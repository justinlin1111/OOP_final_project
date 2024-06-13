import os
import pygame
from player import Player
from minion import Minion
from boss import Boss
from knife import Knife
from theClone import clone

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)

# 設置視窗大小
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS = 60

# 用來讓pause回到game時不要刷新的變數
first_in = True
# 用來重設clone的刷新時間
clone_refresh_time = 0
clone_created = False
score = 0

# 儲存音效
pygame.mixer.init()
knife_sound = pygame.mixer.Sound(os.path.join("sound", "knife_no_hit.mp3"))

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
    score = int(0)
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
