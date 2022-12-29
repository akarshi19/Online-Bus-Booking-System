from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=12)
Label(root,text='Add New Details to Database',font='Arial 18',fg='Green3').grid(row=2,columnspan=12,pady=20)
def new_op():
    root.destroy()
    import new_operator

def new_b():
    root.destroy()
    import new_bus

def new_route():
    root.destroy()
    import bus_route

def new_r():
    root.destroy()
    import new_run

Button(root,text='New Operator',font='Arial 12',bg='Pale Green',command=new_op).grid(row=3,column=4)
Button(root,text='New Bus',font='Arial 12',bg='OrangeRed2',command=new_b).grid(row=3,column=5)
Button(root,text='New Route',font='Arial 12',bg='Steel Blue',command=new_route).grid(row=3,column=6)
Button(root,text='New Run',font='Arial 12',bg='Rosy Brown',command=new_r).grid(row=3,column=7)

root.mainloop()
