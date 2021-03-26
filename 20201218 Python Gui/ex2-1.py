# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:43:56 2020

@author: 沈明楷
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:04:16 2020

@author: user
"""
from tkinter import *

ui = Tk()
ui.title("ex1-2")
ui.configure(bg="lightblue")

screen_w = ui.winfo_screenwidth() #回傳螢幕寬的像素
screen_h = ui.winfo_screenheight() #回傳螢幕高的像素

w=screen_w/2 
h=screen_h/3

x = (screen_w - w)/4 
y = (screen_h - h)/2

ui.geometry("%dx%d+%d+%d" % (w,h,x,y))


"""----------------------------------------------------------------------------------"""

lab1=Label(ui,
           text=" 搜尋", #文字內容
           bg="#ffffff", #背景色
           fg="#555555", #文字顏色
           width=30,
           height=2,
           anchor="w",
           relief="groove",
           bd=2
           )

lab2=Label(ui,
           text="submit", #文字內容
           bg="#999999", #背景色
           fg="#000000", #文字顏色
           width=10,
           height=2,
           anchor="center",
           relief="groove",
           bd=2           
           )

lab3=Label(ui,
           text="您尚未查詢", #文字內容
           bg="#ffffff", #背景色
           fg="#000000", #文字顏色
           width=20,
           height=5,
           anchor="center",
           relief="groove",
           bd=2           
           )

"""----------------------------------------------------------------------------------"""
ui.columnconfigure(0,weight=1)
ui.rowconfigure(1,weight=1)

lab1.grid(row=0,column=0,
          padx=5,pady=5,sticky=W+E)
lab2.grid(row=0,column=1,
          padx=5,pady=5,)
lab3.grid(row=1,column=0,columnspan=2,
          padx=5,pady=5,sticky=W+E+S+N)

"""----------------------------------------------------------------------------------"""
ui.mainloop()