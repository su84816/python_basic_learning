import sys

read = sys.stdin.read()
new_r = read.split()

# print(new_r)
for str in new_r:
    print(str)

#map寫法
# ans = map(str,new_r)
# res = list(ans)
# print(res)

#python main.py < in1.txt