import tkinter as tk
import script
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import *
import sys
import webbrowser
import os
import time
t=0.0
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def browse_button1():
    global source1
    filename = filedialog.askdirectory()
    source1.set(filename)
    print(filename)

def browse_button2():
    global source2
    filename = filedialog.askdirectory()
    source2.set(filename)
    print(filename)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkFont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("FSORTER")
        width=600
        height=500

        root =tk.Frame(self)
        root.pack(side="top", fill="both", expand=True)
        root.grid_rowconfigure(0, weight=600)
        root.grid_columnconfigure(0, weight=500)

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.frames = {}
        for F in (start,page1):
            page_name = F.__name__
            frame = F(parent=root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("start")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


class start(tk.Frame):
    def __init__(self, parent, controller):
        var = IntVar()
        var.set(0)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_1=tk.Label(self)
        label_1["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=10)
        label_1["font"] = 'Helvetica 14 bold'
        label_1["fg"] = "#333333"
        label_1["justify"] = "center"
        label_1["text"] = "Do you have Labelled Data"
        label_1.pack()
        label_1.place(x=30,y=50,width=211,height=60)



        label_2=tk.Label(self)
        label_2["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=10)
        label_2["font"] = 'Helvetica 14 bold'
        label_2["fg"] = "#333333"
        label_2["justify"] = "center"
        label_2["text"] = "Labelled Data Location"
        label_2.pack()
        label_2.place(x=30,y=180,width=211,height=60)

        label_3=tk.Label(self)
        label_3["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=10)
        label_3["font"] = 'Helvetica 14 bold'
        label_3["fg"] = "#333333"
        label_3["justify"] = "center"
        label_3["text"] = "Source Folder Location"
        label_3.pack()
        label_3.place(x=30,y=310,width=211,height=60)

        self.label_var = tk.StringVar()
        self.label_var2=tk.StringVar()

        def chooseen():
            global conditiong
            conditiong=True
            if var.get() !=0:
                choose["state"]=NORMAL
                next["state"]=NORMAL
                choose["state"]=NORMAL
                choose2["state"]=NORMAL

        def choosedis():
            global conditiong
            conditiong=True
            if var.get()!=0:
                choose["state"]=DISABLED
                next["state"]=NORMAL
                choose2["state"]=NORMAL

        R1=tk.Radiobutton(self)
        R1["anchor"] = "w"
        ft = tkFont.Font(family='Times',size=10)
        R1["font"] = 'Helvetica 12'
        R1["fg"] = "#333333"
        R1["justify"] = "left"
        R1["text"] = "Yes"
        R1["relief"] = "sunken"
        R1["value"] = 1
        R1["command"] = chooseen
        R1["variable"]= var
        R1.pack()
        R1.place(x=280,y=60,width=85,height=25)

        R2=tk.Radiobutton(self)
        R2["anchor"] = "w"
        ft = tkFont.Font(family='Times',size=10)
        R2["font"] = 'Helvetica 12'
        R2["fg"] = "#333333"
        R2["justify"] = "left"
        R2["text"] = "No"
        R2["value"] = 2
        R2["command"] = choosedis
        R2["variable"]= var
        R2.pack()
        R2.place(x=280,y=80,width=85,height=25)


        label_4=tk.Label(self)
        label_4["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=12)
        label_4["font"] = 'Helvetica 12'
        label_4["fg"] = "#333333"
        label_4["justify"] = "center"
        label_4["text"] = "Location"
        label_4["textvariable"]=self.label_var
        label_4.pack()
        label_4.place(x=280,y=220,width=211,height=20)




        choose=tk.Button(self)
        choose["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        choose["font"] = ft
        choose["fg"] = "#000000"
        choose["justify"] = "center"
        choose["text"] = "Choose"
        choose["command"] = self.choose
        choose.pack()
        choose["state"]=DISABLED
        choose.place(x=280,y=190,width=95,height=30)


        choose2=tk.Button(self)
        choose2["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        choose2["font"] = ft
        choose2["fg"] = "#000000"
        choose2["justify"] = "center"
        choose2["text"] = "Choose"
        choose2["command"] = self.choose2
        choose2["state"]=DISABLED
        choose2.pack()
        choose2.place(x=280,y=320,width=95,height=30)


        cancel=tk.Button(self)
        cancel["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        cancel["font"] = ft
        cancel["fg"] = "#000000"
        cancel["justify"] = "center"
        cancel["text"] = "Cancel"
        cancel["command"] = self.cancel
        cancel.pack()
        cancel.place(x=390,y=450,width=70,height=25)

        next=tk.Button(self)
        next["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        next["font"] = ft
        next["fg"] = "#000000"
        next["justify"] = "center"
        next["text"] = "Next"
        next["state"]=DISABLED
        next.pack()
        next["command"]=self.next
        next.place(x=500,y=450,width=70,height=25)

        
        help=tk.Button(self)
        help["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        help["font"] = ft
        help["fg"] = "#000000"
        help["justify"] = "center"
        help["text"] = "Help"
        help["command"] = self.help
        help.pack()
        help.place(x=30,y=450,width=70,height=25)

        label_p=tk.Label(self)
        label_p["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Helvetica 18 bold',size=10)
        label_p["font"] = 'Helvetica 18 bold'
        label_p["fg"] = "#333333"
        label_p["justify"] = "center"
        label_p["text"] = "Code written with ❤️ by Pranav Aggarwal"
        label_p.pack()
        label_p.place(x=0,y=475,width=600,height=25)


        self.label_var2.set("Location")
        self.label_var.set("Location")


        label_5=tk.Label(self)
        label_5["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=12)
        label_5["font"] = 'Helvetica 12'
        label_5["fg"] = "#333333"
        label_5["justify"] = "center"
        label_5["text"] = "Location"
        label_5["textvariable"]=self.label_var2
        label_5.pack()
        label_5.place(x=280,y=350,width=211,height=20)

    def choose2(self):
        browse_button2()
        self.label_var2.set(source2.get())
    
    def choose(self):
        browse_button1()
        self.label_var.set(source1.get())

    def cancel(self):
        sys.exit(1)

    def next(self):
        global t
        st=time.time()
        self.controller.show_frame("page1")
        global conditiong
        script.swag(source2.get(), source1.get(),conditiong)
        et=time.time()
        t=st-et
        print(et-st)

    def help(self):
        webbrowser.open("https://github.com/Pranav0-0Aggarwal/FSorter/blob/main/README.md")
    
    def r1(self):
        condition=TRUE
    
    def r2(self):
        condition=FALSE

class page1(tk.Frame):
    def __init__(self, parent, controller):
        self.label_vari = tk.StringVar()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        messagebox=tk.Message(self)
        messagebox["bg"] = "#fffdfd"
        ft = tkFont.Font(family='Times',size=10)
        messagebox["font"] = ft
        messagebox["fg"] = "#333333"
        messagebox["justify"] = "center"
        messagebox["text"] ="Task Succesfully completed"
        messagebox.pack() 
        messagebox.place(x=40,y=180,width=510,height=235)

        cancel=tk.Button(self)
        cancel["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        cancel["font"] = ft
        cancel["fg"] = "#000000"
        cancel["justify"] = "center"
        cancel["text"] = "Cancel"
        cancel["command"] = self.cancel
        cancel.pack() 
        cancel.place(x=390,y=450,width=70,height=25)

        Previous=tk.Button(self)
        Previous["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        Previous["font"] = ft
        Previous["fg"] = "#000000"
        Previous["justify"] = "center"
        Previous["text"] = "Previous"
        Previous["command"] = self.previous
        Previous.pack()
        Previous.place(x=500,y=450,width=70,height=25)

        label_p=tk.Label(self)
        label_p["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Helvetica 18 bold',size=10)
        label_p["font"] = 'Helvetica 18 bold'
        label_p["fg"] = "#333333"
        label_p["justify"] = "center"
        label_p["text"] = "Code written with ❤️ by Pranav Aggarwal"
        label_p.pack()
        label_p.place(x=0,y=475,width=600,height=25)

    def cancel(self):
        sys.exit(1)


    def previous(self):
        restart_program()

if __name__ == "__main__":
    app = App()
    width=600
    height=500
    screenwidth = app.winfo_screenwidth()
    screenheight = app.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    app.geometry(alignstr)
    source1 = StringVar()
    source2= StringVar()
    sourcea=f"{source1.get()}"
    sourceb=f"{source2.get()}"
    conditiong = True
    app.mainloop()
