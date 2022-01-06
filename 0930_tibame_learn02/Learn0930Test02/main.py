import random
read = int(input('請猜個數字(1-100):'))
ans = random.randint(1,100)
a = 1
b = 100

print(ans)

#待補try except防呆
while True :
    if ans > read:
        a = read
        read = int(input(f'繼續猜:範圍{a}~{b}:'))
        while read < a or read > b:
           read = int(input(f'輸入超出範圍:範圍{a}~{b}:'))
        
    elif ans < read:
        b = read
        read = int(input(f'繼續猜:範圍{a}~{b}:'))
        while read < a or read > b:
            read = int(input(f'輸入超出範圍:範圍{a}~{b}:'))
     
    else:
      print (f'猜對了!答案是{ans}')
      break
      
# #v1
# import random
# read = int(input('請猜個數字(1-100):'))
# ans = random.randint(1,100)
# a = 1
# b = 100
# print(ans)


# while read != ans :
#     if ans > read:
#       while read - a > b - read :
#         b = read
#         read = int(input(f'繼續猜:範圍{a}~{b}:'))
        
#         if read < a or read > b:
#             read = int(input(f'輸入超出範圍:範圍{a}~{b}:'))
#     if ans < read:
#       while read - a < b - read :
#         a = read
#         read = int(input(f'繼續猜:範圍{a}~{b}:'))
        
#         if read < a or read > b:
#             read = int(input(f'輸入超出範圍:範圍{a}~{b}:'))

# print (f'猜對了!答案是{ans}')

# # import random

# # bumb = random.randint(1, 100)

# # min_num = 1
# # max_num = 100

# # while True:
# #     guess = int(input(f'請{min_num}~{max_num}猜一個數字:'))
# #     if guess == bumb:
# #         print('猜中喇!!')
# #         break
# #     else:
# #         # 猜的數字比正確數字小 -> 修改min
# #         # 猜的數字比正確數字大 -> 修改max
# #         if guess < bumb:
# #             min_num = guess
# #         else:
# #             max_num = guess