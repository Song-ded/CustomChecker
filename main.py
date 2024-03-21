import customtkinter as CTk
import wmi
import math
import os
from datetime import datetime, timedelta
import socket
from pathlib import Path
import requests
import subprocess
import json


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
raw_time = os_info.LastBootUpTime

year = int(raw_time[0:4])
month = int(raw_time[4:6])
day = int(raw_time[6:8])
hour = int(raw_time[8:10])
minute = int(raw_time[10:12])
second = int(raw_time[12:14])

offset_hours = int(raw_time[15:18])
offset_minutes = int(raw_time[18:20])
offset = timedelta(hours=offset_hours, minutes=offset_minutes)

utc_time = datetime(year, month, day, hour, minute, second) - offset

resp = requests.get('https://pastebin.com/raw/5JRvQiZ4')

#os.startfile(r"_internal\x64\folders.exe")

class App(CTk.CTk):
    def __init__(self):

        with open(r'_internal\x64\text.txt', 'r', encoding='utf-8') as file:

            info_text = file.read()
        
        super().__init__()
        


        
        self.title("Custom Checker by NВАЛ")
        self.geometry("850x650")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        CTk.set_default_color_theme("dark-blue")

        


        self.frameone = CTk.CTkFrame(master=self) #правая часть
        self.frameone.grid(row=0, column=0, padx=0, pady=0, sticky = "ne")#правая часть

        self.frametwo = CTk.CTkFrame(master=self)#левая часть
        self.frametwo.grid(row=0, column=0, padx=0, pady=0, sticky = "nw")#левая часть

        self.framethree = CTk.CTkFrame(master=self) #правая часть
        self.framethree.grid(row=0, column=0, padx=0, pady=0, sticky = "se")#правая часть

        self.framefour = CTk.CTkFrame(master=self) #правая часть
        self.framefour.grid(row=0, column=0, padx=0, pady=0, sticky = "sw")#правая часть
        
        
       

#правая часть
        self.label = CTk.CTkLabel(master=self.frameone, text=info_text)
        self.label.grid(row=0, column=0,padx=35,pady=15, sticky='s')
        
      #  self.labelempty = CTk.CTkLabel(master=self.frameone, text ='')  # Оттягивает в низ лебел (пустое место, если убрать то оно будет по тексту)
       # self.labelempty.grid(row=1, column=0,padx=0,pady=90, sticky='s')
#левая часть
        self.label2 = CTk.CTkLabel(master=self.frametwo, text = "Session start time: {0}".format(utc_time.strftime("%Y-%m-%d %H:%M:%S")))
        self.label2.grid(row=1, column=0,padx=35,pady=5, sticky='s')
        
        self.label3 = CTk.CTkLabel(master=self.frametwo, text = 'OS Name: {0}'.format(os_name.decode('utf-8')))
        self.label3.grid(row=2, column=0,padx=35,pady=5, sticky='s')

        self.label4 = CTk.CTkLabel(master=self.frametwo, text = 'OS Version: {0}'.format(os_version))
        self.label4.grid(row=3, column=0,padx=35,pady=5, sticky='s')

        self.label5 = CTk.CTkLabel(master=self.frametwo, text = "IP address: {0}".format(get_local_ip()))
        self.label5.grid(row=4, column=0,padx=35,pady=5, sticky='s')

        self.label6 = CTk.CTkLabel(master=self.frametwo, text = 'RAM: {0} GB'.format(math.ceil(system_ram)))
        self.label6.grid(row=5, column=0,padx=35,pady=5, sticky='s')

        self.label7 = CTk.CTkLabel(master=self.frametwo, text = 'CPU: {0}'.format(proc_info.Name))
        self.label7.grid(row=6, column=0,padx=35,pady=5, sticky='s')

        self.label8 = CTk.CTkLabel(master=self.frametwo, text = 'Graphics Card: {0}'.format(gpu_info.Name))
        self.label8.grid(row=7, column=0,padx=35,pady=5, sticky='s')
       


#правая нижняя часть       
        
        
        self.button = CTk.CTkButton(master=self.framethree, text="LastActivityView",command=lambda: self.button_callback("x"))
        self.button.grid(row=3, column=1, padx=35, pady=15, sticky = "n")
        self.button = CTk.CTkButton(master=self.framethree, text="ProcessHacker",command=lambda: self.button_callback("xx"))
        self.button.grid(row=5, column=1, padx=35, pady=15, sticky = "n")
        self.button = CTk.CTkButton(master=self.framethree, text="Everything",command=lambda: self.button_callback("xxx"))
        self.button.grid(row=4, column=1, padx=35, pady=15, sticky = "n")




#левая нижняя часть   
        self.button = CTk.CTkButton(master=self.framefour, text="AppData",command=lambda: self.button_callback("yy"))
        self.button.grid(row=2, column=1, padx=35, pady=15, sticky = "n")
        self.button = CTk.CTkButton(master=self.framefour, text="Recent",command=lambda: self.button_callback("yyy"))
        self.button.grid(row=3, column=1, padx=35, pady=15, sticky = "n")
        self.button = CTk.CTkButton(master=self.framefour, text="Prefetch",command=lambda: self.button_callback("yyyy"))
        self.button.grid(row=4, column=1, padx=35, pady=15, sticky = "n")
        self.button = CTk.CTkButton(master=self.framefour, text="Program Files",command=lambda: self.button_callback("yyyyy"))
        self.button.grid(row=5, column=1, padx=35, pady=15, sticky = "n")

        
     
        
        
 
 
    def button_callback(self, farg):
        if farg == 'yyyyy':
            os.system(r"explorer.exe C:\Program Files")
        elif farg == 'yy':
            os.system("explorer.exe " + os.getenv('APPDATA'))
        elif farg == 'yyy':
            os.system("explorer.exe " + str(Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Recent"))
        elif farg == 'yyyy':
            os.system(r"explorer.exe C:\Windows\Prefetch")

        if farg == 'x':
            os.startfile(r"_internal\Last\LastActivityView.exe")
        elif farg == "xx":
            os.startfile(r"_internal\x64\ProcessHacker.exe")
        elif farg == "xxx":
            os.startfile(r"_internal\Evry\Everything.exe")
        print(farg)

    

app = App()
app.mainloop()
