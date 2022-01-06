try:
    pwd = input("請輸入您的密碼: ")
    if len(pwd)<8:
        raise Exception("密碼長度不足")
    if len(pwd)>16:
        raise Exception("密碼長度太長")
except Exception as e:
    print("密碼長度檢查異常: " + e) 
# with open('file.txt','r') as f:
#     print(f.read())
# # f = open('write.txt', 'w', encoding='utf-8')
# # f.write("Write file!")
# # f.close() # 記得要關閉檔案，不然會造成很奇怪的問題

# # # class Chair():
# # #     pass
# # #     def __init__(self,c):
# # #         self.color = c
# # #     def seat(self) :
# # #         print(self.color,'的椅子很好坐')
    

# # # # a_chair = Chair("Green")
# # # # a_chair.seat()
# # # # b_chair = Chair("Yello")
# # # # a_chair.seat()

# # # # print(a_chair.color)

# # # # Chair.seat(a_chair)

# # # # # class Chair():
# # # # #     def set_color(self,c):
# # # # #         self.color = c

# # # # # a_chair = Chair()
# # # # # a_chair.set_color = "Green"

# # # # # b_chair = Chair()
# # # # # b_chair.set_color = "Red"

# # # # # print(a_chair.set_color)
# # # # # print(b_chair.set_color)

# # # # # # def sam_first(name="預設"):
# # # # # #     sam = name
# # # # # #     return sam

# # # # # # test = sam_first("")
# # # # # # print(test)

# # # # # # # from pytube import YouTube

# # # # # # # YouTube('https://www.youtube.com/watch?v=SlAQndqFGew').streams.first().download()
# # # # # # # yt = YouTube('https://www.youtube.com/watch?v=SlAQndqFGew')
# # # # # # # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
# # # # # # # # no1_dict = {'name':'Sam','no':'1','sex':'men'}
# # # # # # # # no2_dict = {'name':'Rain','no':'2','sex':'women'}

# # # # # # # # # #串列生成式
# # # # # # # # # print([str(i) for i  in range(5)])