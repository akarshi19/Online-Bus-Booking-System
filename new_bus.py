from tkinter import *
from tkinter.messagebox import*
import sqlite3

root1=Tk()
h,w=root1.winfo_screenheight(),root1.winfo_screenwidth()
root1.geometry('%dx%d+0+0'%(w,h))

bus1=PhotoImage(file='.\\Bus_for_project.png')
Label(root1,image=bus1).grid(row=0,column=0,columnspan=16,padx=w/2.5)

Label(root1,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=16)
Label(root1,text='Add Bus Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=16,pady=20)

Label(root1, text="Bus ID", font='Arial 12', fg='black').grid(row=3, column=2)
b_id = Entry(root1)
b_id.grid(row=3, column=3)

bus_type = StringVar()
bus_type.set("Select Bus Type")
opt = ["2x2", "AC 2x2", "3x2", "AC 3x2"]
d_menu = OptionMenu(root1, bus_type, *opt)
d_menu.grid(row=3, column=4)
        
Label(root1, text="Capacity", font='Arial 12', fg='black').grid(row=3, column=5)
capacity = Entry(root1)
capacity.grid(row=3, column=6)
        
Label(root1, text="Fare Rs", font='Arial 12', fg='black').grid(row=3, column=7)
fare = Entry(root1)
fare.grid(row=3, column=8)
        
Label(root1, text="Operator ID", font='Arial 12', fg='black').grid(row=3, column=9)
op_id = Entry(root1)
op_id.grid(row=3, column=10)
        
Label(root1, text="Route ID", font='Arial 12', fg='black').grid(row=3, column=11)
r_id = Entry(root1)
r_id.grid(row=3, column=12)

def bus_add():
    bid=b_id.get()
    dmenu=bus_type.get()
    capa=capacity.get()
    fare_rs=fare.get()
    opid=op_id.get()
    route_id=r_id.get()
    con1=sqlite3.Connection('Bus_DB')
    cur1=con1.cursor()
    cur1.execute('create table if not exists bus(bus_id varchar(5) not null primary key,bus_type varchar(10),capacity int,fare int,op_id varchar(5) not null,route_id varchar(5) not null,foreign key(op_id) references operator(opr_id),foreign key(route_id) references route(r_id))')
    cur1.execute('select bus_id from bus')
    res=cur1.fetchall()
    if (bid,) in res:
        showerror("error","bus id already exists!!!")
    else:
        data="bus_id="+bid+"     bus_type="+dmenu+"     capacity="+capa+"     fare="+fare_rs+"     op_id="+opid+"     route_id="+route_id
        cur1.execute('insert into bus(bus_id,bus_type,capacity,fare,op_id,route_id) values(?,?,?,?,?,?)',(bid,dmenu,capa,fare_rs,opid,route_id))
        con1.commit()
        showinfo('success', "bus added successfully!!")
        Label(root1,text=data).grid(row=6,columnspan=12)
        
                      
Button(root1, text="Add Bus", font='Arial 12 bold', bg='Pale Green', fg='black',command=bus_add).grid(row=5, column=7,pady=40)
                                                                                         
Button(root1, text="Edit Bus", font='Arial 12 bold', bg='Pale Green', fg='black').grid(row=5, column=8)
                                                                                          

        
def ho1():
    root1.destroy()
    import Home
    
home1=PhotoImage(file='.\\home.png')
Button(root1,image=home1,bg='Pale Green',command=ho1).grid(row=5,column=9)        
        
root1.mainloop()






