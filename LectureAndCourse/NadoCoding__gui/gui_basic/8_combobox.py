import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("나도 GUI")
root. geometry("640x480") # 가로 x 세로 + x 좌표 + y좌표

values = [str(i) + '일' for i in range(1,32)] 
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonly_combobox.pack()
readonly_combobox.current(0) # 0번째 인덱스 값 선택


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()