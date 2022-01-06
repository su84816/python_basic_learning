import sys

read = sys.stdin.read()

num_L = read.split()
# num_L = ['2','2']

x = 1

i = int(num_L[0])
j = int(num_L[1])

while x <= i:
    y = 1
    while y <= j and x <= i:
     print(f'{x}x{y}={x*y}')
     y = y + 1
    x = x + 1