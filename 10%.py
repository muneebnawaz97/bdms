from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.geometry("400x200")


#Database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

mycursor = mydb.cursor()
mycursor.execute("USE BDMS")

#Create submit function

def login():
    #clear Text boxes
    id=Userid.get()
    p=password.get()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")
    query="SELECT * FROM LOGIN_CREDENTIALS WHERE login_username=%s AND login_password=%s"
    args=(id,p)
    mycursor.execute(query,args)
    myresult=mycursor.fetchall()
    if myresult == []:
        Userid.delete(0,END)
        password.delete(0,END)
        not_exists=Label(root,text='Incorrect username or password')
        not_exists.grid(row=6,column=1)
    else:
        Userid.delete(0,END)
        password.delete(0,END)
        root.destroy()
        main_menu()
    
    mydb.commit()
    mydb.close()

def main_menu():
    main=Tk()
    main.geometry('700x700')
    submit_btn=Button(main,text="Add Member",command=add_member)
    submit_btn.grid(row=0,column=10,columnspan=2,pady=10,padx=10,ipadx=100)
    main.mainloop()

def add(Userid,Username,password,main,role):
    id=Userid.get()
    name=Username.get()
    p=password.get()
    r=role.get()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")
    
    query = "INSERT INTO LOGIN_CREDENTIALS(login_id, login_username, login_password, user_role) VALUES(%s,%s,%s,%s)"
    arg = (id, name, p, r)
	
    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Entry already exists')
        warn_label.grid(row=12,column=0)

    mydb.close()

            
        

def add_member():
    main=Tk()
    main.geometry('400x400')
    Userid = Entry(main,width=30)
    Userid.grid(row=4,column=4,padx=20)

    Username = Entry(main,width=30)
    Username.grid(row=5,column=4,padx=20)

    password = Entry(main,width=30)
    password.grid(row=6,column=4,padx=20)

    Userid_label=Label(main,text='User ID')
    Userid_label.grid(row=4,column=0)

    Username_label=Label(main,text='Username')
    Username_label.grid(row=5,column=0)

    password_label=Label(main,text='password')
    password_label.grid(row=6,column=0)

    role = Entry(main,width=30)
    role.grid(row=7,column=4,padx=20)

    role_label=Label(main,text='Role: admin or user')
    role_label.grid(row=7,column=0)
    
    add_btn=Button(main,text="Add Member",command=lambda: add(Userid,Username,password,main,role))
    add_btn.grid(row=10,column=3,columnspan=2,pady=10,padx=10,ipadx=100)
    main.mainloop()



Userid = Entry(root,width=30)
Userid.grid(row=4,column=4,padx=20)

password = Entry(root,width=30)
password.grid(row=5,column=4,padx=20)
 
# create labels

Userid_label=Label(root,text='Username')
Userid_label.grid(row=4,column=0)

password_label=Label(root,text='password')
password_label.grid(row=5,column=0)

not_exists=Label(root,text='')
not_exists.grid(row=6,column=1)

submit_btn=Button(root,text="Login",command=login)
submit_btn.grid(row=10,column=3,columnspan=2,pady=10,padx=10,ipadx=100)


root.mainloop()

