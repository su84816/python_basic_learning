import sys

L = sys.stdin.read() 

new_L = L.split()

no_open = ['星期五' , '星期六' ,'星期日' ]

a = new_L[0]

b = int(new_L[1])

c = int(new_L[2])

if a in no_open :
  print("不開市")
# 苦工：
# if a == '星期五' or a == '星期六' or a == '星期日':
#   print("不開市")
else:
  print(b*c)


# print(f'{new_L[0]}')
# print(new_L[1])
# print(new_L[2])

#使用python main.py < in1.txt 呼叫




