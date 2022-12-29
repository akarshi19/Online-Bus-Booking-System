from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=14,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=14)
Label(root,text='Add Bus Operator Details',font='Arial 18',fg='Green2').grid(row=2,columnspan=14,pady=20)
def op_add():
    iid = opr_id.get()
    iname = name.get()
    iaddress = address.get()
    iphone = phone.get()
    iemail = email.get()
    con=sqlite3.Connection("Bus_DB")
    cur=con.cursor()
    cur.execute('create table if not exists operator(opr_id varchar(5) primary key,name varchar(20),address varchar(50),phone char(10),email varchar(30))')
    cur.execute('select opr_id from operator')
    res=cur.fetchall()
            
    if len(iid) > 0 and len(iid) <= 5 and iid.isnumeric():
        if  len(iname) < 20 and len(iname) > 0:
            if len(iaddress) < 50 and len(iaddress) > 0:
                if iphone.isnumeric() and len(iphone) == 10:
                    if len(iemail) > 0 and len(iemail) < 30:
                        if (iid,) in res:
                            showerror("ERROR","operator id already exists!!")
                        else:
                            cur.execute('insert into operator (opr_id,name,address,phone,email)values(?,?,?,?,?)',(iid, iname, iaddress, iphone, iemail))
                            con.commit()
                            showinfo('success', "operator added successfully!!")
                            Label(root,text=iid,font='Arial 10').grid(row=4,column=3)
                            Label(root,text=iname,font='Arial 10').grid(row=4,column=5)
                            Label(root,text=iaddress,font='Arial 10').grid(row=4,column=7)
                            Label(root,text=iphone,font='Arial 10').grid(row=4,column=9)
                            Label(root,text=iemail,font='Arial 10').grid(row=4,column=11)    
                    else:
                        showerror("invalid input", "enter email correctly")
                else:
                    showerror("invalid input", "enter phone correctly")
            else:
                showerror("invalid input", "enter address correctly")
        else:
            showerror("invalid input", "enter name correctly")
    else:
        showerror("invalid input", "enter id correctly")


##Label(root, image=bus).grid(row=0, column=0, columnspan=12)
##Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=1,column=0,columnspan=12)
##                                                                                                          
##Label(root, text="Add Bus Operator Details", font='Arial 20 bold', bg='dark orchid', fg='black').grid(row=2,column=0,pady=20,columnspan=12)
Label(root, text="Operator ID", font='Arial 12', fg='black').grid(row=3, column=2)
opr_id = Entry(root)
opr_id.grid(row=3, column=3)
Label(root, text="Name", font='Arial 12', fg='black').grid(row=3, column=4)
name = Entry(root)
name.grid(row=3, column=5)
Label(root, text="Address", font='Arial 12', fg='black').grid(row=3, column=6)
address = Entry(root)
address.grid(row=3, column=7)
Label(root, text="Phone", font='Arial 12', fg='black').grid(row=3, column=8)
phone = Entry(root)
phone.grid(row=3, column=9)
Label(root, text="Email", font='Arial 12', fg='black').grid(row=3, column=10)
email =  Entry(root)
email.grid(row=3, column=11)



Button(root, text="Add", font='Arial 12', bg='Pale Green', fg='black',command=op_add).grid(row=3, column=12)
Button(root, text="Edit", font='Arial 12', bg='Pale Green', fg='black').grid(row=3, column=13)

def ho():
    root.destroy()
    import Home
    
home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='Pale Green',command=ho).grid(row=4,column=12,pady=50)

root.mainloop()



