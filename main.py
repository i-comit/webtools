import tkinter as tk
from pagequeri import Page1
from autoping import Page2
from imgscraper import Page3
from about import Page4

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", pady='10', padx='10',expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="WEBPAGE QUERY", command=p1.lift)
        b2 = tk.Button(buttonframe, text="WEBPAGE PINGER", command=p2.lift)
        b3 = tk.Button(buttonframe, text="IMAGE SCRAPER", command=p3.lift)
        b4 = tk.Button(buttonframe, text="ABOUT", command=p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.wm_title("GLUONG WEB QUERY PY-TOOLS")
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("650x350")
    root.wm_minsize(width=600, height=350)
    root.wm_maxsize(width=700, height=350)
    root.mainloop()