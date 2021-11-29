#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Canvas, Scale, HORIZONTAL

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColoMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)  # klávesa Esc spustí funkci quit()

        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(
            self, from_=0, to=255, orient=HORIZONTAL, length=256, command=self.change
        )
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=256)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=256)
        self.scaleB.pack()

        self.canvasMain = Canvas(self, width=256, height=100, background="#000000")
        self.canvasMain.pack()

        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()

        self.btn2 = tk.Button(self, text="Change", command=self.change)
        self.btn2.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
