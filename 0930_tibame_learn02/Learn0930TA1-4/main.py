import sys

L = sys.stdin.read() 
#Step1:資料處理,區分成兩個陣列(user&PC),分別用變數儲存
new_L = L.split(',')

L_user = new_L[0].split()

L_PC = new_L[1].split()

count = 0 #計數器

if L_user[0] in L_PC:
  count += 1 
  
if L_user[1] in L_PC:
  count = count + 1  

if L_user[2] in L_PC:
  count = count + 1

if L_user[3] in L_PC:
  count = count + 1

if L_user[4] in L_PC:
  count = count + 1


if count < 3:
  print('0')
elif count == 3:
  print('100')
elif count == 4:
  print('1000')
elif count == 5:
  print('10000')



# print(L_user)
# print(L_PC)

#使用python main.py < in1.txt 呼叫




