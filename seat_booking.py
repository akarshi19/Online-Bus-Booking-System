from tkinter import *
from tkinter.messagebox import*
from datetime import date
import sqlite3

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=11,padx=w/2.5)

Label(root,text='Online Bus Booking System',font='Arial 20',fg='Red',bg='Sky Blue').grid(row=1,column=0,columnspan=11,pady=2)
Label(root,text='Enter Journey Details',font='Arial 15',fg='Green3',bg='Pale Green').grid(row=3,column=0,columnspan=11,pady=2)
to_place=Label(root,text='To',font='Arial 10').grid(row=5,column=1)
to_place=Entry(root)
to_place.grid(row=5,column=2)
from_place=Label(root,text='From',font='Arial 10').grid(row=5,column=3)
from_place=Entry(root)
from_place.grid(row=5,column=4)
journey_date=Label(root,text='Journey Date',font='Arial 10').grid(row=5,column=5)
journey_date=Entry(root)
journey_date.grid(row=5,column=6)

def show_bus(): 
    tp=to_place.get()
    fp=from_place.get()
    jd=journey_date.get()

    if tp.isalpha() and fp.isalpha():
        if not jd=='':
            tp = tp.lower()
            fp = fp.lower()
            con=sqlite3.Connection('Bus_DB')
            cur=con.cursor()
            cur.execute('select r_id from route where s_name=? and e_name=?', (fp, tp))
            res_route = cur.fetchall()
            if len(res_route)==0:
                showerror('no route found','we are currently not running on this route')
            else:
                for i in res_route:
                    for j in i:
                        val_route = str(j)

                cur.execute('select bus_id from bus where route_id=?', (val_route))
                res_bid = cur.fetchall()

                if len(res_bid)==0:
                    showerror('no bus found','we have not started any bus on this route yet!!')
                else:
                    val_bid = []
                    for i in res_bid:
                        for j in i:
                            val_bid.append(j)
                    res_new_bid=[]
                    for i in range(len(val_bid)):
                        cur.execute('select b_id from running where run_date=? and b_id=? ',(jd, val_bid[i]))
                        res_new_bid.append(cur.fetchall())
                            #print(res_new_bid)
                    b=[]
                    for i in res_new_bid:
                        for j in i:
                            b.append(j[0])

                            #print(b)
                    if len(b)==0:
                        showerror('no running bus',"try another date!!")
                    else:
                        Label(root,text='Select bus ',font='Arial 10').grid(row=7,column=1)
                        Label(root, text='Operator ', font='Arial 10').grid(row=7, column=2)
                        Label(root, text='Bus_type ', font='Arial 10').grid(row=7, column=3)
                        Label(root, text='Available Capacity ', font='Arial 10').grid(row=7, column=4)
                        Label(root, text='Fare ', font='Arial 10').grid(row=7, column=5)
                        r=8
                        bus_no=IntVar()
                        bus_select = IntVar()
                        serial_no=1
                        for i in b:
                            bus_no=i
                            cur.execute('select op_id from bus where bus_id=?',(i))
                            res_opr_id=cur.fetchall()
                            for j in res_opr_id:
                                opr_id=j[0]

                            cur.execute('select name from operator where opr_id=?',(opr_id))
                            res_opr_name=cur.fetchall()
                            for j in res_opr_name:
                                opr_name=j[0]

                            cur.execute('select bus_type from bus where bus_id=?',(i))
                            res_bus_type=cur.fetchall()
                            for j in res_bus_type:
                                bus_type=j[0]

                            cur.execute('select seat_avail from running where run_date=? and b_id=?',(jd,i))
                            res_seat_avail=cur.fetchall()
                            for j in res_seat_avail:
                                seat_avail=j[0]

                            cur.execute('select fare from bus where bus_id=?',(i))
                            res_fare=cur.fetchall()
                            for j in res_fare:
                                fare=j[0]

                            def show_button():
                                Button(root, text='Proceed', bg='Pale Green', fg='black', font='Arial 12',command=proceed).grid(row=8, column=10, padx=10)
                                

                            var=Radiobutton(root,value=bus_no,variable=bus_select,command=show_button)
                            var.grid(row=r,column=1)
                            Label(root, text=opr_name, font='Arial 10').grid(row=r, column=2)
                            Label(root, text=bus_type, font='Arial 10 ').grid(row=r, column=3)
                            Label(root, text=seat_avail, font='Arial 10 ').grid(row=r, column=4)
                            Label(root, text=fare, font='Arial 10 ').grid(row=r, column=5)

                            r+=1
                            serial_no+=1

                        def proceed():
                            f_bus_id = bus_select.get()

                            
                            Label(root,text='Fill passenger details', bg='Sky blue', fg='red',font='Calibri 18').grid(row=13,columnspan=11,pady=5)
                            

                            Label(root,text='Name',font='Arial 10 ').grid(row=15,column=0)
                            pname = Entry(root)
                            pname.grid(row=15,column=1)

                            gender = StringVar()
                            gender.set("Select Gender")
                            opt = ["Male", "Female", "Other"]
                            g_menu = OptionMenu(root, gender, *opt)
                            g_menu.grid(row=15, column=3)

                            Label(root, text='No of seats', font='Arial 10').grid(row=15, column=4)
                            pseat=Entry(root)
                            pseat.grid(row=15,column=5)

                            Label(root, text='Mobile', font='Arial 10').grid(row=15, column=6)
                            pmobile = Entry(root)
                            pmobile.grid(row=15, column=7)

                            Label(root, text='age', font='Arial 10').grid(row=15, column=8)
                            page = Entry(root)
                            page.grid(row=15, column=9)

                            def book_seat():
                                name=pname.get()
                                gen=gender.get()
                                seats=pseat.get()
                                seats=int(seats)
                                age=page.get()
                                age=int(age)
                                mobile=pmobile.get()
                                bid=bus_select.get()
                                if len(mobile)==10:
                                    if len(name)>0 and len(name)<20:
                                        if age>0 and age<150:
                                            if seats>0 and seats<6:
                                                        #print(name, gen, age, mobile, seats, bid)
                                                booking_ref=1
                                                cur.execute('create table if not exists booking_history(name varchar(20),gender char(1),no_of_seat int,phone char(10),age int,booking_ref varchar(10) not null primary key,booking_date date,travel_date date,bid varchar(5),foreign key(bid) references bus(bus_id))')
                                                cur.execute('select booking_ref from booking_history')
                                                res_ref=cur.fetchall()
                                                ref=[]
                                                for i in res_ref:
                                                    ref.append(i[0])
                                                booking_ref=len(ref)+1
                                                        #print(booking_ref)
                                                cur_date=date.today()
                                                cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                con.commit()
                                                cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                res_s=cur.fetchall()
                                                s=res_s[0][0]
                                                s=s-seats
                                                cur.execute('update running set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                con.commit()
                                                showinfo("succefull","booking successfull")
##                                                root.destroy()
##                                                import bus_ticket

                                            else:
                                                showerror("booking limit exceed","you can only book upto 5 seats")
                                        else:
                                            showerror("incorrect age","enter valid age")
                                    else:
                                        showerror("incorrect name","enter valid name")
                                else:
                                    showerror("invalid mobile no","enter valid mobile no")


                            Button(root, text='Book Seat', bg='Pale Green', fg='black', font='Arial 12 ',command=book_seat).grid(row=11, column=10)



        else:
            showerror('error','enter journey date')


    else:
        showerror('ERROR',"enter correctly!!")

Button(root,text='Show Bus',font='Arial 10',bg='Sea Green',command=show_bus).grid(row=5,column=7)
def ho3():
    root.destroy()
    import Home
home3=PhotoImage(file='.\\home.png')
Button(root,image=home3,bg='Green',command=ho3).grid(row=5,column=8,pady=2)
root.mainloop()

             
##def data1():
##    Label(root3,text='Select Bus',font='Arial 10',fg='Forest Green').grid(row=7,column=1)
##    Label(root3,text='Operator',font='Arial 10',fg='Forest Green').grid(row=7,column=2)
##    Label(root3,text='Bus Type',font='Arial 10',fg='Forest Green').grid(row=7,column=3)
##    Label(root3,text='Available/Capacity',font='Arial 10',fg='Forest Green').grid(row=7,column=4)
##    Label(root3,text='Fare',font='Arial 10',fg='Forest Green').grid(row=7,column=5)
##    x1=to.get()
##    x2=fr.get()
##    x3=jd.get()
##    
##    cur1.execute('''select Name,Type,Seat_Available,Capacity,Fare,m.B_ID
##           from Operator,Bus as m,Runs as l,Route as f, Route as t
##           where f.sname=? and t.sname=? and Date=? and l.b_id=m.B_ID and
##           f.S_ID<t.S_ID and f.R_ID=t.R_id and t.R_ID=t.R_id''',(x1,x2,x3))
##    res1=cur1.fetchall()
##    num=8
##    for i in res1:
##       r1=Radiobutton(root3,text='Select',font='calibri 12 bold',bg='spring green',variable=bus_select,value=i[5],indicator=0)
##       r1.grid(row=num,column=1,padx=w//160,pady=h//80)
##        
##       operator=Label(root3, text = i[0], fg = "blue1",font='calibri 12 bold')
##       operator.grid(row = num, column=2)
##       b_type=Label(root3, text = i[1], fg = "blue1",font='calibri 12 bold')
##       b_type.grid(row = num, column=3)
##       a_seat=Label(root3, text = i[2], fg = "blue1",font='calibri 12 bold')
##       a_seat.grid(row = num, column=4)
##       t_seat=Label(root3, text = i[3], fg = "blue1",font='calibri 12 bold')
##       t_seat.grid(row = num, column=5)
##       fare=Label(root3, text = i[4], fg = "blue1",font='calibri 12 bold')
##       fare.grid(row = num, column=6)
##       num=num+1
##    
##    con1.commit()
##    con1.close()
##    
##    Button(root3,text='Proceed to Book',font='Arial 10',bg='Pale Green',command=details).grid(row=8,column=10,pady=10)
##    print(res1)
##
##def details():
##     booked_bus_id=bus_select.get()
##
##     if (booked_bus_id=='None'):
##        showwarning("Warning",'Please select a bus')
##
##     else:
##        Label(root3,text='Fill Passenger Details to Book the Bus Ticket',font='Arial 18',fg='Red',bg='Sky Blue').grid(row=13,columnspan=11,pady=5)
##        name=Label(root3,text='Name',font='Arial 10')
##        name.grid(row=15,column=0)
##        name=Entry(root3)
##        name.grid(row=15,column=1)
##
##        Label(root3,text='Gender',font='Arial 10').grid(row=15,column=2)
##        e_gender=StringVar()
##        option=('Male','Female','Other')
##        e_gender.set('')
##        e_menu=OptionMenu(root3,e_gender,*option)
##        e_menu.grid(row=15,column=3)
##        
##        seats=Label(root3,text='No. of Seats',font='Arial 10',width=8)
##        seats.grid(row=15,column=4)
##        seats=Entry(root3,width=5)
##        seats.grid(row=15,column=5)
##        
##        mobile=Label(root3,text='Mobile  No.',font='Arial 10',width=10)
##        mobile.grid(row=15,column=6)
##        mobile=Entry(root3)
##        mobile.grid(row=15,column=7,sticky='W')
##        
##        age=Label(root3,text='Age',font='Arial 10',width=5)
##        age.grid(row=15,column=8)
##        age=Entry(root3,width=5)
##        age.grid(row=15,column=9)
##        
##        con1=sqlite3.connect('Bus_DB')
##        cur1=con1.cursor()
##        
##        cur1.execute(' select Fare from Bus where B_ID={}'.format(bus_select.get()))
##        Fare=cur1.fetchone()
##        fare=int(Fare[0])
##        con1.commit()
##        print(fare)
##        
##        con1.close()
##        def confirm():
##            n=int(seats.get())
##            tf=n*fare
##            tf=str(tf)
##            answer = askyesno("Booking Confirmation", "Are you sure you want to book the bus?\n Total Amount to be paid is Rs "+tf)
##            if answer:
##                name1=name.get()
##                age1=age.get()
##                nos=seats.get()
##                mob=mobile.get()
##                gender=e_gender.get()
##                T_date=jd.get()
##                con1=sqlite3.connect('Bus_DB')
##                cur1=con1.cursor()
##                cur1.execute('create table if not exists booking_history (pname,gender,age,mobile,bus,travelling_date,booking_date,no_of_seats,total_fare,booking_ref_number)')
##                cur1.execute('''select count(*)+1 from booking_history''')
##                a=cur1.fetchone()
##                count=a[0]
##                cur1.execute('''insert into booking_history (pname,gender,age,mobile,bus,travelling_date,booking_date,no_of_seats,total_fare,booking_ref_number) values (?,?,?,?,?,?,DATE(),?,?,?)''',(name1,gender,age1,mob,booked_bus_id,T_date,nos,tf,count))
##                cur1.execute('''update Runs set seat_available=seat_available-? where b_id=? and Date=?''',(nos,booked_bus_id,T_date))
##                con1.commit()
##
##                root3.destroy()
##                import bus_ticket
##        y=Button(root3,text='Book Seat',font='Arial 10',bg='Pale Green',command=confirm)
##        y.grid(row=11,column=10) 





              
##                def error():
##                    if len(name.get())==0:
##                        showerror("value missing","please enter full details")
##                    elif len(seats.get())==0:
##                        showerror("value missing","please enter number of seats")
##                    elif len(mobile.get())==0:
##                        showerror("value missing","please enter your mobile number")
##                    elif len(age.get())==0:
##                        showerror("value missing","Please enter your Age")
##                    else:
##                        showinfo("fare","Total amount to be paid is fare*no. of seats")
##                error()




   















