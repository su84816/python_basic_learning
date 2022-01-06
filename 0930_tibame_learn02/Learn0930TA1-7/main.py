import sys
import math

read = sys.stdin.read() 

if '+' in read :
    a = read.split('+')
    num_1 = int(a[0])
    num_2 = int(a[1])
    print(f'{num_1+num_2}')
elif '-' in read :
    a = read.split('-')
    num_1 = int(a[0])
    num_2 = int(a[1])
    print(f'{num_1-num_2}')
elif '*' in read :
    a = read.split('*')
    num_1 = int(a[0])
    num_2 = int(a[1])
    print(f'{num_1 * num_2}')
elif '/' in read :
    a = read.split('/')
    num_1 = int(a[0])
    num_2 = int(a[1])
    b = num_1 // num_2
    print(f'{math.floor(b)}')


# 注意!
# 在做整數除法的時候，請直接無條件捨去至整數，不需要保留小數點
# ex: 5 / 5 = 1.0
# 請輸出1

# 輸入為一組只有一個運算符號(+、-、*、/)的算式，請輸出算式的答案
# 注意! 輸入不會有任何的空白

#使用python main.py < in1.txt 呼叫
