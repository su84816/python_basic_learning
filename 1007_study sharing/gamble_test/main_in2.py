import random
f = 23800 #本金 ###資料不實!!109:24000,111基本薪資調漲,應該用爬蟲抓勞動部資料比較準確 https://www.mol.gov.tw/topic/3067/5990/
i = 1 #玩的次數
g = 10 #賭注
w = 0 #贏的次數
l = 0 #輸的次數
user_input = int(input('你想賺多少錢?')) #Input:我要贏到多少錢？

while f < user_input: #只要本金比user輸入的少就繼續
    a = random.randint(1,2) #1代表輸,2代表贏
        
    #print(a)
    
    if a == 1:
        w = w + 1
        f = f + g
        # print(f'Win  , 第 <{i}> 次 , 你贏了 "{g}" 元 , 本金 : {f} ')
        i = i + 1
        g = 10
        continue #贏了就退出,用break
        
    if a == 2:
        l = l + 1
        f = f - g
        g = g * 2
        # print(f'Lose , 第 <{i}> 次 , 你輸了 "{int(g/2)}" 元 , 本金 : {f} ')
        i = i + 1
        continue
if user_input < f:
    print('別玩了...你本來就有')
elif user_input > 150000:
    print('作夢吧....夢裡啥都有...(程式跑太久了辣)')  #如何加速?
else:           
    print(f'=====總計玩了{i}次,贏了{w}次 , 輸了{l}次=====')