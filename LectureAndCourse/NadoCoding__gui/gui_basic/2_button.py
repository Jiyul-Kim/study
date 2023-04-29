from tkinter import *

root = Tk()
root.title("나도 GUI")
root. geometry("640x480") # 가로 x 세로 + x 좌표 + y좌표
#root.resizable(False, False) # x , y 의 창 크기 값 변경 불가


btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root,padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root,padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4')
btn4.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn5= Button(root, text="동작하는 버튼", command=btncmd)
btn5.pack()
root.mainloop()