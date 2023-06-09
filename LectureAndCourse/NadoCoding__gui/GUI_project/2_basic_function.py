import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__ / 서브 모듈은 import 안해줌
from tkinter import filedialog # 서브 모듈

root = Tk()
root.title("나도 GUI")
root.resizable(False,False)

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
                                        filetypes=(("PNG 파일", "*.png"), ("모든 파일","*.*")), \
                                        initialdir=r"E:\PYTHONWORKSPACE\pygame_project_02\images") # 최초의 경로를 보여줌 / 앞에 r을 붙혀주면 탈출문자로 인식 안함
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제
def delete_file():
    # list_file.curselection()

    for index in reversed(list_file.curselection()): #lst.revers 는 원래의 리스트 값 마저 순서를 뒤집는데, reversed(list)는 원래의 값은 보존하되, 값은 따로 뒤집어서 보여줌
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로 넓이: ", cmd_width.get())
    print("간격 : ", cmd_space.get())
    print("포맷 : ", cmd_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, padx=5, pady=5,width=12, text="선택 삭제", command=delete_file)
btn_delete_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipadx=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x", expand=True, padx=5, pady=5,ipady=4) # 높이 변경 

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipadx=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본 유지", "1024", "800", "640"]

cmd_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmd_width.current(0)
cmd_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]

cmd_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmd_space.current(0)
cmd_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]

cmd_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmd_format.current(0)
cmd_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar

frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipadx=5)


p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)



root.mainloop()