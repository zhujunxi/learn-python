"""
花旗骰

Version: 0.1
Author: github
"""
import random
import os

money = 100
num = 1

while money > 0:    
    print('------ 第%d局 - 当前资产为：%d 元 --------' % (num, money))
    num += 1
    needs_go_on = False
    counter = 1
    while True:
        debt = int(input('请下注：'))
        if 0< debt <= money:
            break
    first = random.randint(1, 6) + random.randint(1, 6)
    print('第%d轮摇出了%d点' % (counter, first))
    if first == 7 or first == 11:
        money += debt
        print('玩家胜利')
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('庄家胜利')
    else:
        print('首轮未决胜负，游戏继续')
        needs_go_on = True
    
    while needs_go_on:
        current = random.randint(1, 6) + random.randint(1, 6)
        counter += 1

        print('第%d轮摇出了%d点' % (counter, current))
        
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False
        else:
            needs_go_on = True
    # n=os.system('cls')

print('-GAME OVER-')

