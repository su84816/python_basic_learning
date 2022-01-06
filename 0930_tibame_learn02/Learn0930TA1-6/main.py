import sys

read = int(sys.stdin.read())

# 4. 西元年份除以 400 可整除，為閏年。
if read % 400 == 0 :
    print('True')
# 2. 西元年份除以 4 可整除，且除以 100 不可整除，為閏年。
elif read % 4 == 0 and read % 100 != 0:
    print('True')
# 1. 西元年份除以 4 不可整除，為平年。
elif read % 4 != 0:
    print('False')
# 3. 西元年份除以 100 可整除，且除以 400 不可整除，為平年
elif read % 100 == 0 and read % 400 != 0:
    print('False')

