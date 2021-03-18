from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

cursor=sqlite3.connect("my_db.db")

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end',values=i)

def search():
    q2=q.get()
    query="select * from customers WHERE first_name like '%"+q2+"%' OR last_name like '%"+q2+"%'"
    rows=cursor.execute(query).fetchall()
    update(rows)

def clear():
    # query="select * from customers"
    # rows=cursor.execute(query).fetchall()
    # update(rows)
    trv.delete(*trv.get_children())

def getrow(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item["values"][0])
    t2.set(item["values"][1])
    t3.set(item["values"][2])
    t4.set(item["values"][3])
    t5.set(item["values"][4])

def update_customer():
    fname = t2.get()
    lname = t3.get()
    age = t4.get()
    sex = t5.get()
    custid=t1.get()

    if messagebox.askyesno("Confirm Please","Do you wanna update customer?"):
        query="Update customers Set first_name=""?"",last_name=""?"",age=""?"",sex=""?"" where id=""?"""
        cursor.execute(query,(fname,lname,age,sex,custid))
        cursor.commit()

def add_new():
    fname=t2.get()
    lname=t3.get()
    age=t4.get()
    sex=t5.get()
    # query="insert into customers(first_name,last_name,age,sex) values('"+fname+"','"+lname+"','"+age+"','"+sex+"')"
    query="insert into customers(first_name,last_name,age,sex) values(""?"",""?"",""?"",""?"")"
    cursor.commit()

    cursor.execute(query,(fname,lname,age,sex))
def delete_customer():
    customers_id=t1.get()
    if messagebox.askyesno("Confirm Delete","Are you sure want to delte"):
        query="delete from customers where id="+customers_id
        cursor.execute(query)
        cursor.commit()
        clear()
    else:
        return TRUE

#adding a phote in the background
# bk_immage=tk.PhotoImage(file="cars.png")
# bk_label=tk.Label(root,image=bk_immage)
# bk_label.place(relwidth=1,relheight=1)
root=Tk()
q=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()

wrapper1=LabelFrame(root,text="Customer List")
wrapper2=LabelFrame(root,text="Search")
wrapper3=LabelFrame(root,text="Customer Data")

wrapper1.pack(fill="both",expand="yes")
wrapper2.pack(fill="both",expand="yes")
wrapper3.pack(fill="both",expand="yes")

trv=ttk.Treeview(wrapper1,columns=(1,2,3,4,5),show="headings",height="35")
trv.pack()

headings=["Customer ID","First Name","Last Name","Age","Sex"]
s=1
for i in headings:
    trv.column(s ,minwidth=80, width=380,stretch=0,anchor="c")
    trv.heading(s, text=i)
    trv.heading(s,text=i)
    s = s + 1

#event Listiner
trv.bind("<Double 1>",getrow)

query="select * from customers"
rows=cursor.execute(query).fetchall()
update(rows)

#Search Section
lbl=Label(wrapper2,text="Search")
lbl.pack(side=tk.LEFT,padx=10)
ent=Entry(wrapper2,textvariable=q)
ent.pack(side=tk.LEFT,padx=6)
btn=Button(wrapper2,text="Search",command=search)
btn.pack(side=tk.LEFT,padx=6)
cbtn=Button(wrapper2,text="Clear",command=clear)
cbtn.pack(side=tk.LEFT,padx=6)
#event listnere for when pressing ENTER KEY does the research
ent.bind("<Return>", (lambda event: search()))

#User data Section
lbl1=Label(wrapper3,text="Customer ID")
lbl1.grid(row=0,column=0,padx=5,pady=3)
ent1=Entry(wrapper3,textvariable=t1)
ent1.grid(row=0,column=1,padx=5,pady=3)

lbl2=Label(wrapper3,text="First Name")
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2=Entry(wrapper3,textvariable=t2)
ent2.grid(row=1,column=1,padx=5,pady=3)

lbl3=Label(wrapper3,text="Last Name")
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3=Entry(wrapper3,textvariable=t3)
ent3.grid(row=2,column=1,padx=5,pady=3)

lbl4=Label(wrapper3,text="Age")
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4=Entry(wrapper3,textvariable=t4)
ent4.grid(row=3,column=1,padx=5,pady=3)

lbl5=Label(wrapper3,text="SEX")
lbl5.grid(row=4,column=0,padx=5,pady=3)
ent5=Entry(wrapper3,textvariable=t5)
ent5.grid(row=4,column=1,padx=5,pady=3)

up_btn=Button(wrapper3,text="Update",command=update_customer)
add_btn=Button(wrapper3,text="Add new",command=add_new)
delete_btn=Button(wrapper3,text="delete",command=delete_customer)

add_btn.grid(row=5,column=0,padx=5,pady=3)
up_btn.grid(row=5,column=1,padx=5,pady=3)
delete_btn.grid(row=5,column=2,padx=5,pady=3)


root.title("My Application")
root.geometry("800x700")
root.mainloop()
