from tkinter import *
from tkinter import ttk


class mainWindow(object):
    def __init__(self,master):
        self.master = master
        self.master.title("Weight Converter")
        self.master.geometry("500x400")
        self.master.resizable(False,False)

        self.frameUpper = Frame(self.master)
        self.frameUpper.pack(fill=X)

        self.frameMiddle = Frame(self.master)
        self.frameMiddle.pack(fill=BOTH,expand=1)

        self.frameDown = Frame(self.master)
        self.frameDown.pack(fill=BOTH,expand=1)

        self.amleb = Label(self.frameUpper,text = "Input Data")
        self.amleb.grid(row=0,column=0)

        self.amleb2 = Label(self.frameUpper,text = "Results")
        self.amleb2.grid(row=0,column=1,padx=190,sticky=E)
        
        self.textname = Text(self.frameMiddle)
        self.textname.pack(fill=BOTH,expand=Y,side=LEFT)
        self.s = ttk.Scrollbar(self.textname, orient=VERTICAL, command=self.textname.yview)
        self.s.pack(fill=Y, side=RIGHT)
        self.textname.configure(yscrollcommand=self.s.set)
        
        self.textname2 = Text(self.frameMiddle)
        self.textname2.pack(fill=BOTH,expand=Y,side=RIGHT)
        self.s2 = ttk.Scrollbar(self.textname2, orient=VERTICAL, command=self.textname2.yview)
        self.s2.pack(fill=Y, side=RIGHT)
        self.textname2.configure(yscrollcommand=self.s2.set)

def main():
    root = Tk()
    mainWindow(root)
    root.mainloop()

if __name__=='__main__':
    main()
