import os
import time
import tkinter as tk
from tkinter import filedialog
import re

# 变量初始化
file_list = []
new_filelist = []
d = 1

window = tk.Tk()  # 创建窗口，命名为window
window.title('PowerRename')  # 赋予窗口名
window.geometry("660x300")  # 设置窗口大小
# 路径组
l1 = tk.Label(window, text='路径：')  # 设置标签
l1.place(x=20, y=15)  # 放置标签
hint = tk.StringVar()


def when_enter(a):
    try:
        old_list.delete(0, "end")
        flash_list(entry_path.get())
    except FileNotFoundError as ex:
        hint.set(ex)
    a = 0


entry_path = tk.Entry(window)
entry_path.place(x=60, y=15)
entry_path.bind('<Return>', when_enter)
# 筛选组
l2 = tk.Label(window, text='筛选：')  # 设置标签
l2.place(x=220, y=15)  # 放置标签
# 改名组
l4 = tk.Label(window, text="替换：")
l4.place(x=420, y=15)
rename_list = tk.Listbox(window)
rename_list.place(x=460, y=50)


def renamer():
    global d
    print(d)
    filelist = new_filelist
    n = 0
    m = 0
    d = 1
    print(filelist)
    for i in filelist:
        timeStamp = os.path.getctime(entry_path.get() + "/" + str(new_filelist[n]))
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime(entry_rename.get(), timeArray)
        rename_list.insert(0, otherStyleTime)
        oldname = entry_path.get() + os.sep + filelist[n]
        print(oldname)
        if os.path.isfile(oldname):
            newname = entry_path.get() + os.sep + str(int(otherStyleTime)+1+m) + '.md'
            os.rename(oldname, newname)
            print(oldname, '======>', newname)
        n += 1
        m += 1
    when_enter_rename(1)


def when_enter_rename(c):
    n = 0
    global d
    rename_list.delete(0, "end")
    for i in new_filelist:
        if d == 0:
            renamer()
            break
        else:
            timeStamp = os.path.getctime(entry_path.get() + "/" + str(new_filelist[n]))
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime(entry_rename.get(), timeArray)
            rename_list.insert(0, otherStyleTime)
            n += 1
    d = 1


entry_rename = tk.Entry(window)
entry_rename.insert('insert', "%y%m%d%H%M%S")
entry_rename.place(x=460, y=15)
entry_rename.bind('<Return>', when_enter_rename)


def when_enter_re(b):
    global new_filelist
    global d
    new_list.delete(0, "end")
    new_filelist = []
    for data in file_list:
        if re.match(entry_re.get(), data) is not None:
            new_filelist.append(data)
    new_list.delete(0, "end")
    for item in new_filelist:  # 将所获得的列表全部刷新
        new_list.insert(0, item)
    d = 1
    when_enter_rename(1)
    b = 0


entry_re = tk.Entry(window)
entry_re.place(x=260, y=15)
entry_re.bind('<Return>', when_enter_re)
# 新旧列表
old_list = tk.Listbox(window)
old_list.place(x=60, y=50)  # 将小部件放置到主窗口中
new_list = tk.Listbox(window)
new_list.place(x=260, y=50)
# 提示标签
l3 = tk.Label(window, textvariable=hint)
l3.place(x=175, y=254)


def hit_me():
    path = filedialog.askdirectory()  # 设置变量path为选中文件夹路径
    if path != '':
        entry_path.delete(0, "end")  # 按下按钮后文本框清零
        entry_path.insert('insert', path)  # 将变量path填充到文本框中
        flash_list(entry_path.get())
    else:
        pass
    hint.set('')


get_dir = tk.Button(window, text='选择路径', command=hit_me)
get_dir.place(x=100, y=250)


def gomi():
    global d
    d = 0
    when_enter_rename(1)


rename = tk.Button(window, text='ReName', command=gomi)
rename.place(x=500, y=250)


def flash_list(path):
    global file_list
    global dir_list
    global new_filelist
    global d
    old_list.delete(0, "end")
    new_list.delete(0, "end")
    file_list = []
    dir_list = []
    new_filelist = []
    dir_list = os.listdir(path)  # 将文本框获取内容放入dir_list
    # 在dir_list中遍历文件名，用os.path.join()拼接成绝对路径，再以os.path.isfile()判断是否为文件
    file_list = [name for name in dir_list if os.path.isfile(os.path.join(path, name))]
    for item in file_list:  # 将所获得的列表全部刷新
        old_list.insert(0, item)
    when_enter_re(1)
    d = 1
    when_enter_rename(1)


window.mainloop()  # 窗口常驻

