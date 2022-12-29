from tkinter import*
from tkinter.messagebox import*
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,columnspan=10,padx=w//2.5)
Label(root,text='Online Bus Booking System',font='Arial 30',fg='Red',bg='Sky Blue').grid(row=1,columnspan=10)
Label(root,text='').grid(row=2,columnspan=10,pady=20)
Label(root,text='Name : Akarshi Mathur',font='Calibri 20 bold',fg='Medium Blue').grid(row=3,columnspan=10)
Label(root,text='').grid(row=4,columnspan=10,pady=10)
Label(root,text='Er. No. : 211B029',font='Calibri 20 bold',fg='Medium Blue').grid(row=5,columnspan=10)
Label(root,text='').grid(row=6,columnspan=10,pady=10)
Label(root,text='Jaypee University of Engineering And Technology',font='Calibri 20 bold',fg='Medium Blue').grid(row=7,columnspan=10)
Label(root,text='A-B Road, Raghogarh, Distt. - Guna (M.P.), PIN - 473226, INDIA',font='Calibri 20 bold',fg='Medium Blue').grid(row=9,columnspan=10)
Label(root,text='Project Based Learning',font='Arial 15',fg='Red').grid(row=10,columnspan=10)

def close():
    root.destroy()
    import Home
root.after(5000,close)
root.mainloop()
