import tkinter as tk
# from PIL import Image,  ImageTk
from page import Page

class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#555555")
        label0 = tk.Label(self, text="A simple desktop application for web search automation and web data extraction")
        label0.place(relx=0.05, rely=0.05)

        label = tk.Label(self, text="works on linux and windows")
        label.place(relx=0.05, rely=0.25)

        label1 = tk.Label(self, text="created by khiem g luong")
        label1.place(relx=0.05, rely=0.45)

        label2 = tk.Label(self, text="i-COMIT LLC")
        label2.place(relx=0.05, rely=0.65)

        label3 = tk.Label(self, text="i-comit.github.io")
        label3.place(relx=0.05, rely=0.85)

        # image1 = Image.open("icomiti.png")

        # test = ImageTk.PhotoImage(image1)

        # label1 = tk.Label(image=test)
        # label1.image = test

        # Position image