import random
f = 23800 #本金 ###資料不實!!109:24000,111基本薪資調漲,應該用爬蟲抓勞動部資料比較準確 https://www.mol.gov.tw/topic/3067/5990/
i = 1 #玩的次數
g = 10 #賭注
w = 0 #贏的次數
l = 0 #輸的次數
# roll = 0 #紀錄骰子次數
user_input = int(input('你想玩幾次?')) #Input:要玩幾次？

for x in range(user_input): #計數器<=使用者輸入就繼續
#for 一根香蕉 in 一串香蕉 >>>可迭代 "list"/"dict"使用
#for 


# java: for(i=0,i<6(判斷是)),i--(運算式)))

    a = random.randint(1,2) #2代表輸,1代表贏
        
    #print(a)
    
    if a == 1:
        w = w + 1
        f = f + g
        #print(f'Win  , 第 <{i}> 次 , 你贏了 "{g}" 元 , 本金 : {f} ')
        i = i + 1
        g = 10
        roll = 0
        continue #贏了就退出,用break
        
    if a == 2:
        l = l + 1
        f = f - g
        g = g * 2
        #print(f'Lose , 第 <{i}> 次 , 你輸了 "{int(g/2)}" 元 , 本金 : {f} ')
        i = i + 1
        roll = roll + 1
        continue
        
print(f'=====總計贏了{w}次 , 輸了{l}次 , 本金+損益{f} , 你的損益狀況是{f-23800}=====')