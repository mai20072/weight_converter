from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog,ttk

import csv,os

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

        # menu 
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Open",accelerator = 'Ctrl+O')
        self.file_menu.add_command(label = "Convert",accelerator = 'Ctrl+T')
        self.file_menu.add_command(label = "Save",accelerator = 'Ctrl+S')
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4')
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu ( self.menu,tearoff = 0)
        self.edit_menu.add_command(label = "Clear text field",accelerator = 'Alt + S')
        self.menu.add_cascade(label = "Edit" , menu  = self.edit_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I')
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1')
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)

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
        
        self.convb = Button(self.frameDown ,text = "Convert", command=self.conv)
        self.convb.grid(pady=5,padx=5,row=3,column=0,sticky=W)

        self.savef = Button(self.frameDown ,text = "Save As...",command=self.save)
        self.savef.grid(pady=5,row=3,column=1,sticky=W)
        
        # menu 
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Open",accelerator = 'Ctrl+O',command = self.open)
        self.file_menu.add_command(label = "Convert",accelerator = 'Ctrl+T',command = self.conv)
        self.file_menu.add_command(label = "Save",accelerator = 'Ctrl+S',command = self.save)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu ( self.menu,tearoff = 0)
        self.edit_menu.add_command(label = "Clear text field",accelerator = 'Alt + S',command = self.cleart)
        self.menu.add_cascade(label = "Edit" , menu  = self.edit_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Alt-s>',lambda event: self.cleart())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-s>',lambda event:self.save())
        self.master.bind('<Control-o>',lambda event:self.open())
        self.master.bind('<Control-t>',lambda event:self.conv())

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
            if self.varfrom.get() == "Lbs -> Kg":
                for i in self.lines:
                    value = i*0.45359237
                    self.textname2.insert('end',value)
                    self.textname2.insert('end',"\n")
            elif self.varfrom.get() == "Kg -> Lbs":
                for i in self.lines:
                    value = i*2.20462
                    self.textname2.insert('end',value)
                    self.textname2.insert('end',"\n")
                    
    def open(self):
        formats = [("Csv files", "*.csv"),("Text files", "*.txt"),("all files", "*.*")]
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=formats)
        try:
            with open(filename) as f:
                thereader = csv.reader(f)
                for row in thereader:
                    try:
                        row = float(row[0])
                        self.textname.insert('end',row)
                        self.textname.insert('end',"\n")
                    except: pass
        except: pass
        
    def cleart(self):
        """ clears text field """
        self.textname.delete(1.0,END)
        
    def save(self):
        file_name = filedialog.asksaveasfilename(title="Save as...",defaultextension='.csv')
        with open(file_name,'a+') as f:
            for i in self.lines:
                f.write(str(i)+'\n')
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help","Input data by File-Open or keyboard. \nSpaces and commas indicate other number value.\nNumber point number for decimals (half Kg=0.5). \nAlphabetical characters aren't supported!")
    
    def aboutmenu(self):
        msg.showinfo("About","About Weight Converter \nVersion 1.1")
        
def main():
    root = Tk()
    functionality(root)
    root.mainloop()

if __name__=='__main__':
    main()
