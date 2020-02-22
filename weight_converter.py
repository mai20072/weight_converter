from tkinter import *
from tkinter import ttk


class mainWindow(object):
    def __init__(self,master):
        self.master = master
        self.master.title("Weight Converter")
        self.master.geometry("500x400")
        self.master.resizable(False,False)


def main():
    root = Tk()
    mainWindow(root)
    root.mainloop()

if __name__=='__main__':
    main()