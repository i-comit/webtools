import tkinter as tk
# from PIL import Image,  ImageTk
from page import Page

class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#555555")
        label0 = tk.Label(self, text="a collection of web queries")
        label0.place(relx=0.1, rely=0.1)

        label = tk.Label(self, text="works on linux and windows")
        label.place(relx=0.1, rely=0.3)

        label1 = tk.Label(self, text="created by khiem g luong")
        label1.place(relx=0.1, rely=0.4)

        label2 = tk.Label(self, text="i-COMIT LLC")
        label2.place(relx=0.1, rely=0.6)

        label3 = tk.Label(self, text="i-comit.github.io")
        label3.place(relx=0.1, rely=0.8)

        # image1 = Image.open("icomiti.png")

        # test = ImageTk.PhotoImage(image1)

        # label1 = tk.Label(image=test)
        # label1.image = test

        # Position image
        label1.place(relx=0.6, rely=0.8)