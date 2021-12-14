import tkinter as tk
from page import Page
from tkinter import filedialog, Text
import os
from tkinter.constants import X
# from PIL import Image, ImageTk

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import numpy as np

import pandas as pd
from pandas import DataFrame
from page import Page

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#555555")
        TableLabel = tk.Label(self, text="TABLE SCRAPER")
        TableLabel.place(width=145, height=20, relx=0.45, rely=.025)

        L4b = tk.Label(self, text="")
        L4b.place(relwidth=.75, height=20, relx=.15, rely=.6)
        L4b.config(text='leaving folder directory empty will save to the current directory')

        #TABLE SCRAPER BELOW ---------------------------------------------

        L5 = tk.Label(self, borderwidth=2, relief='sunken', text="enter name for datatable")
        L5.place(width=180, height=20, relx=0.05, rely=.15)
        E5 = tk.Entry(self, bd =2)
        E5.place (relwidth=0.45, height=20, relx=0.36, rely=.15)

        L6 = tk.Label(self, borderwidth=2, relief='sunken', text="enter wikipedia url here")
        L6.place(width=180, height=20, relx=0.05, rely=.25)
        E6 = tk.Entry(self, bd =2)
        E6.place (relwidth=0.45, height=20, relx=0.36, rely=.25)

        L7 = tk.Label(self, borderwidth=2, relief='sunken', text="folder directory (optional)")
        L7.place(width=180, height=20, relx=0.05, rely=.35)
        E7 = tk.Entry(self, bd =2)
        E7.place (relwidth=0.45, height=20, relx=0.36, rely=.35)

        var = tk.IntVar()
        R1 = tk.Radiobutton(self, text="CSV", variable=var, value=0)
        R1.place(relx=0.38, rely=.45)

        R2 = tk.Radiobutton(self, text="JSON", variable=var, value=1)
        R2.place(relx=0.52, rely=.45)

        R3 = tk.Radiobutton(self, text="HTML", variable=var, value=2)
        R3.place(relx=0.68, rely=.45)

        TableScrape = tk.Button(self, text="E\nN\nT\nE\nR",padx=10, pady=5, command=lambda:[input_table_scrape()])
        TableScrape.place(relwidth=0.04, relheight=0.36, relx=0.9, rely=.15)

        TableScrapeClr = tk.Button(self, text="C\nL\nE\nA\nR",padx=10, pady=5, command=lambda:[clr_table_scrape()])
        TableScrapeClr.place(relwidth=0.04, relheight=0.36, relx=0.85, rely=.15)

        def input_table_scrape():
            name = E5.get()
            url = E6.get()
            if(E7.get() != ''):
                os.chdir(E7.get())     

            if(name or url == ''):
                L4b.config(text="you haven't input any data")    


            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, 'lxml')

            ctr_table = soup.findAll('table', class_='wikitable', limit= 3)
            dflist = pd.read_html(str(ctr_table))
            df = pd.DataFrame(dflist[0])
            #print(df.head(10))
            if(var.get() == 0):
                df.to_csv(f'{name}.csv')
            if(var.get() == 1):
                df.to_json(f'{name}.json', orient="split")
            if(var.get() == 2):
                df.to_html(f'{name}.html')

            L4b.config(text='saved table at ' + os.sep.join(os.path.normpath(os.getcwd()).split(os.sep)[-3:]))


        def clr_table_scrape():
            E5.delete(0, 'end')
            E6.delete(0, 'end')
            E7.delete(0, 'end')
