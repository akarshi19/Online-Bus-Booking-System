from tkinter import *
from tkinter.messagebox import*
import sqlite3

root4=Tk()
h,w=root4.winfo_screenheight(),root4.winfo_screenwidth()
root4.geometry('%dx%d+0+0'%(w,h))

bus4=PhotoImage(file='.\\Bus_for_project.png')
Label(root4,image=bus4).grid(row=0,column=0,columnspan=12,padx=w/2.5)

Label(root4,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=12)
Label(root4,text='Add Bus Route Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=12,pady=20)
def add_route():
    route_id=r_id.get()
    start_station=s_station.get()
    start_id=s_id.get()
    end_station=e_station.get()
    end_id=e_id.get()
    con4=sqlite3.Connection('Bus_DB')
    cur4=con4.cursor()
    cur4.execute('create table if not exists route(r_id varchar(5) not null primary key,s_name varchar(20),s_id varchar(5),e_name varchar(20),e_id varchar(5) )')
    cur4.execute('select r_id from route')
    res=cur4.fetchall()
    if (route_id,) in res:
        showerror('ERROR',"Route id already exists")
    else:
        start_station=start_station.lower()
        end_station=end_station.lower()
        cur4.execute('insert into route(r_id,s_name,s_id,e_name,e_id) values(?,?,?,?,?)',(route_id,start_station,start_id,end_station,end_id))
        con4.commit()
        showinfo('Success',"Route record added successfully!!")

Label(root4, text="Route ID", font='Arial 12', fg='black').grid(row=3, column=0)
r_id=Entry(root4)
r_id.grid(row=3, column=1)
Label(root4, text="Staring station", font='Arial 12', fg='black').grid(row=3, column=2)
s_station=Entry(root4)
s_station.grid(row=3, column=3)
Label(root4, text="Station ID", font='Arial 12', fg='black').grid(row=3, column=4)
s_id=Entry(root4)
s_id.grid(row=3, column=5)
Label(root4, text="Ending station", font='Arial 12', fg='black').grid(row=4, column=1)
e_station=Entry(root4)
e_station.grid(row=4, column=2)
Label(root4, text="Ending Station ID", font='Arial 12', fg='black').grid(row=4, column=3)
e_id=Entry(root4)
e_id.grid(row=4,column=4)

Button(root4, text="Add Route", font='Arial 12 ', bg='Pale Green', fg='black',command=add_route).grid(row=4, column=8)
Button(root4, text="Delete Route", font='Arial 12', bg='Pale Green2', fg='black').grid(row=4, column=9)


def ho():
    root4.destroy()
    import Home
    
home4=PhotoImage(file='.\\home.png')
Button(root4,image=home4,bg='Pale Green',command=ho).grid(row=3,column=8,pady=50)
root4.mainloop()





















root4.mainloop()
