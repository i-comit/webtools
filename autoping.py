import tkinter as tk
from page import Page
import subprocess as sp
import csv
import time 
import threading
from datetime import datetime
import requests
import pygame

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def getUrl():
            urls=[]
            name = str(e1.get().strip())
            interval = int(dropdownoptions[dropdownlist.get()])
            print(interval)
            csvthread= threading.Thread(target=logCSV, args=(1,))
            now = datetime.now()
            titletime= datetime.date(now).strftime("%Y%m%d") 
            with open(f'{name}-PingTest{titletime}.csv', 'w', newline="") as outcsv:
                        writer = csv.writer(outcsv)
                        writer.writerow(["Time", "Packet Sent", "Packet Received", "Packet Loss", "Status"])
            csvthread.daemon = True
            csvthread.start()
            urls.append(name)

            # listvar.set(urls)
            for url in urls:
                Lb1.insert(0, url)    

        def logCSV(name):
            name = str(e1.get().strip())
            response = requests.get('https://' + f'{name}')
            status_code = int(response.status_code)

            interval = int(dropdownoptions[dropdownlist.get()])
            namecache = name
            intervalcache = interval
            now = datetime.now()
            titletime= datetime.date(now).strftime("%Y%m%d")
            
            starttime=time.time() 
            e1.delete(0, "end")
            # e2.delete(0, "end")
            while(True):       
                output = sp.getoutput(f'ping -n 3 {namecache} | find "Packets"')
                # print (output)
                packetsent = output[20:21]
                packetreceived = output[34:35]
                packetloss = output[44:45]
                print(status_code)

                if(packetsent == packetreceived):
                    status= "UP"
                if(packetsent == packetloss):
                    status="DOWN"
                    pygame.mixer.init()
                    pygame.mixer.music.load("alarm16bit.wav")
                    pygame.mixer.music.play()
                if(status_code == int(503)):
                    status="503"
                    pygame.mixer.init()
                    pygame.mixer.music.load("alarm16bit.wav")
                    pygame.mixer.music.play()
                if(packetsent != packetreceived):
                    status="ERROR"

                with open(f'{namecache}-PingTest{titletime}.csv', 'a', newline="") as f:
                    writef = csv.writer(f)
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)

                    writef.writerow([current_time] + [packetsent] + [packetreceived] + [packetloss] + [status])

                    time.sleep(intervalcache - ((time.time() - starttime) % intervalcache))

        # lbl5=tk.Label(self, text="MULTITHREADED PAGE PINGER", fg='red', font=("Helvetica", 14))
        # lbl5.pack(side="top", ipady=30)
        l1= tk.Label(self, text="Enter Website URL Here \n\n\nEnter Time Interval Here",  fg='black', font=("Verdana", 9))
        l1.pack(ipadx=0, padx=10, ipady=4, pady=3, side='left', anchor='ne')
        # lbl1 = tk.Label(self, text="helo world", fg='black', font=("Verdana", 9))
        # lbl1.place(x= 150, y=190, width=300, height=30)
        e1=tk.Entry(self, bd=5, width=18)
        e1.pack(ipadx=30, padx=20, ipady=4, pady=3, side='top', anchor='nw')

        dropdownlist = tk.StringVar(self)
        dropdownoptions = {
            'Every 5 Seconds': 5,
            'Every 15 Seconds': 15, 
            'Every 30 Seconds': 30,
            'Every Minute': 60,
            'Every 5 Minutes' : 300,
            'Every 15 Minutes' : 900,
            'Every 30 Minutes' : 1800,
            'Every Hour' : 3600,
        }

        dropdownlist.set('Every 5 Seconds') # set the default option

        dropdown = tk.OptionMenu(self, dropdownlist, *dropdownoptions)
        dropdown.pack(ipadx=30, padx=20, ipady=4, pady=3, side='top', anchor='nw')

        # e2=Entry(window, bd=5)
        # e2.pack(ipadx=30, padx=20, ipady=4, pady=3, side=TOP, anchor=NW)

        Lb1 = tk.Listbox(self)
        Lb1.place(relx=0.67, rely=.05, relheight=0.8, relwidth=0.3)

        Start = tk.Button(self,bg='#3F3F3F', fg='white', text="START", pady=0, borderwidth=3, relief="ridge", command=lambda:[getUrl()])
        Start.place(relx=0.02, rely=0.70, relwidth=0.6, height=35)