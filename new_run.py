from tkinter import *
from tkinter.messagebox import*
import sqlite3
root2=Tk()
h,w=root2.winfo_screenheight(),root2.winfo_screenwidth()
root2.geometry('%dx%d+0+0'%(w,h))

bus2=PhotoImage(file='.\\Bus_for_project.png')
Label(root2,image=bus2).grid(row=0,column=0,columnspan=16,padx=w/2.5)

Label(root2,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=16)
Label(root2,text='Add Bus Running Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=16,pady=20)

Label(root2, text="Bus ID", font='Arial 12', fg='black').grid(row=3, column=4)
bus_id=Entry(root2)
bus_id.grid(row=3, column=5)

Label(root2, text="Running Date", font='Arial 12', fg='black').grid(row=3, column=6)
running_date=Entry(root2)
running_date.grid(row=3, column=7)
    #Label(root2,text="date format YYYY-MM-DD").grid(row=4,column=3)

Label(root2, text="Seat Available", font='Arial 12', fg='black').grid(row=3, column=8)
seat_avail=Entry(root2)
seat_avail.grid(row=3, column=9)
def add_run():
    bid=bus_id.get()
    run_date=running_date.get()
    s_avail=seat_avail.get()
    con2=sqlite3.Connection('Bus_DB')
    cur2=con2.cursor()
    cur2.execute('create table if not exists running(b_id varchar(5) ,run_date date,seat_avail int,foreign key(b_id) references bus(bus_id))')
    cur2.execute('insert into running(b_id,run_date,seat_avail) values (?,?,?)',(bid,run_date,s_avail))
    con2.commit()
    showinfo('sucess','run added successfully!!')    

Button(root2, text="Add Run", font='Arial 12 bold', bg='green2', fg='black',command=add_run).grid(row=3, column=10)
Button(root2, text="Delete Run", font='Arial 12 bold', bg='green2', fg='black').grid(row=3, column=11)

def ho2():
    root2.destroy()
    import Home
    
home2=PhotoImage(file='.\\home.png')
Button(root2,image=home2,bg='Pale Green',command=ho2).grid(row=4,column=10,pady=50)
root2.mainloop()


































