from tkinter import *

root = Tk()
root.title("나도 GUI")
root. geometry("640x480") # 가로 x 세로 + x 좌표 + y좌표

btn1 = Button(root,text="버튼1")
btn2 = Button(root,text="버튼2")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)


root.mainloop()