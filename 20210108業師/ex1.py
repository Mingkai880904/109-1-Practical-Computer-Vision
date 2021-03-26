# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:13:33 2021

@author: user
"""
from tkinter import *
from PIL import Image,ImageTk,ImageDraw,ImageFilter
from tkinter import filedialog as fd #載入對話框
import os

ui = Tk()
ui.title("濾鏡練習")
ui.configure(bg="#efefef")
screen_w = ui.winfo_screenwidth() #回傳螢幕寬的像素
screen_h = ui.winfo_screenheight() #回傳螢幕高的像素

global ui_w,ui_h
ui_w=screen_w/2 #設定視窗 寬度為螢幕的二分之一
ui_h=screen_h/2 #設定視窗 高度為螢幕的二分之一

x = (screen_w - ui_w)/2 #設定視窗X軸 為視窗X軸的一半
y = (screen_h - ui_h)/2 #設定視窗Y軸 為視窗Y軸的一半

ui.geometry("%dx%d+%d+%d" % (ui_w,ui_h,x,y))

"""----------------------------------------------------------------------------------"""

def open_image(): #開啟圖片檔
    openfilename=fd.askopenfilename(initialdir=".",title="123",\
                 filetypes = (("圖片檔","*.jpg;*.png")
                              ,("所有檔案","*.*")))
    print(openfilename)
    
    global filename_
    filename = os.path.split(openfilename)[1] #分割路徑與檔名
    print(os.path.split(openfilename)[1])
    filename_ = filename.split('.')#分割檔名與副檔名
    print(filename_)
    
    jpg1 = Image.open(openfilename)  #開啟圖片
    jpg1_w,jpg1_h = jpg1.size #回傳原始圖片長寬
    print(jpg1_w,jpg1_h)
    
    global re #re為原始圖片大小 與 lab大小 之倍數
    if jpg1_w >= jpg1_h and jpg1_w > ui_w*0.4:
        re=(ui_w*0.4)/jpg1_w
    elif jpg1_h >= jpg1_w and jpg1_h > ui_h*0.6:
        re=(ui_h*0.6)/jpg1_h
    else:
        re=1
    
    global jpg1_tk
    jpg1_resize =jpg1.resize((int(jpg1_w*re),int(jpg1_h*re))) #重新定義圖片大小
    jpg1_tk = ImageTk.PhotoImage(jpg1_resize) #將圖片轉為TK相容的格式
    lab2.configure(image=jpg1_tk) #傳送圖片屬性給lab2
    lab2.image = jpg1_tk #顯示圖片
    global jpg2
    jpg2 = jpg1 #設定jpg2為後續處理圖片 全域變數

def lab4_img(): #傳送小圖至lab4，並顯示
    global jpg2_tk
    jpg2_tk = ImageTk.PhotoImage(out_jpg_resize)
    lab4.configure(image=jpg2_tk)
    lab4.image = jpg2_tk

def image_blur(): #模糊濾鏡
    global out_jpg,out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.BLUR)

    jpg2_w,jpg2_h = jpg2.size
    out_jpg_resize =jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.BLUR)
    lab4_img()
    
def image_sharpen(): #銳利濾鏡
    global out_jpg,out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.SHARPEN)

    jpg2_w,jpg2_h = jpg2.size
    out_jpg_resize =jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.SHARPEN)
    lab4_img()
    
def image_contour(): #黑白線條濾鏡
    global out_jpg,out_jpg_resize
    out_jpg = jpg2.filter(ImageFilter.CONTOUR)
    out_jpg=out_jpg.convert("1")

    jpg2_w,jpg2_h = jpg2.size
    out_jpg_resize =jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.CONTOUR)
    out_jpg_resize=out_jpg_resize.convert("1")
    lab4_img()
    
def aa(): #顏色疊加濾鏡
    global out_jpg,out_jpg_resize
    jpg2_col = Image.new('RGB',jpg2.size, "#faebd7")
    out_jpg = jpg2.filter(ImageFilter.SHARPEN)
    out_jpg = Image.blend(out_jpg,jpg2_col, 0.2)
    
    jpg2_w,jpg2_h = jpg2.size
    out_jpg_resize =jpg2.resize((int(jpg2_w*re),int(jpg2_h*re)))
    jpg2_col = Image.new('RGB',out_jpg_resize.size, "#faebd7")
    out_jpg_resize = out_jpg_resize.filter(ImageFilter.SHARPEN)
    out_jpg_resize = Image.blend(out_jpg_resize,jpg2_col, 0.2)
    lab4_img()

def image_save(): #儲存圖片至程式目錄
    out_jpg.save(filename_[0]+"_uot.jpg")

def btn_view_down(event):#當按下按鈕時，執行動作(回調函數)
    lab4.configure(image=jpg1_tk)
    lab4.image = jpg1_tk

def btn_view_up(event):#當放開按鈕時，執行動作(回調函數)
    lab4.configure(image=jpg2_tk)
    lab4.image = jpg2_tk

"""----------------------------------------------------------------------------------"""

lab1=Label(ui,
           text="原始照片", #文字內容
           bg="#efefef", #背景色
           font="微軟正黑體 16 bold underline", 
           #bold粗體、underline 底線 、overstrike刪除線
           fg="#333333" #文字顏色           
           )

lab2=Label(ui,
           text="", #文字內容
           bg="#ffffff", #背景色
           font="微軟正黑體 20 underline", 
           #bold粗體、underline 底線 、overstrike刪除線
           fg="#333333", #文字顏色
           relief="groove", #邊框樣式 raised,ridge,sunken,groove,solid
           bd=1 #邊框寬度
           )

lab3=Label(ui,
           text="濾鏡效果", #文字內容
           bg="#efefef", #背景色
           font="微軟正黑體 16 bold underline", 
           #bold粗體、underline 底線 、overstrike刪除線
           fg="#333333" #文字顏色          
           )

lab4=Label(ui,
           text="", #文字內容
           bg="#ffffff", #背景色
           font="微軟正黑體 20 underline", 
           #bold粗體、underline 底線 、overstrike刪除線
           fg="#333333", #文字顏色
           relief="groove", #邊框樣式 raised,ridge,sunken,groove,solid
           bd=1 #邊框寬度
           )


btn1=Button(ui,
           text="疊加", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。   
           command=aa
           )

btn_open= Button(ui,
           text="開啟圖片", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。    
           command=open_image
           )

btn_save= Button(ui,
           text="儲存圖片", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。   
           command=image_save
           )



btn_blur= Button(ui,
           text="模糊", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。   
           command=image_blur
           )

btn_sharpen= Button(ui,
           text="銳利", #文字內容
           bg="#a9a9a9", #背景色
           fg="#000000", #文字顏色
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff", #按下按鈕時的背景顏色。
           activeforeground="#000fff", #按下按鈕時的文字顏色。   
           command=image_sharpen
           )

btn_contour= Button(ui,
           text="線條",
           bg="#a9a9a9",
           fg="#000000",
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff",
           activeforeground="#000fff",
           command=image_contour
           )

btn_view= Button(ui,
           text="比對",
           bg="#a9a9a9",
           fg="#000000",
           font="微軟正黑體 16 bold",
           anchor="center",
           relief="groove",
           bd=2,
           activebackground="#ffffff",
           activeforeground="#000fff"
           )

"""----------------------------------------------------------------------------------"""

lab1.place(relwidth=0.2,relheight=0.1,
           relx=0.15,rely=0.1)

lab2.place(relwidth=0.4,relheight=0.6,
           relx=0.05,rely=0.2)

lab3.place(relwidth=0.2,relheight=0.1,
           relx=1-0.15-0.2,rely=0.1)

lab4.place(relwidth=0.4,relheight=0.6,
           relx=1-0.05-0.4,rely=0.2)

btn1.place(relwidth=0.08,relheight=0.1,
           relx=0.46,rely=0.70)

btn_open.place(relwidth=0.15,relheight=0.1,
           relx=0.05+0.2-0.075,rely=0.85)

btn_save.place(relwidth=0.15,relheight=0.1,
           relx=1-0.05-0.4+0.125,rely=0.85)

btn_blur.place(relwidth=0.08,relheight=0.1,
           relx=0.46,rely=0.25)

btn_sharpen.place(relwidth=0.08,relheight=0.1,
           relx=0.46,rely=0.40)

btn_contour.place(relwidth=0.08,relheight=0.1,
           relx=0.46,rely=0.55)

btn_view.place(relwidth=0.08,relheight=0.1,
           relx=0.46,rely=0.85)

"""----------------------------------------------------------------------------------"""


btn_view.bind('<ButtonPress-1>',btn_view_down)#按下按鈕
btn_view.bind('<ButtonRelease-1>',btn_view_up)#放開按鈕

lab4.bind('<ButtonPress-3>',btn_view_down)#按下圖片
lab4.bind('<ButtonRelease-3>',btn_view_up)#放開圖片

ui.mainloop()