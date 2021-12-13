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

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        ImgLabel = tk.Label(self, text="IMAGE SCRAPER")
        ImgLabel.place(width=145, height=20, relx=0.45, rely=.025)

        L1 = tk.Label(self, borderwidth=2, relief='sunken', text="enter name for local folder")
        L1.place(width=200, height=20, relx=0.05, rely=.1)
        E1 = tk.Entry(self, bd =2)
        E1.place (relwidth=0.45, height=20, relx=0.36, rely=.1)


        L2 = tk.Label(self, borderwidth=2, relief='sunken', text="enter wikipedia url here")
        L2.place(width=200, height=20, relx=0.05, rely=.2)
        E2 = tk.Entry(self, bd =2)
        E2.place (relwidth=0.45, height=20, relx=0.36, rely=.2)



        L3 = tk.Label(self, borderwidth=2, relief='sunken', text="how many images you want")
        L3.place(width=200, height=20, relx=0.05, rely=.3)
        E3 = tk.Entry(self, bd =2)
        E3.place (relwidth=0.45, height=20, relx=0.36, rely=.3)

        L4 = tk.Label(self, borderwidth=2, relief='sunken', text="folder directory (optional)")
        L4.place(width=200, height=20, relx=0.05, rely=.4)
        E4 = tk.Entry(self, bd =2)
        E4.place (relwidth=0.45, height=20, relx=0.36, rely=.4)

        L4b = tk.Label(self, text="")
        L4b.place(relwidth=.75, height=20, relx=.15, rely=.55)
        L4b.config(text='leaving folder directory empty will save to the current directory')

        ImgScrape = tk.Button(self, text="E\nN\nT\nE\nR",padx=10, pady=5, command=lambda:[input_img_scrape()])
        ImgScrape.place(relwidth=0.04, relheight=0.36, relx=0.9, rely=.1)

        ImgScrapeClr = tk.Button(self, text="C\nL\nE\nA\nR",padx=10, pady=5, command=lambda:[clr_img_scrape()])
        ImgScrapeClr.place(relwidth=0.04, relheight=0.36, relx=0.85, rely=.1)

       
        def input_img_scrape():

            test_path = E1.get()
            url = E2.get()
            n_images = int(E3.get())
            if(E4.get() != ''):
                os.chdir(E4.get())  

            try:
                os.mkdir(test_path)

            except OSError:
                current_path = os.getcwd() + '\\' + test_path
            else:
                print ("successfully created the directory %s " % test_path)
                current_path = os.getcwd()

            html_content = requests.get(url, allow_redirects=True).text
            soup = BeautifulSoup(html_content, 'lxml')

            bs4 = soup.findAll('img', limit=n_images)

            def formaturl(url):
                if not re.match('(?:http|ftp|https):', url):
                    return 'http:{}'.format(url)
                return url

            urlArr = []

            def removing_characters(str):
                regex = "[a-z, \s, ()]"
                return (re.sub(regex, "", str))

            for tag in bs4:
                url = tag['src']
                name = tag['alt']
                newurl = formaturl(url)
                urlArr.append(newurl)


            def urlarray(urlx):
                for i, urlx in enumerate(urlArr):
                    save_name = os.path.join(test_path, f'{test_path}_{i}.jpg')
                    urllib.request.urlretrieve(urlx, save_name)
                return urlx
            
            L4b.config(text='saved images at ' + os.sep.join(os.path.normpath(current_path).split(os.sep)[-3:]))

            urlarray(urlArr)

        def clr_img_scrape():
            E1.delete(0, 'end')
            E2.delete(0, 'end')
            E3.delete(0, 'end')

        def handle_click(event):
            print("clicked!")

            E2.bind("<1>", handle_click)