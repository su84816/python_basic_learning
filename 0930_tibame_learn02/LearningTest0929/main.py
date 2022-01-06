i = int(input ('安安你幾歲?'))
j = int(input ('安安你有多少錢?'))

a = 18
m = 20000

#使用or的話可以縮成第一行:if age > 18 or money > 10000
if i > 18:
   print(f'歡迎光臨')

elif i < a and j > m/2:
   print(f'歡迎光臨')
   
else:
   print(f'謝謝惠顧')

# 如果年紀大於18，顯示歡迎光臨

# 如果年紀小於18，但是money大於10000也顯示歡迎光臨

# 否則顯示謝謝惠顧


#巢狀寫法
# if age > 18:
# print( 'Welcom')
# else:
# if money > 10000:
# print('Welcom2')
# else:
# print('No')