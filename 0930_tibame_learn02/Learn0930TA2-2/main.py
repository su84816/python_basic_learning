import sys

read = sys.stdin.read() 
new_read = read.split() #資料處理
len = len(new_read) #list長度
ans_list = []
# space = []
x = 0

# while x < len :
#     space[x] = ' '
#     x = x + 1

while x < len :
    ans_list.append(int(new_read[x])+1)
    x = x + 1

print (' '.join(str(i) for i in ans_list)) #因為List裡面都是int,要轉成str才能用join

# i = 0
# ans = ''

# while i < len(str):
#   ans += str(str[i+1]) + ''
#   i = i + 1

# print(ans.strip())
# #最後會多一個空白,所以
# #使用python main.py < in1.txt 呼叫