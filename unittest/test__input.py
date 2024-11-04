import zipfile
import tkinter as tk
from tkinter.tix import WINDOW
from tkinter import *
from tkinter.filedialog import *

root = tk.Tk()
root.title("path choose")
root.geometry("200x200")
path = StringVar()

def selectPath():
    global path_
    path_ = askopenfile()
    if path_:
        path.set(path_)
    return path_

def loadfile_func():
    import shutil
    file = "../input/"
    file_name = path_
    shutil.copyfile(path_,file)
    open(file_name,mode='r')
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(file)

if __name__ == '__main__':
    selectPath()
    print(path_)
    loadfile_func()

root.mainloop()