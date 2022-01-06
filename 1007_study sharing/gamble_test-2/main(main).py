import random
f = 23800 #本金
i = 1 #玩的次數
g = 1 #賭注
w = 0 #贏的次數
l = 0 #輸的次數


for x in range(0,10): #玩10次
    a = random.randint(1,2) #1代表輸,2代表贏
        
    print(a)
    
    if a == 1:
        w = w + 1
        f = f + g
        print(f'Win  , 第 <{i}> 次 , 你贏了 "{g}" 元 , 本金 : {f} ')
        i = i + 1
        g = 1
        continue #贏了就退出,用break
        
    if a == 2:
        l = l + 1
        f = f - g
        g = g * 2
        print(f'Lose , 第 <{i}> 次 , 你輸了 "{int(g/2)}" 元 , 本金 : {f} ')
        i = i + 1
        continue
        
print(f'=====總計贏了{w}次 , 輸了{l}次 , 本金{f}=====')