import sys

read = sys.stdin.read() 

first_str = str(read.split())

a = first_str[2] #英文字母

first_num = 0

num = 0
#可以用字典直接處理
id_data = {
    'A' : '10' ,
    'B' : '11' ,
    'C' : '12' , 
    'D' : '13' ,
    'E' : '14' ,
    'F' : '15' , 
    'G' : '16' ,
    'H' : '17' ,
    'I' : '34' , 
    'J' : '18' ,
    'K' : '19' ,
    'L' : '20' ,
    'M' : '21' , 
    'N' : '22' ,
    'O' : '35' ,
    'P' : '23' ,
    'Q' : '24' ,
    'R' : '25' ,
    'S' : '26' ,
    'T' : '27' ,
    'U' : '28' ,
    'V' : '29' ,
    'W' : '32' ,
    'X' : '30' ,
    'Y' : '31' ,
    'Z' : '33' ,
}
# key_data = id_data.keys
value_data = id_data.values()


# num = int(read[1])*8 + int(read[2])*7 + int(read[3])*6 + int(read[4])*5 + int(read[5])*4 + int(read[6])*3 + int(read[7])*2 + int(read[8])*1  + int(read[9])*1

# if (first_num + num) % 10 == 0:
#     print('合法')
# else:
#     print('不合法')
  

# #使用python main.py < in1.txt 呼叫




