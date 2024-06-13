import os
import pygame
import sys
import settings

# 初始化 Pygame
pygame.init()
pygame.mixer.init()

# 創建視窗
screen = pygame.display.set_mode(settings.WINDOW_SIZE)
pygame.display.set_caption("HOME SCREEN")
clock = pygame.time.Clock()

# 載入圖像
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT - 20))

# 載入音樂
pygame.mixer.music.load(os.path.join("sound", "never_give_up.mp3"))
pygame.mixer.music.set_volume(0.3)

# 定義文字類
class Text:
    def __init__(self, text, font_size, position, color):
        self.font = pygame.font.SysFont(None, font_size)
        self.text_surface = self.font.render(text, True, color)
        self.rect = self.text_surface.get_rect(center=position)
    
    def draw(self, screen):
        screen.blit(self.text_surface, self.rect)

# 此函式用於畫出一個類似血條的東西
# surf -> 想要畫在哪個平面?
# BAR_LENGTH -> 這根bar的長度(寬)
# BAR_LENGTH -> 這根bar的高度
# color -> 想要畫出的顏色
# outline_color -> 想要畫出的外框顏色
# amount -> 在所有量裡剩下的量(ex:剩餘血量)
# max_value -> 所有量(ex:最大血量)
# x -> 想要畫在畫布的絕對位置x上
# y -> 想要畫在畫布的絕對位置y上
def draw_bar(surf, BAR_LENGTH, BAR_HEIGHT, color, outline_color, amount, max_value, x, y):
    if amount < 0:
        amount = 0
    if amount > max_value:
        amount = max_value
    fill = (amount/max_value)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, color, fill_rect)
    pygame.draw.rect(surf, outline_color, outline_rect, 2)  # 2是外框像素值

# 定義必要函式
# 需要一個精靈跟一個類別，如果在群組中除了自己以外的東西碰到自己，這個精靈會有彈開的動作。
def avoid_overlap(sprite, group):
    for other_sprite in group:
        if other_sprite != sprite and pygame.sprite.collide_circle(sprite, other_sprite):
            if sprite.rect.centerx < other_sprite.rect.centerx:
                sprite.rect.x -= 1
            else:
                sprite.rect.x += 1
            if sprite.rect.centery < other_sprite.rect.centery:
                sprite.rect.y -= 1
            else:
                sprite.rect.y += 1

pygame.mixer.music.play(-1)

# 主畫面迴圈
def main_menu():
    settings.first_in = True
    while True:
        clock.tick(settings.FPS)
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                    # 切換到遊戲畫面
                    return "game"
                elif description_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return "description"
        
        # 繪製背景
        screen.fill(settings.WHITE)
        
        # 創建並繪製按鈕
        start_button = Text("START", 50, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT/2), settings.BLACK)
        start_button.draw(screen)

        description_button = Text("DESCRIPTION", 40, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT/2 + 70), settings.BLACK)
        description_button.draw(screen)

        last_score = Text(f"LAST SCORE : {settings.score}", 40, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT/2 - 140), settings.BLACK)
        last_score.draw(screen)
        
        # 更新畫面
        pygame.display.update()

# 遊戲描述畫面
def game_description():
    while True:
        clock.tick(settings.FPS)
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_main.rect.collidepoint(pygame.mouse.get_pos()):
                    return "main_menu"
        
        screen.fill(settings.BLACK)

        back_to_main = Text("Back", 50, (settings.WINDOW_WIDTH/12, settings.WINDOW_HEIGHT/12), settings.WHITE)
        back_to_main.draw(screen)
        descriptions = []
        descriptions.append(Text(" \"W\" , \"A\" , \"S\" , \"D\" to move, click the mouse to attack", 50, (settings.WINDOW_WIDTH/2, 100), settings.WHITE))
        descriptions.append(Text("The upper right is the blood volume,", 50, (settings.WINDOW_WIDTH/2, 175), settings.WHITE))
        descriptions.append(Text("and the lower right is the experience value and level.", 50, (settings.WINDOW_WIDTH/2, 250), settings.WHITE))
        descriptions.append(Text("Enemies become stronger the more times they are defeated", 50, (settings.WINDOW_WIDTH/2, 425), settings.WHITE))
        descriptions.append(Text("Intensity is initially distinguished by color", 50, (settings.WINDOW_WIDTH/2, 500), settings.WHITE))
        descriptions.append(Text("from weak to strong from red to purple.", 50, (settings.WINDOW_WIDTH/2, 550), settings.WHITE))
        descriptions.append(Text("Click the esc key on the keyboard to pause the game", 50, (settings.WINDOW_WIDTH/2, 600), settings.WHITE))
        
        
        for description in descriptions:
            description.draw(screen)

        # 更新畫面
        pygame.display.update()

# 設置定時器來控制事件產生
TIMER_EVENT_ID = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT_ID, 10000)

# 遊戲畫面迴圈
def game_screen():
    if settings.first_in:
        settings.game_init()

    start_time = pygame.time.get_ticks()
    # 複製人刷新時間
    settings.clone_refresh_time = start_time
    settings.clone_created = False

    while True:
        # 設置遊戲的FPS
        clock.tick(settings.FPS)
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 遊戲畫面點esc會回到主畫面
                if event.key == pygame.K_ESCAPE:
                    return "pause"
                # 點一下滑鼠要執行攻擊
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 玩家攻擊
                settings.player.attack(settings.enemies)
            elif event.type == TIMER_EVENT_ID:
                # 先判斷敵人數量是不是超過30
                if len(settings.enemies) < 30:
                    # 每10秒就生成一個敵人
                    enemy = settings.Minion()
                    settings.enemies.add(enemy)
        
        # 計算經過的時間
        elapsed_time = (pygame.time.get_ticks() - settings.clone_refresh_time) / 1000  # 轉換為秒
        if elapsed_time >= 30 and not settings.clone_created:
            clone = settings.clone(settings.player)  
            settings.enemies.add(clone)
            settings.clone_created = True

        # 更新遊戲
        settings.all_sprites.update()
        settings.enemies.update(settings.player)
        settings.experiences.update()

        # 寫上玩家的資訊
        player_level = Text(f"LEVEL : {settings.player.level}", 20, (settings.WINDOW_WIDTH - 80, 30), settings.WHITE)
        player_attack_power = Text(f"ATTACK : {settings.player.attack_power}", 20, (settings.WINDOW_WIDTH - 80, 60), settings.WHITE)
        player_experiece = Text(f"{int(settings.player.experience)} / {settings.player.needed_experience}", 20, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT - 10), settings.BLACK)
        player_health = Text(f"{settings.player.health} / {settings.player.max_health}", 20, (150, 20), settings.WHITE)

        # 如果玩家碰到經驗值，經驗要提升，並且消失
        for experience in settings.experiences:
            if pygame.sprite.collide_rect(settings.player, experience):
                settings.player.experience += experience.value
                experience.kill()
 
        # 敵人之間要判斷是否碰撞，不然會重疊
        for enemy in settings.enemies:
            avoid_overlap(enemy, settings.enemies)

        # 敵人碰到玩家要扣血(敵人加攻擊力屬性)
        for enemy in settings.enemies:
            if pygame.sprite.collide_circle(settings.player, enemy):
                settings.player.health -= enemy.attack_power  # 根據敵人的攻擊力扣血
                enemy.stayAwayFrom(settings.player)
                if settings.player.health <= 0:
                    print("Player is dead!")
                    return "main_menu"

        # 更新畫面
        screen.fill(settings.WHITE)
        screen.blit(background_image, (0,0))
        settings.all_sprites.draw(screen)
        settings.enemies.draw(screen)
        settings.weapons.draw(screen)
        settings.experiences.draw(screen)

        # 畫血條出來(此函式在main裡)
        draw_bar(screen, 100, 10, settings.GREEN, settings.WHITE, settings.player.health, settings.player.max_health, 5, 15)
        draw_bar(screen, settings.WINDOW_WIDTH, 20, settings.YELLOW, settings.BLACK, settings.player.experience, settings.player.needed_experience, 0, settings.WINDOW_HEIGHT - 20)
        score = Text(f"SCORE : {settings.score}", 50, (settings.WINDOW_WIDTH/2, 30), settings.WHITE)
        score.draw(screen)
        player_level.draw(screen)
        player_attack_power.draw(screen)
        player_experiece.draw(screen)
        player_health.draw(screen)
        pygame.display.update()

def pause():
    settings.first_in = False
    while True:
        # 限制FPS
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_game.rect.collidepoint(pygame.mouse.get_pos()):
                    return "game"
            
            screen.fill(settings.BLACK)

            back_to_game = Text("Continue", 50, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT*2/3), settings.WHITE)
            back_to_game.draw(screen)

            description_button = Text(f"LAST SCORE : {settings.score}", 40, (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT/2 - 140), settings.BLACK)
            description_button.draw(screen)
            
            # 更新畫面
            pygame.display.update()      
                
# 主迴圈
if __name__ == "__main__":
    current_screen = "main_menu"
    while True:
        if current_screen == "main_menu":
            current_screen = main_menu()
        elif current_screen == "game":
            current_screen = game_screen()
        elif current_screen == "description":
            current_screen = game_description()
        elif current_screen == "pause":
            current_screen = pause()
