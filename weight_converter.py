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

class functionality(mainWindow):
    def __init__(self,master):
        super().__init__(master)

        self.fromleb = Label(self.frameDown,text = "Conversion type:")
        self.fromleb.grid(pady=5,row=0)
        
        self.fromlist = list([" ", "Kg -> Lbs", "Lbs -> Kg"])
        self.varfrom = StringVar(master)
        self.varfrom.set(self.fromlist[0])
        self.popupfrommenu = OptionMenu(self.frameDown ,self.varfrom,*self.fromlist)
        self.popupfrommenu.grid(pady=5,row=0,column=1,sticky=E)
        
        self.convb = Button(self.frameDown ,text = "Convert")
        self.convb.grid(pady=5,padx=5,row=3,column=0,sticky=W)

        

        self.savef = Button(self.frameDown ,text = "Save As...")
        self.savef.grid(pady=5,row=3,column=1,sticky=W)

    def conv(self):
        """ convertion fuction """ 
        try:self.textname2.delete(1.0,END)
        except:pass
        corf = 0

        if self.varfrom.get() == " ":
            print(2)
            msg.showerror("Error", "Choose a conversion type!")
        else:
            #try:
            self.lines = (self.textname.get(1.0,END).replace(' ','\n').replace(',','\n'))
            self.lines = (self.lines.splitlines())
            self.lines = self.lines[0:len(self.lines)] 
            self.lines = [ x for x in self.lines if x.replace('.', '', 1).isdigit()  ]
            for i in range(len(self.lines)):self.lines[i] = float(self.lines[i])
            corf=1

        if corf==1:
            for i in self.lines:
                if self.varfrom.get() == "Lbs -> Kg":
                    value = i*0.45359237
                    self.textname2.insert('end',value)
                    self.textname2.insert('end',"\n")
                elif self.varfrom.get() == "Kg -> Lbs":
                    value = i*2.20462
                    self.textname2.insert('end',value)
                    self.textname2.insert('end',"\n")

def main():
    root = Tk()
    functionality(root)
    root.mainloop()

if __name__=='__main__':
    main()
