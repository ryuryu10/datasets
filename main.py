#!/usr/bin/python
# -*- coding:utf-8 -*
from logging import root
import tkinter as tk
import tkinter.ttk as ttk
import ctypes
import math
import json

root = tk.Tk()

global Data_View

def Window_installation():
    try:
        User32 = ctypes.windll.user32
        USMW = math.trunc((User32.GetSystemMetrics(0) / 2))
        USMH = math.trunc((User32.GetSystemMetrics(1) / 2))
    except:
        pass
        USMW = 500
        USMH = 500
    PSSW = 890
    PSSH = 420
    MPSW = math.trunc(PSSW / 2)
    MPSH = math.trunc(PSSH / 2)
    SS = "{0}x{1}+{2}+{3}".format(
        PSSW,
        PSSH,
        USMW-MPSW,
        USMH-MPSH
    )
    root.geometry(SS)
    root.resizable(False, False)
    root.lift()

def Window_design():
    global Data_View

    window_title = tk.Label(root)
    window_title.place(x=9, y=10, height=47, width=352)
    window_title.configure(font="-family {나눔고딕} -size 19")
    window_title.configure(text='''Vioce Datasets Configurator''')

    Data_View_AREA = tk.LabelFrame(root)
    Data_View_AREA.place(x=10, y=60, height=234, width=709)
    Data_View_AREA.configure(text='''데이터 뷰어''')
    
    scrollbar = tk.Scrollbar(Data_View)
    scrollbar.pack(side="right", fill="y")

    Data_View = tk.ttk.Treeview(root, 
        column=["a", "age", "grade"], 
        displaycolumns=["a", "age", "grade"],
        yscrollcommand = scrollbar.set
        )
    Data_View.pack()

    Data_View.column("a", width=60, anchor="center")
    Data_View.heading("a", text="Sector", anchor="center")

    Data_View.column("age", width=60, anchor="center")
    Data_View.heading("age", text="Num", anchor="center")

    Data_View.column("grade", width=565, anchor="center")
    Data_View.heading("grade", text="Sentence", anchor="center")
    Data_View["show"] = "headings"
    Data_View.place(x=20, y=80, height=209)

    Input_AREA = tk.LabelFrame(root)
    Input_AREA.place(x=9, y=300, height=84, width=710)
    Input_AREA.configure(text='''데이터 입력''')

    Detail_Value = ttk.Entry(root)
    Detail_Value.place(x=69, y=350, height=21, width=85)

    Sector_Value = ttk.Entry(root)
    Sector_Value.place(x=69, y=320, height=21, width=85)

    Sentence_Value = ttk.Entry(root)
    Sentence_Value.place(x=237, y=320, height=21, width=375)

    Sentence_Label = ttk.Label(root)
    Sentence_Label.place(x=168, y=320, height=19, width=66)
    Sentence_Label.configure(text='''Sentence :''')

    Sector_Label = ttk.Label(root)
    Sector_Label.place(x=20, y=320, height=19, width=47)
    Sector_Label.configure(text='''Sector :''')

    Detail_Label = ttk.Label(root)
    Detail_Label.place(x=20, y=350, height=19, width=47)
    Detail_Label.configure(text='''Detail :''')

    Directory_Label = ttk.Label(root)
    Directory_Label.place(x=168, y=350, height=19, width=64)
    Directory_Label.configure(text='''Directory :''')

    Directory_Value = ttk.Entry(root)
    Directory_Value.place(x=237, y=350, height=21, width=375)

    PUSH_Button = ttk.Button(root)
    PUSH_Button.place(x=620, y=320, height=55, width=87)
    PUSH_Button.configure(text='''PUSH''')

    Labelframe3 = tk.LabelFrame(root)
    Labelframe3.place(x=730, y=60, height=325, width=150)
    Labelframe3.configure(text='''메뉴''')

    Status_Value = ttk.Label(root)
    Status_Value.place(x=10, y=390, height=19, width=865)
    Status_Value.configure(text='''[STATUS] READY''')

    Select_Button = ttk.Button(root)
    Select_Button.place(x=740, y=80, height=35, width=127)
    Select_Button.configure(text='''파일 선택''')

    Open_Button = ttk.Button(root)
    Open_Button.place(x=740, y=120, height=35, width=127)
    Open_Button.configure(text='''파일 열기''')

    Save_button = ttk.Button(root)
    Save_button.place(x=740, y=160, height=35, width=127)
    Save_button.configure(text='''저장''')

def Select_button():
    data_list = []
    with open('son-recognition-All.json', "r") as myfile:
        json_data = json.load(myfile)
        for e, v in json_data.items():
            data_list.append((e[-12:][0:3],e[-12:][4:8],'a'))
        for i in range(len(data_list)):
            Data_View.insert("", "end", text="", values=data_list[i], iid=i)

def main():
    treeValueList = [("1", '0000', "A"),
                 ("1", '0245', "B"),
                 ("2", '21', "C")]

    
    root.mainloop()

if __name__ == "__main__":
    Window_installation()
    Window_design()
    Select_button()
    main()
