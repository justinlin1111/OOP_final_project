sprite就是一個比較方便做一些管理的群，裡面有一些像是all_sprites.update()就是會直接執行被加到all_sprites裡所有物件的update函數，我會分幾種是因為他們本身不是同一個類型的，加上有些update需要其他參數，加到all_sprite我不知道會不會有問題，所以就分開寫了

這個遊戲我們預計會做成隨著時間難度會越高的肉割遊戲，其中會有包含:
1. 敵人生成(O)
    1. 從螢幕邊緣生成(在enemies的__init__做)(O)
    2. 從天而降生成(random + 動畫)(O)
    3. 敵人會在每十秒就生成一次(O)
2. 敵人強度
    1. 以顏色來代表(在主畫面要有提示說強度的顏色分布)
    2. 複製玩家當下的能力(可能需要一個新的類別，事後把它新增到sprite的enemies就好)
3. 扣血機制(O)
    1. 玩家碰觸到敵人或被敵人攻擊(我還沒寫被敵人攻擊，所以這部分也需要在敵人寫攻擊之後做邏輯判斷、碰觸敵人只要在main裡面利用groupcollide就可以了)
4. 升級機制(O)
    1. 擊敗敵人會獲得大量經驗用以提升數值(O)
    2. 隨著時間會少量增加經驗(用上面方法的話只要寫在player的update就可)(O)
，一旦血量耗盡遊戲就結束，最終的成績根據他們在遊戲中存活的時間與擊敗的敵人數量判定(在更新遊戲的地方多做判斷就好，如果沒血了就跳回主畫面(HOME SCREEN))