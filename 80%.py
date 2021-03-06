from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.geometry("400x200")


# Database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

mycursor = mydb.cursor()
mycursor.execute("USE BDMS")


def login():
    # clear Text boxes
    id = Userid.get()
    p = password.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")
    query = "SELECT * FROM LOGIN_CREDENTIALS WHERE login_username=%s AND login_password=%s"
    args = (id, p)
    mycursor.execute(query, args)
    myresult = mycursor.fetchall()
    if myresult == []:
        Userid.delete(0, END)
        password.delete(0, END)
        not_exists = Label(root, text='Incorrect username or password')
        not_exists.grid(row=6, column=1)
    else:
        Userid.delete(0, END)
        password.delete(0, END)
        root.destroy()
        main_menu(myresult[0][3])

    mydb.commit()
    mydb.close()


def generate_userReport():
    main=Tk()
    main.geometry('700x400')
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    mycrsor = mydb.cursor()
    mycursor.execute("USE BDMS")
    query = "SELECT login_username,user_role FROM BDMS.LOGIN_CREDENTIALS"
    mycursor.execute(query)
    i=0 
    for LOGIN_CREDENTIALS in mycursor: 
        for j in range(len(LOGIN_CREDENTIALS)):
            e = Entry(main, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, LOGIN_CREDENTIALS[j])
    i=i+1
    mydb.commit()
    mydb.close() 
    main.mainloop()

def Remove_order():
     
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")
    query = "DROP TABLE BDMS.ORDER"
    mycursor.execute("USE BDMS")

def edit_prod(main, Product_Category, Product_Name, total_qty, Sale_Price, Discount_offer, Discount_price):
    ctg = Product_Category.get()
    n = Product_Name.get()
    qty = total_qty.get()
    sp = Sale_Price.get()
    do = Discount_offer.get()
    dp = Discount_price.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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
    

def main_menu(user_role):
    
    
    main = Tk()
    main.geometry('700x700')
    if user_role== ' admin':
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
        )

        mycursor = mydb.cursor()
        mycursor.execute("USE BDMS")
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
            popup.mainloop()
        mydb.commit()
        mydb.close()
    
    if user_role == 'admin':
        
        submit_btn = Button(main, text="Add Member", command=add_member)
        submit_btn.grid(row=0, column=10, columnspan=2,pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Remove Member",command= remove_member)
        submit_btn.grid(row=1,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Edit Member",command=edit_member)
        submit_btn.grid(row=6,column=10,columnspan=2,pady=10,padx=10,ipadx=100)
    
        submit_btn=Button(main,text="Edit Product",command=edit_product)
        submit_btn.grid(row=6,column=20,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn = Button(main, text="Add Product", command=add_product)
        submit_btn.grid(row=0, column=20, columnspan=2,
                    pady=10, padx=10, ipadx=100)

        submit_btn = Button(main, text="Remove Products", command=remove_product)
        submit_btn.grid(row=1, column=20, columnspan=2,pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Generate Userreport",command=generate_userReport)
        submit_btn.grid(row=2,column=20,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn = Button(main, text="View Product/s", command=view_product)
        submit_btn.grid(row=3, column=20, columnspan=2,
                    pady=10, padx=10, ipadx=100)

        submit_btn=Button(main,text="Generate Bill",command=generate_bill)
        submit_btn.grid(row=2,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Remove Bill",command=Remove_order)
        submit_btn.grid(row=3,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

    
        submit_btn=Button(main,text="Place Order",command=order_product_gui)
        submit_btn.grid(row=3,column=10,columnspan=2,pady=10,padx=10,ipadx=100) 
    else:
        submit_btn=Button(main,text="Generate Bill",command=generate_bill)
        submit_btn.grid(row=2,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

        submit_btn=Button(main,text="Remove Bill",command=Remove_order)
        submit_btn.grid(row=3,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

    
        submit_btn=Button(main,text="Place Order",command=order_product_gui)
        submit_btn.grid(row=4,column=10,columnspan=2,pady=10,padx=10,ipadx=100)

    main.mainloop()


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

def order_product(main,Product_Name,total_qty):
    name=Product_Name.get()
    qty=total_qty.get()

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")
    mycursor.execute("SELECT * FROM PRODUCTS WHERE prod_name LIKE " + "\'" + name + "\'")
    check_if_prod_exists_query =  mycursor.fetchone()
    print(check_if_prod_exists_query)
    if check_if_prod_exists_query is None:
        warn_label=Label(main,text='Product out of stock.')
        warn_label.grid(row=12,column=0)
        print("Product out of stock")
    elif int(check_if_prod_exists_query[4]) < int(qty):
        print(qty)
        print(check_if_prod_exists_query[4])
        warn_label=Label(main,text='Less quantity product available.')
        warn_label.grid(row=12,column=0)
        print("Less quantity product available")
        
    else:
        print("C")
        query = "INSERT INTO BDMS.ORDER(prod_name, total_qty) VALUES(%s,%s)"
        arg = (name, qty)
        mycursor.execute(query, arg)
        #print(minus_qty)
        #minus_qty =int(check_if_prod_exists_query[4]) - int(qty)
        #mycursor.execute("UPDATE PRODUCTS SET total_qty = " + int(minus_qty) + " WHERE prod_name = \'"+name+"\'")
        
    
    try:
        mydb.commit()
        main.destroy()
    
    except mysql.connector.IntegrityError as err:
        warn_label=Label(main,text='Invalid Entry Try again')
        warn_label.grid(row=12,column=0)
    

def generate_bill():
    main=Tk()
    main.geometry('700x400')
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    mycrsor = mydb.cursor()
    mycursor.execute("USE BDMS")
    
    query = "SELECT * FROM BDMS.ORDER"
    mycursor.execute(query)
    i=0 
    for products in mycursor: 
        for j in range(len(products)):
            e = Entry(main, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, products[j])
        i=i+1
    #mydb.commit()
    mydb.close() 
    main.mainloop()


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
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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
        host="localhost",
        user="root",
        passwd="root"
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

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


def add_product():
    main = Tk()
    main.geometry('700x400')

    Product_id = Entry(main, width=30)
    Product_id.grid(row=4, column=4, padx=20)
    Product_id_label = Label(main, text='Product ID')
    Product_id_label.grid(row=4, column=0)

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
    total_qty_label = Label(main, text='Total Qty of Product')
    total_qty_label.grid(row=7, column=0)

    Cost_Price = Entry(main, width=30)
    Cost_Price.grid(row=8, column=4, padx=20)
    Cost_Price_label = Label(main, text='Cost Price per unit')
    Cost_Price_label.grid(row=8, column=0)

    Sale_Price = Entry(main, width=30)
    Sale_Price.grid(row=9, column=4, padx=20)
    Sale_Price_label = Label(main, text='Sale Price per unit')
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

    #Discounted_Price = ((100-Discount_perc)/100)*Sale_Price

    add_btn = Button(main, text="Add Product", command=lambda: prod_add(
        main, Product_id, Product_Category, Product_Name, total_qty, Cost_Price, Sale_Price, Discount_offer, Discount_price))
    add_btn.grid(row=13, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    main.mainloop()


def prod_add(main, Product_id, Product_Category, Product_Name, total_qty, Cost_Price, Sale_Price, Discount_offer, Discount_price):
    id = Product_id.get()
    ctgry = Product_Category.get()
    name = Product_Name.get()
    qty = total_qty.get()
    cp = Cost_Price.get()
    sp = Sale_Price.get()
    d = Discount_offer.get()
    dp = Discount_price.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE BDMS")

    query = "INSERT INTO PRODUCTS(prod_id, prod_category, prod_name, total_qty, cost_price, sale_price, discount_offer, discount_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    arg = (id, ctgry, name, qty, cp, sp, d, dp)

    try:
        mycursor.execute(query, arg)
        mydb.commit()
        main.destroy()

    except mysql.connector.IntegrityError as err:
        warn_label = Label(main, text='Invalid Entry Try again')
        warn_label.grid(row=12, column=0)

    mydb.close()


def add(Userid, Username, password, main, role):
    id = Userid.get()
    name = Username.get()
    p = password.get()
    r = role
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
        warn_label = Label(main, text='Entry already exists')
        warn_label.grid(row=12, column=0)

    mydb.close()


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

    role_label = Label(main, text='Role: admin or user')
    role_label.grid(row=7, column=0)
   
    clicked = StringVar()
    clicked.set("Assign Role")
    
    drop=OptionMenu(main,clicked,"user","admin")
    drop.grid(row=7, column=4,columnspan=2)
    
    role=clicked.get()

    add_btn = Button(main, text="Add Member", command=lambda: add(
        Userid, Username, password, main, role,))
    add_btn.grid(row=10, column=3, columnspan=2, pady=10, padx=10, ipadx=100)
    
    main.mainloop()


Userid = Entry(root, width=30)
Userid.grid(row=4, column=4, padx=20)

password = Entry(root, width=30)
password.grid(row=5, column=4, padx=20)

# create labels

Userid_label = Label(root, text='Username')
Userid_label.grid(row=4, column=0)

password_label = Label(root, text='password')
password_label.grid(row=5, column=0)

not_exists = Label(root, text='')
not_exists.grid(row=6, column=1)

submit_btn = Button(root, text="Login", command=login)
submit_btn.grid(row=10, column=3, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()
