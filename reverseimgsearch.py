import tkinter as tk
from page import Page
from selenium import webdriver
import platform
from tkinter import filedialog
from PIL import ImageTk, Image 
import os
from selenium.webdriver.common.keys import Keys

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#555555")
        label = tk.Label(self, text="REVERSE IMAGE SEARCH")
        label.place(width=145, height=20, relx=0.4, rely=.025)
        # listbox = tk.Listbox(self, width="43", height="12")
        # listbox.place(relx=0.43, rely=0.05)
        btn1 = tk.Button(self,bg='#3F3F3F', fg='white', text="CHOOSE IMAGE", pady=0, borderwidth=3, relief="ridge", command=lambda:[chooseImg()])
        btn1.place(relx=0.025, rely=0.025, relwidth=0.28, height=35)
        btn2 = tk.Button(self,bg='#3F3F3F', fg='white',  text="RUN SEARCH", pady=0, borderwidth=3, relief="ridge", command=lambda:[queryWebsite()])

        def chooseImg():
            filetypes = (
            ('JPEG files', '*.jpg'),
            ('PNG files', '*.png*')
            )

            chooseImg.img = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/Pictures',
                filetypes=filetypes)

            img = Image.open(chooseImg.img)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            imgpanel =tk.Label(self, image = img, bd=1)
            imgpanel.image = img
            imgpanel.place(relx=0.7, rely=0.35)
            btn2.place(relx=0.7, rely=0.025, relwidth=0.28, height=35)

        def queryWebsite():
            PATH = ""
            print(platform.system())
            if(platform.system() == "Windows"):
                PATH = "./chromedriver.exe"
                print(os.getcwd())
            if(platform.system() == "Linux"):
                PATH = "./chromedriver"
            print(PATH)
            driver = webdriver.Chrome(PATH)

            # driver.get(chooseImg.img)
            # driver.get("http://www.google.hr/searchbyimage/upload")

            # elem = driver.find_element_by_name('q')
   
            # elem.send_keys(Keys.ENTER)

            # multipart = {'encoded_image': (chooseImg.img, open(chooseImg.img, 'rb')), 'image_content': ''}
            # response = requests.post("http://www.google.com/searchbyimage/upload", files=multipart, allow_redirects=False)
            # fetchUrl = response.headers['Location']
            # webbrowser.open(fetchUrl)

            driver.get('https://images.google.com/')

            # Find cam button
            cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
            cam_button.click()

            # Find upload tab
            upload_tab = driver.find_elements_by_xpath("//*[contains(text(), 'Upload an image')]")[0]
            upload_tab.click()

            # Find image input
            upload_btn = driver.find_element_by_name('encoded_image')
            upload_btn.send_keys(chooseImg.img)
