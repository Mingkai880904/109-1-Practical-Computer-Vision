# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:04:16 2020

@author: user
"""
from tkinter import *

ui = Tk()
ui.title("ex2")
ui.configure(bg="lightyellow")

screen_w = ui.winfo_screenwidth() #回傳螢幕寬的像素
screen_h = ui.winfo_screenheight() #回傳螢幕高的像素

w=screen_w/3 #設定視窗 寬度為螢幕的三分之一
h=screen_h/2 #設定視窗 高度為螢幕的三分之一

x = (screen_w - w)/2 #設定視窗X軸 為視窗X軸的一半
y = (screen_h - h)/2 #設定視窗Y軸 為視窗Y軸的一半

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))

#ui.rowconfigure(1,weight=1)
#ui.columnconfigure(0,weight=1)

"""----------------------------------------------------------------------------------"""

lab1=Label(ui,
           text="A", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2
           )

lab2=Label(ui,
           text="B", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab3=Label(ui,
           text="C", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab4=Label(ui,
           text="D", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab5=Label(ui,
           text="E", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab6=Label(ui,
           text="F", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=4,
           anchor="center",
           relief="groove",
           bd=2           
           )

"""----------------------------------------------------------------------------------"""

lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,columnspan=2,sticky=E+W)
#lab3.grid(row=0,column=2)
lab4.grid(row=1,column=0)
lab5.grid(row=1,column=1)
lab6.grid(row=1,column=2)


"""----------------------------------------------------------------------------------"""

#lab1.grid(row=0,column=0,sticky=W)
#lab2.grid(row=0,column=1,sticky=W+E)
#lab3.grid(row=0,column=2)
#lab4.grid(row=1,column=0,columnspan=2,sticky=W+E+S+N)
#lab5.grid(row=1,column=1)
#lab6.grid(row=1,column=2)

"""----------------------------------------------------------------------------------"""
ui.mainloop()