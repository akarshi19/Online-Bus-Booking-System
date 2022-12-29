from tkinter import *
from tkinter.messagebox import*
import sqlite3
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=3,padx=w/2.5)
Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=2,column=0,columnspan=12)
Label(root,text='Check Your Booking',font='Arial 15',fg='Green3',bg='Pale Green').grid(row=3,column=0,columnspan=12)
Label(root,text='Enter your Mobile No.',font='Arial 10',width=15).grid(row=4,column=0,sticky='E')
mob=Entry(root)
mob.grid(row=4,column=1)


def check_tkt():
##    frame=Frame(root,highlightbackground='Black',highlightthickness=2,height=100,width=500)
##    frame.grid(row=5,columnspan=5)
    mobile=mob.get()
    if len(mobile)==10 and mobile.isdigit():
        con=sqlite3.Connection('Bus_DB')
        cur=con.cursor()
        cur.execute('select * from booking_history where phone=?',[mobile])
        res_tkt=cur.fetchall()
        for i in res_tkt:
            name=i[0]
            gen=i[1]
            seat=i[2]
            phone=i[3]
            age=i[4]
            ref=i[5]
            book_date=i[6]
            travel_date=i[7]
            b_i_d=i[8]
        cur.execute('select fare,route_id from bus where bus_id=?',[b_i_d])
        res_bus=cur.fetchall()
        fare=res_bus[0][0]
        route_id=res_bus[0][1]
        cur.execute('select s_name,e_name from route where r_id=?',[route_id])
        res_route=cur.fetchall()
        s_name=res_route[0][0]
        e_name=res_route[0][1]
        cur.execute('select booking_ref from booking_history where phone=?',[phone])
        res_ref=cur.fetchall()
        b_ref=res_ref[0][0]

        Label(text="YOUR TICKET", font='Arial 12 ',bg='Sky Blue').grid(row=6,columnspan=12 )
        Label(text="Booking ref = "+b_ref,font='Arial 12').grid(row=7,column=0)
        Label(text="Name = " + name, font='Arial 12').grid(row=7, column=1)
        Label(text="Gender = " + gen, font='Arial 12 ').grid(row=8, column=0)
        Label(text="No of seats = " + str(seat), font='Arial 12 ').grid(row=8, column=1)
        Label(text="Age = " + str(age), font='Arial 12').grid(row=9, column=0)
        Label(text="Booked on = " + book_date, font='Arial 12 ').grid(row=9, column=1)
        Label(text="Travel date = " + travel_date, font='Arial 12 ').grid(row=10, column=0)
        Label(text="Fare = " + str(fare), font='Arial 12 ').grid(row=10, column=1)
        Label(text="Total fare = " + str(fare*seat), font='Arial 12 ').grid(row=11, column=0,columnspan=4)


       
        showinfo('Success','Seat Booked...')



Button(root,text='Check Booking',font='Arial 10',command=check_tkt).grid(row=4,column=2,sticky='W')
root.mainloop()
##def checknumber(mobNumber):
##    count=0
##    for i in mobNumber:
##        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
##            count+=1
##    if count==10:
##        return True
##    else:
##        return False
##    def entrycheck():
##        if len(mobNumber.get())!=10:
##            showerror('Value missing','Enter correct Mobile Number')
##        elif checknumber(mobNumber.get())==False:
##            showerror('Invalid input','Enter number properly')


##'''cur8.execute('''select booking_ref from booking_history where mobile=?''',[phone])
##        res_ref=cur8.fetchone()
##        b_ref=res_ref[0][0]
##        con8.commit()
##        print(b_ref)  '''     

##        cur8.execute('''select Fare from Bus where B_ID=?''',[b_i_d])
##        res_bus=cur8.fetchone()
##        fare=res_bus[0][0]
##        con8.commit()












