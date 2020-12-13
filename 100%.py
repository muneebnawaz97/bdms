from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.geometry("400x200")


#Database

mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )   

mycursor = mydb.cursor()
#mycursor.execute("USE BDMS")

#Create submit function

def login():
    #clear Text boxes
    id=Userid.get()
    p=password.get()
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )

    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
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
        main_menu(myresult[0][3])
        
    
    mydb.commit()
    mydb.close()

def main_menu(user_role):
    main = Tk()
    main.geometry('800x800')
    if user_role== 'admin':
        mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )

        mycursor = mydb.cursor()
        #mycursor.execute("USE BDMS")
        num=100000
        query = "SELECT * FROM PRODUCTS WHERE total_qty<=10000"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if myresult != []:
        #print(myresult[0][1])
            string=''
            for i in range(len(myresult)):
                string+=str(myresult[i][1]) + '               ' + str(myresult[i][2]) + '               ' + str(myresult[i][3]) + '\n '
            popup=Tk()
            popup.geometry('500x300')
            popup.wm_title('LOW STOCK WARNING')
            desc=Label(popup,text='     Category        Item Name      Quantity Remaining')
            desc.grid(row=0, column=3)
            items=Label(popup,text=string)
            items.grid(row=1, column=3)
            b1=Button(popup,text='Okay',command=popup.destroy)
            b1.grid(row=2,column=3,pady=10,padx=10,ipadx=100)
            #popup.mainloop()
        mydb.commit()
        mydb.close()
    
    if user_role == 'admin':
        
        submit_btn = Button(main, text="Add Member", command=add_member)
        submit_btn.grid(row=0, column=10, columnspan=2,pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Remove Member",command= remove_member)
        submit_btn.grid(row=1,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Edit Member",command=edit_member)
        submit_btn.grid(row=2,column=10,columnspan=2,pady=10,padx=10,ipadx=100)
    
        submit_btn=Button(main,text="Edit Product",command=edit_product)
        submit_btn.grid(row=0,column=20,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn = Button(main, text="Add Product", command=add_product)
        submit_btn.grid(row=1, column=20, columnspan=2,
                    pady=10, padx=10, ipadx=100)

        submit_btn = Button(main, text="Remove Products", command=remove_product)
        submit_btn.grid(row=2, column=20, columnspan=2,pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Generate Userreport",command=generate_userReport)
        submit_btn.grid(row=3,column=20,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn = Button(main, text="View Product/s", command=view_product)
        submit_btn.grid(row=4, column=20, columnspan=2,
                    pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Generate Bill",command=generate_bill)
        submit_btn.grid(row=3,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Remove Bill",command=Remove_order)
        submit_btn.grid(row=4,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn = Button(main, text="Warehouse Capacity", command=warehse_gui)
        submit_btn.grid(row=5, column=20, columnspan=2,pady=10, padx=10, ipadx=100)
        
        submit_btn=Button(main,text="Sales Summary Report", command=sale_report)
        submit_btn.grid(row=6,column=20,columnspan=2,pady=10,padx=10,ipadx=100)
        
        submit_btn=Button(main,text="Place Order",command=order_product_gui)
        submit_btn.grid(row=5,column=10,columnspan=2,pady=10,padx=10,ipadx=100) 
        
        submit_btn=Button(main,text="Generate Performance Report",command=generate_performance)
        submit_btn.grid(row=6,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Edit Order/Bill",command=Edit_Bill)
        submit_btn.grid(row=7,column=10,columnspan=2,pady=10,padx=10,ipadx=100)
        
    else:
        submit_btn=Button(main,text="Generate Bill",command=generate_bill)
        submit_btn.grid(row=2,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Remove Bill",command=Remove_order)
        submit_btn.grid(row=3,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

    
        submit_btn=Button(main,text="Place Order",command=order_product_gui)
        submit_btn.grid(row=4,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Edit Order/Bill",command=Edit_Bill)
        submit_btn.grid(row=5,column=10,columnspan=2,pady=10,padx=10,ipadx=100)



    main.mainloop()

def generate_performance():
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query ="SELECT prod_name,SUM(total_qty) FROM order GROUP BY prod_name"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)
    '''
    if myresult != []:
        #print(myresult[0][1])
            string=''
            for i in range(len(myresult)):
                string+=str(myresult[i][0]) + '               '+ str(myresult[i][1]) + '               ' + str(myresult[i][2])+ '               ' + str(myresult[i][3]) + '               ' + str(myresult[i][4]) + '               ' + str(myresult[i][5])+ '               ' + str(myresult[i][6]) + '               ' + str(myresult[i][7]) +' \n '
            popup=Tk()
            popup.geometry('600x600')
            popup.wm_title('Inventory Report')
            desc=Label(popup,text=' Product ID     Category        Item Name      Total Quantity    C_Price    S_Price      Dis_off    Dis_price')
            desc.grid(row=0, column=3)
            items=Label(popup,text=string)
            items.grid(row=1, column=3)
            b1=Button(popup,text='Okay',command=popup.destroy)
            b1.grid(row=2,column=3,pady=10,padx=10,ipadx=100)
            popup.mainloop()
        '''
    mydb.close()

def remove_product():
    main = Tk()
    main.geometry('700x400')

    Product_Category = Entry(main, width=30)
    Product_Category.grid(row=5, column=4, padx=20)
    Product_Category_label = Label(main, text='Category (Food/Dairy/Items)')
    Product_Category_label.grid(row=5, column=0)

    Product_Name = Entry(main, width=30)
    Product_Name.grid(row=6, column=4, padx=20)
    Product_Name_label = Label(main, text='Product Name')
    Product_Name_label.grid(row=6, column=0)

    rmv_btn = Button(main, text="Remove Product", command=lambda: prod_rmv(
        main, Product_Category, Product_Name))
    rmv_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    main.mainloop()


def prod_rmv(main, Product_Category, Product_Name):
    ctgry = Product_Category.get()
    name = Product_Name.get()

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )

    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "DELETE FROM PRODUCTS WHERE prod_category = %s AND prod_name = %s"
    arg = (ctgry, name)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Invalid Entry Try again')
        warn_label.grid(row=12, column=0)

    mydb.close()



def prod_rmv(main,Product_Category,Product_Name):
    ctgry=Product_Category.get()
    name=Product_Name.get()
    
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
    
    query = "DELETE FROM PRODUCTS WHERE prod_category = %s AND prod_name = %s"
    arg = (ctgry, name)
    
    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)
    mydb.close()



def add_product():
    main=Tk()
    main.geometry('700x400')
    
    Product_id = Entry(main,width=30)
    Product_id.grid(row=4,column=4,padx=20)
    Product_id_label=Label(main,text='Product ID')
    Product_id_label.grid(row=4,column=0)

    Product_Category = Entry(main,width=30)
    Product_Category.grid(row=5,column=4,padx=20)
    Product_Category_label=Label(main,text='Category (Food/Dairy/Items)')
    Product_Category_label.grid(row=5,column=0)

    Product_Name = Entry(main,width=30)
    Product_Name.grid(row=6,column=4,padx=20)
    Product_Name_label=Label(main,text='Product Name')
    Product_Name_label.grid(row=6,column=0)

    total_qty = Entry(main,width=30)
    total_qty.grid(row=7,column=4,padx=20)
    total_qty_label=Label(main,text='Total Qty of Product')
    total_qty_label.grid(row=7,column=0)
    
    Cost_Price = Entry(main,width=30)
    Cost_Price.grid(row=8,column=4,padx=20)
    Cost_Price_label=Label(main,text='Cost Price per unit')
    Cost_Price_label.grid(row=8,column=0)
    
    Sale_Price = Entry(main,width=30)
    Sale_Price.grid(row=9,column=4,padx=20)
    Sale_Price_label=Label(main,text='Sale Price per unit')
    Sale_Price_label.grid(row=9,column=0)

    Discount_offer = Entry(main,width=30)
    Discount_offer.grid(row=10,column=4,padx=20)
    Discount_offer_label=Label(main,text='Discount? (Y/N)')
    Discount_offer_label.grid(row=10,column=0)

    Discount_price = Entry(main,width=30)
    Discount_price.grid(row=11,column=4,padx=20)
    Discount_price_label=Label(main,text='Discount Price (0 means no discount)')
    Discount_price_label.grid(row=11,column=0)

    #Discounted_Price = ((100-Discount_perc)/100)*Sale_Price
    
    add_btn=Button(main,text="Add Product",command=lambda: prod_add(main,Product_id,Product_Category,Product_Name,total_qty,Cost_Price,Sale_Price,Discount_offer,Discount_price))
    add_btn.grid(row=13,column=3,columnspan=2,pady=10,padx=10,ipadx=100)
    main.mainloop()


def prod_add(main,Product_id,Product_Category,Product_Name,total_qty,Cost_Price,Sale_Price,Discount_offer,Discount_price):
    id=Product_id.get()
    ctgry=Product_Category.get()
    name=Product_Name.get()
    qty=total_qty.get()
    cp=Cost_Price.get()
    sp=Sale_Price.get()
    d=Discount_offer.get()
    dp=Discount_price.get()

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
    
    query = "INSERT INTO PRODUCTS(prod_id, prod_category, prod_name, total_qty, cost_price, sale_price, discount_offer, discount_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    arg = (id, ctgry, name, qty, cp, sp, d, dp)
    
    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)

    mydb.close()

def add(Userid, Username, password, main, role):
    id = Userid.get()
    name = Username.get()
    p = password.get()
    r = role
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "INSERT INTO LOGIN_CREDENTIALS(login_id, login_username, login_password, user_role) VALUES(%s,%s,%s,%s)"
    arg = (id, name, p, r)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Entry already exists')
        warn_label.grid(row=12, column=0)

    mydb.close()

def Edit_Bill():
    main=Tk()
    main.geometry('700x400')

    Product_Name1 = Entry(main,width=30)
    Product_Name1.grid(row=6,column=4,padx=20)
    Product_Name_label1=Label(main,text='Product to be Edited')
    Product_Name_label1.grid(row=6,column=0)

    total_qty = Entry(main,width=30)
    total_qty.grid(row=7,column=4,padx=20)
    total_qty_label=Label(main,text='Qty to be changed')
    total_qty_label.grid(row=7,column=0)
    
    add_btn=Button(main,text="Edit in cart",command=lambda: Bill_edit(main,Product_Name1,total_qty))
    add_btn.grid(row=14,column=4,columnspan=2,pady=10,padx=10,ipadx=100)
    
    
    Product_Name = Entry(main,width=30)
    Product_Name.grid(row=16,column=4,padx=20)
    Product_Name_label=Label(main,text='Product Name')
    Product_Name_label.grid(row=16,column=0)

    rmv_btn=Button(main,text="Remove Product from cart",command=lambda: Edit_rmvprod(main,Product_Name))
    rmv_btn.grid(row=18,column=3,columnspan=2,pady=10,padx=10,ipadx=100)
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS;")
    
    query = "SELECT * FROM ORDER;"
    mycursor.execute(query)
    i=20 
    for products in mycursor: 
        for j in range(len(products)):
            e = Entry(main, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, products[j])
        i=i+1
    mydb.commit()
    mydb.close() 
    main.mainloop()
    
def Edit_rmvprod(main,Product_Name):
    name=Product_Name.get()
    
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    
    mycursor = mydb.cursor()
    #ycursor.execute("USE BDMS;")
    print(name)
    query = "DELETE FROM ORDER WHERE prod_name="+"\""+ name +"\";"
    mycursor.execute(query)
    try:
        print(name)
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)
    mydb.close()
    
    
    
    
    
def Bill_edit(main,Product_Name,total_qty):
    name=Product_Name.get()
    qty=total_qty.get()
    print(name, qty)
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor(buffered=True)
    #mycursor.execute("USE BDMS")
    mycursor1 = mydb.cursor(buffered=True)
    #mycursor1.execute("USE BDMS")
    mycursor.execute("SELECT * FROM PRODUCTS WHERE prod_name LIKE " + "\'" + name + "\';")
    check_if_prod_exists_query =  mycursor.fetchone()
    mycursor1.execute("SELECT * FROM ORDER WHERE prod_name LIKE " + "\'" + name + "\';")
    check_if_prod_exists_query1 =  mycursor1.fetchone()

    print(check_if_prod_exists_query)
    print(check_if_prod_exists_query1)
    qty2= int(qty) - int(check_if_prod_exists_query1[1]) 
    if int(check_if_prod_exists_query[3]) < int(qty2):
        print(qty2)
        print(check_if_prod_exists_query[3])
        warn_label=Label(main,text='Less quantity product available.')
        warn_label.grid(row=12,column=0)
        print("Less quantity product available")
    else:
        print("C")
        mycursor2 = mydb.cursor(buffered=True)
        query = "UPDATE BDMS.ORDER SET total_qty=%s WHERE prod_name=%s;"
        arg = (qty, name)
        mycursor2.execute(query, arg)
        if (int(check_if_prod_exists_query1[1]) < int(qty)):
            qty1= int(qty) - int(check_if_prod_exists_query1[1])
            #qty1= qty1 + 1
            print(qty1)
            minus_qty = int(check_if_prod_exists_query[3]) - int(qty1)
            print("Minus:", minus_qty)
            mycursor.execute("UPDATE PRODUCTS SET total_qty = " + str(minus_qty) + " WHERE prod_name = \'"+name+"\'")
        elif (int(check_if_prod_exists_query1[1]) > int(qty)):
            qty1= int(check_if_prod_exists_query1[1]) - int(qty)
            print(qty1)
            abs(qty1)
            plus_qty = int(check_if_prod_exists_query[3]) + int(qty1)
            print("plus:", plus_qty)
            mycursor.execute("UPDATE PRODUCTS SET total_qty = " + str(plus_qty) + " WHERE prod_name = \'"+name+"\'")
        
    try:
        mydb.commit()    
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)
    mydb.close()
        
    
def sale_report():
    main = Tk()
    main.geometry('700x400')

    # Product_Category = Entry(main, width=30)
    # Product_Category.grid(row=0, column=4, padx=20)
    # Product_Category_label = Label(main, text='Products with discount')
    # Product_Category_label.grid(row=0, column=0)

    discnt_btn=Button(main, text="Check Products with discount", command=lambda:discount())
    discnt_btn.grid(row=0, column=0, columnspan=2,pady=10,padx=10,ipadx=100)

    main.mainloop()

def discount():
    main=Tk()
    main.geometry('400x400')
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")   
    query="SELECT * FROM PRODUCTS WHERE DISCOUNT_OFFER='Y' and DISCOUNT_PRICE>0"
    mycursor.execute(query)
    myresult=mycursor.fetchall()
    i=0
    for Products in myresult:
        for j in range(len(Products)):

            e = Entry(main, width =500)
            e.grid(row=i, columns=j+1)
            e.insert(END, myresult[i])
        i=i+1
    
def warehse_gui():
    main = Tk()
    main.geometry('700x400')

    Max_cap = Label(main, text="10000 total items can be stored in the warehouse")
    Max_cap.grid(row=1, column=4, padx=20)

    Max_cap_label = Label(main, text="Maximum Capacity")
    Max_cap_label.grid(row=1, column=0)

    ware_btn = Button(main, text="Current Capacity", command=lambda: warehouse())
    ware_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)

    ware_btn = Button(main, text="Send Items", command=lambda: send())
    ware_btn.grid(row=15, column=3, columnspan=2, pady=10, padx=10, ipadx=100)

    main.mainloop()

def send():
    main = Tk()
    main.geometry("700x400")
    
    send = Entry(main,width=30)
    send.grid(row=0,column=0,padx=20)

    done_btn = Button(main, text="Send Items", command=lambda: send())
    done_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="root"
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("USE BDMS")

def warehouse():
    main = Tk()
    main.geometry("400x400")

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
    query = "select SUM(total_qty) from products"
    mycursor.execute(query)
    myresult = mycursor.fetchone()

    cpcty_btn = Label(main, text="Total Items in warehouse")
    cpcty_btn.grid(row=0, column=1, columnspan=2, pady=10, padx=10, ipadx=100)
    

    x = Label(main, width=10, text="Total Items we have ")
    x.grid(row=0, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

    e = Entry(main, width =10)
    e.grid(row=1, columns=1, columnspan=2, pady=10, padx=10, ipadx=100)
    e.insert(END, myresult)

    if myresult[0] >= 10000:
        exceed_limit = Label(main, text='Storage Limit Exceeded. Please remove items', fg='red')
        exceed_limit.grid(row=6, column=1)

    mydb.close()

def view_product():
    main = Tk()
    main.geometry('700x400')

    Product_Category = Entry(main, width=30)
    Product_Category.grid(row=5, column=3, padx=20)

    Product_Category_label = Label(main, text='Category (Food/Dairy/Items)')
    Product_Category_label.grid(row=5, column=0)
    
    Product_Name = Entry(main, width=30)
    Product_Name.grid(row=6, column=3, padx=20)

    Product_Name_label = Label(main, text='Product Name')
    Product_Name_label.grid(row=6, column=0)

    view_btn = Button(main, text="View Product", command=lambda: prod_view(
        main, Product_Category, Product_Name))
    view_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)

    display_btn = Button(main, text="Inventory Report",
                         command=lambda: display())

    display_btn.grid(row=15, column=3, columnspan=2,
                     pady=10, padx=10, ipadx=100)
    # display_btn = Text(main, height=10, width=24)
    # display_btn.grid(row=2, columnspan=2)
    # Button(main, text="Display", command=lambda: (display_btn.delete(1.0, END), display_btn.insert(
    #     END, display()))).grid(row=15, column=3)

    main.mainloop()


def display():
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "SELECT * FROM PRODUCTS"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if myresult != []:
        #print(myresult[0][1])
            string=''
            for i in range(len(myresult)):
                string+=str(myresult[i][0]) + '               '+ str(myresult[i][1]) + '               ' + str(myresult[i][2])+ '               ' + str(myresult[i][3]) + '               ' + str(myresult[i][4]) + '               ' + str(myresult[i][5])+ '               ' + str(myresult[i][6]) + '               ' + str(myresult[i][7]) +' \n '
            popup=Tk()
            popup.geometry('600x600')
            popup.wm_title('Inventory Report')
            desc=Label(popup,text=' Product ID     Category        Item Name      Total Quantity    C_Price    S_Price      Dis_off    Dis_price')
            desc.grid(row=0, column=3)
            items=Label(popup,text=string)
            items.grid(row=1, column=3)
            b1=Button(popup,text='Okay',command=popup.destroy)
            b1.grid(row=2,column=3,pady=10,padx=10,ipadx=100)
            popup.mainloop()
    '''
    output = ''
    arr = ''
    arr = 'Prod Id\t\tProdCat\t\tProdNam\t\tTot_Qty\t\tC_Price\t\tS_Price\t\tDis_off\t\tDis_Price'
    print(arr)

    # myresult = myresult[0]
    for i in myresult:
        output += str(i) + '\n'
    print(output)

    # for i in myresult:
    #     output = i

    #     print(output)
    # # print(output)
    '''
    mydb.close()


def prod_view(main, Product_Category, Product_Name):
    ctgry = Product_Category.get()
    name = Product_Name.get()

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "SELECT * FROM PRODUCTS WHERE prod_category = %s AND prod_name = %s"
    # query = "SELECT * FROM PRODUCTS
    arg = (ctgry, name)
    mycursor.execute(query, arg)
    myresult = mycursor.fetchall()
    if myresult != []:
        #print(myresult[0][1])
            string=''
            for i in range(len(myresult)):
                string+=str(myresult[i][0]) + '               '+ str(myresult[i][1]) + '               ' + str(myresult[i][2])+ '               ' + str(myresult[i][3]) + '               ' + str(myresult[i][4]) + '               ' + str(myresult[i][5])+ '               ' + str(myresult[i][6]) + '               ' + str(myresult[i][7]) +' \n '
            popup=Tk()
            popup.geometry('600x300')
            popup.wm_title('Product Details')
            desc=Label(popup,text=' Product ID     Category        Item Name      Total Quantity    C_Price    S_Price      Dis_off    Dis_price')
            desc.grid(row=0, column=3)
            items=Label(popup,text=string)
            items.grid(row=1, column=3)
            b1=Button(popup,text='Okay',command=popup.destroy)
            b1.grid(row=2,column=3,pady=10,padx=10,ipadx=100)
            popup.mainloop()
    # try:
    #     mycursor.execute(query, arg)
    #     mydb.commit()
    #     main.destroy()

    # except mysql.connector.IntegrityError as err:
    #     warn_label = Label(main, text='Invalid Entry Try again')
    #     warn_label.grid(row=12, column=0)

    mydb.close()

    
    

def order_product_gui():
    main=Tk()
    main.geometry('700x400')

    Product_Name = Entry(main,width=30)
    Product_Name.grid(row=6,column=4,padx=20)
    Product_Name_label=Label(main,text='Product Name')
    Product_Name_label.grid(row=6,column=0)

    total_qty = Entry(main,width=30)
    total_qty.grid(row=7,column=4,padx=20)
    total_qty_label=Label(main,text='Total Qty of Product')
    total_qty_label.grid(row=7,column=0)
    
    add_btn=Button(main,text="Add to cart",command=lambda: order_product(main,Product_Name,total_qty))
    add_btn.grid(row=14,column=4,columnspan=2,pady=10,padx=10,ipadx=100)
    main.mainloop()

def Remove_order():
    
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
    query = "DROP TABLE ORDER"
    mycursor.execute("TRUNCATE TABLE ORDER")
    mydb.commit()
    mydb.close()

    

    

def order_product(main,Product_Name,total_qty):
    name=Product_Name.get()
    qty=total_qty.get()

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    
    mycursor = mydb.cursor(buffered=True)
    #mycursor.execute("USE BDMS")
    mycursor.execute("SELECT * FROM PRODUCTS WHERE prod_name LIKE " + "\'" + name + "\';")    
    check_if_prod_exists_query =  mycursor.fetchone()    
    sale_price= check_if_prod_exists_query[5]
    print("sale:", sale_price)
    print(check_if_prod_exists_query)
    if check_if_prod_exists_query is None:
        warn_label=Label(main,text='Product out of stock.')
        warn_label.grid(row=12,column=0)
        print("Product out of stock")
    elif int(check_if_prod_exists_query[3]) < int(qty):
        print(qty)
        print(check_if_prod_exists_query[3])
        warn_label=Label(main,text='Less quantity product available.')
        warn_label.grid(row=12,column=0)
        print("Less quantity product available")
    else:
        print("C")
        mycursor2 = mydb.cursor(buffered=True)
        query = "INSERT INTO ORDER(prod_name, total_qty, sale_price) VALUES(%s,%s,%s)"
        arg = (name, qty, sale_price)
        mycursor2.execute(query, arg)
        #mycursor1 = mydb.cursor(buffered=True)
        #mycursor1.execute("UPDATE  BDMS.ORDER INNER JOIN PRODUCTS ON ORDER.prod_name = PRODUCTS.prod_name  SET ORDER.sale_price = PRODUCTS.sale_price;")
        #................................................................................................................mycursor1.execute(query)
        minus_qty =int(check_if_prod_exists_query[4]) - int(qty)
        print(minus_qty)
        mycursor.execute("UPDATE PRODUCTS SET total_qty = " + str(minus_qty) + " WHERE prod_name = \'"+name+"\'")
        
    
    try:
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)
    mydb.close()
    

def generate_bill():
    main=Tk()
    main.geometry('700x400')
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS;")
    Product_name_label=Label(main,text='Product name')
    Product_name_label.grid(row=0,column=0)
    Product_name_label=Label(main,text='Prod_qty')
    Product_name_label.grid(row=0,column=1)
    Product_name_label=Label(main,text='Sale_price')
    Product_name_label.grid(row=0,column=2)
    query = "SELECT * FROM ORDER;"
    mycursor.execute(query)
    i=1 
    for products in mycursor: 
        for j in range(len(products)):
            e = Entry(main, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, products[j])
        i=i+1
    mydb.commit()
    mydb.close() 
    main.mainloop()
    

def generate_userReport1():
    main=Tk()
    main.geometry('700x400')
    
    User_id = Entry(main,width=30)
    User_id.grid(row=4,column=4,padx=20)
    User_id_label=Label(main,text='User ID')
    User_id_label.grid(row=4,column=0)
    
    add_btn=Button(main,text="generate user report",command=lambda: generate_userReport(User_id))
    add_btn.grid(row=14,column=4,columnspan=2,pady=10,padx=10,ipadx=100)
    
       
def generate_userReport():

    #login_username1=User_id.get()
    main=Tk()
    main.geometry('700x400')

    
    
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")
    #mycursor.execute("SELECT * FROM BDMS.LOGIN_CREDENTIALS WHERE login_username LIKE " + "\'" + login_username1 + "\'")

    #query1 = "SELECT * FROM BDMS.LOGIN_CREDENTIALS WHERE login_username LIKE " + "\'" + login_username1 + "\'""
    query = "SELECT login_username,user_role FROM LOGIN_CREDENTIALS"
    mycursor.execute(query)
    i=0 
    for LOGIN_CREDENTIALS in mycursor: 
        for j in range(len(LOGIN_CREDENTIALS)):
            e = Entry(main, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, LOGIN_CREDENTIALS[j])
        i=i+1
    #mydb.commit()
    mydb.close() 
    main.mainloop()

def add(Userid,Username,password,main,role):
    id=Userid.get()
    name=Username.get()
    p=password.get()
    r=role.get()
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
   # mycursor.execute("USE BDMS")
    
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

def edit_prod(main, Product_Category, Product_Name, total_qty, Sale_Price, Discount_offer, Discount_price):
    ctg = Product_Category.get()
    n = Product_Name.get()
    qty = total_qty.get()
    sp = Sale_Price.get()
    do = Discount_offer.get()
    dp = Discount_price.get()

    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "UPDATE PRODUCTS SET total_qty = %s, sale_price = %s, discount_offer = %s, discount_price = %s WHERE prod_category = %s AND prod_name = %s"
    arg = (qty ,sp ,do,dp, ctg, n)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Invalid entry try again')
        warn_label.grid(row=12, column=0)

    mydb.close()

def edit_product():
    main = Tk()
    main.geometry('700x400')

    Product_Category = Entry(main, width=30)
    Product_Category.grid(row=5, column=4, padx=20)
    Product_Category_label = Label(main, text='Category (Food/Dairy/Items)')
    Product_Category_label.grid(row=5, column=0)

    Product_Name = Entry(main, width=30)
    Product_Name.grid(row=6, column=4, padx=20)
    Product_Name_label = Label(main, text='Product Name')
    Product_Name_label.grid(row=6, column=0)

    total_qty = Entry(main, width=30)
    total_qty.grid(row=7, column=4, padx=20)
    total_qty_label = Label(main, text='Assign Total Qty of Product')
    total_qty_label.grid(row=7, column=0)

    Sale_Price = Entry(main, width=30)
    Sale_Price.grid(row=9, column=4, padx=20)
    Sale_Price_label = Label(main, text='New Sale Price per unit')
    Sale_Price_label.grid(row=9, column=0)

    Discount_offer = Entry(main, width=30)
    Discount_offer.grid(row=10, column=4, padx=20)
    Discount_offer_label = Label(main, text='Discount? (Y/N)')
    Discount_offer_label.grid(row=10, column=0)

    Discount_price = Entry(main, width=30)
    Discount_price.grid(row=11, column=4, padx=20)
    Discount_price_label = Label(
        main, text='Discount Price (0 means no discount)')
    Discount_price_label.grid(row=11, column=0)

    edit_btn = Button(main, text="Edit Product", command=lambda: edit_prod(
        main, Product_Category, Product_Name, total_qty, Sale_Price, Discount_offer, Discount_price))
    edit_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    main.mainloop()


def edit_mem(Userid, Username, password, main, role, N_Username, N_password):
    id = Userid.get()
    name = Username.get()
    p = password.get()
    r = role.get()
    nu = N_Username.get()
    np = N_password.get()
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "UPDATE LOGIN_CREDENTIALS SET login_username = %s, login_password = %s, user_role = %s WHERE login_id = %s AND login_password = %s AND login_username = %s"
    arg = (nu ,np ,r,id, p, name)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Invalid entry try again')
        warn_label.grid(row=12, column=0)

    mydb.close()

def edit_member():
    main = Tk()
    main.geometry('600x400')
    
    Userid = Entry(main, width=30)
    Userid.grid(row=4, column=4, padx=20)
    Userid_label = Label(main, text='User ID')
    Userid_label.grid(row=4, column=0)

    Username = Entry(main, width=30)
    Username.grid(row=5, column=4, padx=20)
    Username_label = Label(main, text='Current Username')
    Username_label.grid(row=5, column=0)

    N_Username = Entry(main, width=30)
    N_Username.grid(row=6, column=4, padx=20)
    N_Username_label = Label(main, text='New Username')
    N_Username_label.grid(row=6, column=0)

    password = Entry(main, width=30)
    password.grid(row=7, column=4, padx=20)
    password_label = Label(main, text='Current password')
    password_label.grid(row=7, column=0)

    N_password = Entry(main, width=30)
    N_password.grid(row=8, column=4, padx=20)
    N_password_label = Label(main, text='New password')
    N_password_label.grid(row=8, column=0)

    role_label = Label(main, text='Assign Role: admin or user')
    role_label.grid(row=9, column=0)
    role = Entry(main, width=30)
    role.grid(row=9, column=4, padx=20)

    edit_btn = Button(main, text="Edit Member", command=lambda: edit_mem(
        Userid, Username, password, main, role, N_Username, N_password))
    edit_btn.grid(row=10, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    main.mainloop()


def rmv_mem(Userid, Username, main, role):
    id = Userid.get()
    name = Username.get()
    r = role.get()
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="bef30b652f13a2",
    passwd="b8890586",
    database='heroku_81f4feb0eb9011c'
    )
    mycursor = mydb.cursor()
    #mycursor.execute("USE BDMS")

    query = "DELETE FROM LOGIN_CREDENTIALS WHERE login_id = %s AND login_username = %s AND user_role = %s"
    arg = (id, name, r)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Invalid Entry try again')
        warn_label.grid(row=12, column=0)

    mydb.close()

def remove_member():
    main = Tk()
    main.geometry('400x400')
    
    Userid_label = Label(main, text='User ID')
    Userid_label.grid(row=4, column=0)

    Userid = Entry(main, width=30)
    Userid.grid(row=4, column=4, padx=20)

    Username = Entry(main, width=30)
    Username.grid(row=5, column=4, padx=20)

    Username_label = Label(main, text='Username')
    Username_label.grid(row=5, column=0)

    role = Entry(main, width=30)
    role.grid(row=7, column=4, padx=20)

    role_label = Label(main, text='Role: admin or user')
    role_label.grid(row=7, column=0)

    rmv_btn = Button(main, text="Remove Member", command=lambda: rmv_mem(
        Userid, Username, main, role))
    rmv_btn.grid(row=10, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    main.mainloop()
    


def add_member():
    main = Tk()
    main.geometry('400x400')
    Userid = Entry(main, width=30)
    Userid.grid(row=4, column=4, padx=20)

    Username = Entry(main, width=30)
    Username.grid(row=5, column=4, padx=20)

    password = Entry(main, width=30)
    password.grid(row=6, column=4, padx=20)

    Userid_label = Label(main, text='User ID')
    Userid_label.grid(row=4, column=0)

    Username_label = Label(main, text='Username')
    Username_label.grid(row=5, column=0)

    password_label = Label(main, text='password')
    password_label.grid(row=6, column=0)

    role = Entry(main, width=30)
    role.grid(row=7, column=4, padx=20)

    role_label = Label(main, text='Role: admin or user')
    role_label.grid(row=7, column=0)
   
    add_btn = Button(main, text="Add Member", command=lambda: add(
        Userid, Username, password, main,role))
    add_btn.grid(row=10, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    
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

