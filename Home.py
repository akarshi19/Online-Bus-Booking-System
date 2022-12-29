from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,columnspan=10,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,columnspan=10)
Label(root,text='').grid(row=2,columnspan=10,pady=40)
def seat_book():
    root.destroy()
    import seat_booking

def checkbooked():
    root.destroy()
    import check_booking

def adddetails():
    root.destroy()
    import bus_detail

Button(root,text='Seat Booking',font='Arial 20',bg='Pale Green',command=seat_book).grid(row=3,column=1,padx=80)
Button(root,text='Check Booked Seat',font='Arial 20',bg='Green2',command=checkbooked).grid(row=3,column=2,padx=80)
Button(root,text='Add Bus detail',font='Arial 20',bg='Dark Green',command=adddetails).grid(row=3,column=3,padx=80,pady=20)

Label(root,text='For Admin Only',font='Arial 15',fg='Red').grid(row=4,column=3)

















root.mainloop()
