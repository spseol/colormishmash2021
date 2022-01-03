#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Canvas, Scale, HORIZONTAL, LEFT, Frame, Entry, S, END, StringVar, IntVar

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)  # klávesa Esc spustí funkci quit()
        
        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()
        ### R
        self.varR = IntVar()
        self.lblR = tk.Label(self.frameR, text="R:")
        self.lblR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(
            self.frameR, from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varR 
        )
        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=4, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)
        ### G
        self.varG = StringVar()
        self.lblG = tk.Label(self.frameG, text="G:")
        self.lblG.pack(side=LEFT, anchor=S)
        self.scaleG = Scale(
            self.frameG,from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varG,
        )
        self.scaleG.pack(side=LEFT, anchor=S)
        self.entryG = Entry(self.frameG, width=4, textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)
        ### B
        self.varB = StringVar()
        self.lblB = tk.Label(self.frameB, text="B:")
        self.lblB.pack(side=LEFT, anchor=S)
        self.scaleB = Scale(
            self.frameB, from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varB
        )
        self.scaleB.pack(side=LEFT, anchor=S)
        self.entryB = Entry(self.frameB, width=4, textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)

        self.canvasMain = Canvas(self, width=300, height=200, background="#000000")
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>", self.clickHandler)
        self.entryMain = Entry(self,)
        self.entryMain.pack()

        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()

        self.btn2 = tk.Button(self, text="Change", command=self.change)
        self.btn2.pack()

        self.varR.trace('w', self.change)
        self.varG.trace('w', self.change)
        self.varB.trace('w', self.change)

        self.frameMem = Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        for row in range(3):
            for column in range(7):
                canvas = Canvas(self.frameMem, width=50, height=50, background="#abcdef")
                canvas.grid(row=row, column=column)
                canvas.bind("<Button-1>", self.clickHandler)
                self.canvasMem.append(canvas)

    def clickHandler(self, event):
        print(dir(event))
        if self.cget('cursor')!= 'pencil':
            self.config(cursor='pencil')
            self.color = event.widget.cget('background')
        elif self.cget('cursor') == 'pencil':
            self.config(cursor='')
            event.widget.config(background=self.color)
        if event.widget is self.canvasMain:
            self.varR.set(55)
            self.varG.set(128)

    def change(self, var=None, index=None, mode=None):
        #print(var, index, mode)
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorcode = f"#{r:02x}{g:02x}{b:02x}"
        self.canvasMain.config(background=colorcode)
        self.entryMain.delete(0, END)
        self.entryMain.insert(0, colorcode)


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
