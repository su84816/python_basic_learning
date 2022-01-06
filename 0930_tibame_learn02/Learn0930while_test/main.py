#巢狀迴圈-以九九乘法表為例
i = 1

while i < 14:
  j = 1
  
  while j < 16:
    print(f'{i} x {j} = {i*j}')
    j = j + 1

  i = i + 1

# import random
# # random.randint(1,6)
# i = 0
# j = 0
# while i <= 60:
#   j += 1 
#   i += random.randint(1,6)
# print(j)

# # 1. 初始條件
# i = 0

# # 2. 判斷條件
# while i <= 6:
#   print(f'Hello-{i+1}')
  
#   # 更新條件
#   i += 1
  
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World