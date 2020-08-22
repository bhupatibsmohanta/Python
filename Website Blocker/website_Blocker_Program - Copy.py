from selenium import webdriver
from tkinter import *
import numpy as np
from datetime import datetime as dt 

start=8
end=19

root= Tk()
root.title("Edulyt Browser")
enter = Entry(root, width=50, borderwidth=5)
enter.pack()

def myClick():
    filename= 'C:/Users/Bhupati/Pictures/Website Blocker/Blockedsite_DB.txt'
    blocked=np.loadtxt(filename,delimiter='\n',dtype=str)
    site=enter.get()
    
    status=None
    
    if(site in blocked and dt(dt.now().year, dt.now().month, dt.now().day,start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end)):
        print(site +" is blocked by Edulyt")
        messagebox.showwarning("Error",site+" is Bloked by Edulyt. It's Working Hours. Get Back to Work")
        status="Blocked"
    else:
        driver=webdriver.Chrome()
        driver.get("https://www."+site)
        status="Accessed"
    
    msg=status+", "+site+", "+ str(dt.now())+"\n"
    print(msg)

myButton = Button(root,text="Search",command=myClick)
myButton.pack()

root.mainloop()
