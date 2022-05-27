# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:13:09 2022

@author: green
"""
import time
# from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

class Timer:
    def __init__(self, master):
        frm = ttk.Frame(master, padding=10)
        frm.grid()
        
        width = 4
        button_start = tk.Button(frm, width=width, text = "Start", bg = "green", command = self.start).grid(row = 2, column = 0)
        button_pause = tk.Button(frm, width=width,text = "Pause", bg = "yellow", command=self.pause).grid(row = 2, column = 1)
        button_stop = tk.Button(frm, width=width,text = "Stop", bg = "red", command=self.stop).grid(row = 2, column = 2)
        
        self.hour=tk.StringVar()
        self.minute=tk.StringVar()
        self.second=tk.StringVar()
        
        self.setInitialValues()
        
        row = 0
        ttk.Label(frm, text="H").grid(column=0, row=row)
        ttk.Label(frm, text="M").grid(column=1, row=row)
        ttk.Label(frm, text="S").grid(column=2, row=row)
        row = 1
        self.hourEntry= tk.Entry(frm, insertontime=0, width=3, font=("Arial",18,""),textvariable=self.hour).grid(column=0, row=row)
        self.minuteEntry= tk.Entry(frm, insertontime=0, width=3, font=("Arial",18,""),textvariable=self.minute).grid(column=1, row=row)
        self.secondEntry= tk.Entry(frm, insertontime=0, width=3, font=("Arial",18,""),textvariable=self.second).grid(column=2, row=row)      
        self.timeRemaining = -1

    def setInitialValues(self):
        self.stopTimer = True
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        
    def update(self):
        mins, secs = divmod(self.timeRemaining,60)
        hours = 0
        if mins >60:
             hours, mins = divmod(mins, 60)

        self.hour.set("{0:2d}".format(hours))
        self.minute.set("{0:2d}".format(mins))
        self.second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)
        
        if (self.timeRemaining == 0):
             messagebox.showinfo("Time Countdown", "Time's up ")
        else:
            if not self.stopTimer:
                self.timeRemaining -= 1
                self.update()
        
    def start(self):
        try:
           self.timeRemaining = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
           self.stopTimer = False
        except:
           self.setInitialValues()
           return
       
        self.update()

    def pause(self):
        self.stopTimer = True
        
    def stop(self):
        self.setInitialValues()
        
def position_window(width=300, height=200, xf = 0.5, yf = 0.5):
    
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width*xf) - (width/2)
    y = (screen_height*yf) - (height/2)

    if x > screen_width-width:
        x  = screen_width-width
    if x < width:
        x = 0.0
    if y > screen_height-height:
        y  = screen_height-height*1.25
    if y < 0:
        y = 0
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = tk.Tk()
root.attributes('-topmost', True)
root.attributes('-alpha',1.0)
position_window(150,100,.9,0)

app = Timer(root)

root.mainloop()