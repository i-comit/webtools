import tkinter as tk
from page import Page
from selenium import webdriver
import platform

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="PAGE PINGER")
        label.place(relx=0.15, rely=0.05)
        listbox = tk.Listbox(self, width="43", height="12")
        listbox.place(relx=0.43, rely=0.05)
        btn1 = tk.Button(self,bg='red', fg='white', text="QUERY WEBSITE", pady=0, borderwidth=3, relief="ridge", command=lambda:[queryWebsite()])
        btn1.place(relx=0.12, rely=0.3)
        titlefinderarr = []
        imgfinderarr = []
        imgcheckerarr = []
        start_letter = 'P'

        def queryWebsite():

            PATH = ""
            print(platform.system())
            if(platform.system() == "Windows"):
                PATH = "./chromedriver.exe"
            if(platform.system() == "Linux"):
                PATH = "./chromedriver"
            print(PATH)
            driver = webdriver.Chrome(PATH)
            for page in range(1, 4, 1):
                driver.get("https://www.fishersci.com/us/en/catalog/search/products?keyword=pluriselect&page=" + str(page))
            #     finder = driver.find_element_by_class_name("search_result_item")
            #     print(finder.text)

                titlefinder = driver.find_elements_by_class_name("result_title")
                imgfinder = driver.find_elements_by_class_name("search_image_thumb")


                for img in imgfinder:
                    # imgfinderarr.append(img.get_attribute('src'))
                    # if(img.get_attribute('src') != 'https://assets.fishersci.com/TFS-Assets/CCG/product-images/default.jpg-250.jpg'):
                    imgfinderarr.append(img.get_attribute('src'))


                for title in titlefinder:
                    titlefinderarr.append(title.text)
                    imgcheck = str(title.text)

            for string in imgfinderarr:
                new_string = string.replace("https://assets.fishersci.com/TFS-Assets/CCG/product-images/default.jpg-250.jpg", " - NO IMG")
                imgcheckerarr.append(new_string)

            i=0
            while i < len(imgcheckerarr):
                if 'product-images' in imgcheckerarr[i]:
                    imgcheckerarr[i] = ''
                i+=1

            zippedarr = [i + j for i, j in zip(titlefinderarr, imgcheckerarr,)]
            with_p = [x for x in zippedarr if x.startswith(start_letter)]

            listitem= 0
            while listitem < len(with_p):
                listbox.insert(listitem, with_p[listitem])
                listitem += 1



