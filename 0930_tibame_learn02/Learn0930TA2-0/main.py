import sys
read = int(sys.stdin.read()) 

a = 0
b = 0

while a <= read :
   b = a + b   
   a = a + 1

print(f'{b}') #放哪裡很重要

#使用python main.py < in1.txt 呼叫