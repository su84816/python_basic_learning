#from益詠
import sys

in_num = int(sys.stdin.read())

#起始條件
init_a = 0

init_b = 1

count = 0

if in_num == 1:
    print(init_a)

elif in_num == 2:
    print(init_b)

in_num = in_num - 2

while in_num - count > 0:
    count = count + 1

    if count % 2 == 1:
        init_a = init_a + init_b

    if count % 2 == 0:
        init_b = init_a + init_b

if count != 0:
    if count % 2 == 1:
        print(init_a)

    elif count % 2 == 0:
        print(init_b)