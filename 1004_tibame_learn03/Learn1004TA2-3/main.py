import sys

read = int(sys.stdin.read())

i = 2
ind = read-1
ans=[]
ans.append(0)
ans.append(1)
while True:
    a = ans[i-1]+ans[i-2]
    ans.append(a)
    i = i + 1
    if i > read + 5:
        break

print(ans[ind])
# print(ans)
        
# print(ans)
#python main.py < in1.txt

#####老師寫法
# import sys

# in_txt = sys.stdin.read()

# in_int_txt = int(in_txt) - 1

# first = 0
# second = 1

# if in_int_txt == 0:
#     print(0)
# elif in_int_txt == 1:
#     print(1)
# else:
#     i = 0

#     while i < in_int_txt - 1:
#         first, second = second, first + second
#         i += 1

#     print(second)