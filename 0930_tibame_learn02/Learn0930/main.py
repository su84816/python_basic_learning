import random

key_word = ['剪刀', '石頭', '布']

rand_num = random.randint(0, 2)

user = int(input('[0]剪刀, [1]石頭, [2]布:'))
while user != 0 and user != 1 and user !=2:
    print('輸入錯誤,請重新輸入') #>>>>這邊要做非數字輸入的排除
    user = int(input('[0]剪刀, [1]石頭, [2]布:'))

if user == 0 or user == 1 or user == 2 :
   print('電腦出了: ', key_word[rand_num])
   print('你出了: ', key_word[user])
  
if user == rand_num :
  print('你們平手')
elif user == (rand_num + 1) % 3 : #用餘數作為演算方式,同樣適用於%4...以上的模式
  print('你贏了')
else :
  print('電腦贏了')  

#作法二：如果user - rand_num剛好等於1或是user - rand_num等於-2，就是你贏


#苦功做法
# if user == rand_num :
#   print('你們平手')
# elif user == 0 and rand_num == 2 :
#   print('你贏了')
# elif user == 1 and rand_num == 0 :
#   print('你贏了')
# elif user == 2 and rand_num == 1 :
#   print('你贏了')
# else :
#   print('電腦贏了')  

# ----------比較----------

# 背後是數字的比較
# 1. 是不是平手
# 2. 你是不是贏了
# 3. 電腦贏了