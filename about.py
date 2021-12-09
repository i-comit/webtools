import tkinter as tk
from page import Page

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="Created by Khiem G Luong")
        label.place(relx=0.1, rely=0.5)
 