import os
from tkinter import *

root = Tk()
root.title("제목 없음")
root. geometry()


########################### 스크롤기능 ###########################
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

########################### 메모장 기능 ###########################

txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand=True, side="left")
scrollbar.config(command=txt.yview)


########################### 메뉴 ###########################
menu=Menu(root)

# 파일
# 파일 열기, 저장

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 true
        with open (filename, 'r', encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert (END, file.read()) # 파일 내용을 본문에 입력


def save_file():
    with open (filename, 'w', encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

def close():
    root.destroy()

menu_file = Menu(menu, tearoff=0)
menu_file.add_command (label="열기", command=open_file)
menu_file.add_command (label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command (label="끝내기", command=close)
menu.add_cascade(label="파일", menu=menu_file )

# 편집
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit )

# 서식
menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_format )

# 보기
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view)

# 도움말
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_help)



root.config(menu=menu)
root.mainloop()