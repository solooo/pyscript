# -*- coding: utf-8 -*-
import os
# import win32com
# from win32com.client import Dispatch, constants
# wordApp = win32com.client.Dispatch('Word.Application')
# # 后台运行，显示，不警告
# wordApp.Visible = 0
# wordApp.DisplayAlerts = 0
#
# doc = wordApp.Documents.Open("C:\\Users\\Administrator\\Desktop\\tmp\\智慧幼儿园-程序代码.docx")

path = "C:\\Users\\Administrator\\Desktop\\tmp\\yry_code"
word = open("C:\\Users\\Administrator\\Desktop\\tmp\\code.txt", "w", encoding='utf-8')
for java in os.listdir(path):
    f = open(path + "\\" + java, encoding='utf-8')
    print(java)
    word.write(f.read())
    f.close()
# doc.save()
word.close()
print("over!")
