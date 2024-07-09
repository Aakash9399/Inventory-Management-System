from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class billClass:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  |  Developed by Aakash Palliwar")
        self.root.config(bg="white")
        self.cart_list=[]
        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)   
        #button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="Yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management \t\t Date:DD-MM-YYYY \t\t Time:HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30) 
        
        #===== product frame====
        
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
        ptitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg='white').pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text='Search Product | By Name',font=('times new roman',15,"bold"),bg='white',fg='green').place(x=2,y=5)
        
        lbl_search=Label(ProductFrame2,text="Product Name",font=('times new roman',15,"bold"),bg='white').place(x=2,y=45)
        
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=('times new roman',15),bg='lightyellow').place(x=120,y=47,width=150,height=22)

        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",cursor='hand2').place(x=280,y=45,width=100,height=25)
        btn_showall=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",cursor='hand2').place(x=280,y=10,width=100,height=25)
        
         
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)
        
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        
        
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="NAME")
        self.product_Table.heading("price",text="PRICE")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="STATUS")

        
        
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)

        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 quantity to remove product from the cart'",font=("goudy old style",14),anchor='w',bg="white",fg="red" ).pack(side=BOTTOM,fill=X)

        #====== customer frame=====
        
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        
        ctitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text='Name',font=('times new roman',15),bg='white').place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=('times new roman',13),bg='lightyellow').place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame,text='Contact',font=('times new roman',15),bg='white').place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=('times new roman',13),bg='lightyellow').place(x=340,y=35,width=170)
        
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        
        # calculator=====
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold",),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=2,pady=14,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=2,pady=14,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=2,pady=14,cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=2,pady=14,cursor='hand2').grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=2,pady=14,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=2,pady=14,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=2,pady=14,cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=2,pady=14,cursor='hand2').grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=2,pady=14,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=2,pady=14,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=2,pady=14,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=2,pady=14,cursor='hand2').grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=2,pady=14,cursor='hand2').grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=2,pady=14,cursor='hand2').grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=2,pady=14,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=2,pady=14,cursor='hand2').grid(row=4,column=3)       


        
        
        
        
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)
        self.carttitle=Label(Cart_Frame,text="Cart \tTotal Product:[0]",font=("goudy old style",15),bg="lightgray")
        self.carttitle.pack(side=TOP,fill=X)

        
        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        
        self.Cart_Table=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)

        
        
        self.Cart_Table.heading("pid",text="PID")
        self.Cart_Table.heading("name",text="NAME")
        self.Cart_Table.heading("price",text="PRICE")
        self.Cart_Table.heading("qty",text="QTY")
        self.Cart_Table.heading("status",text="STATUS")

        
        
        self.Cart_Table["show"]="headings"
        
        self.Cart_Table.column("pid",width=40)
        self.Cart_Table.column("name",width=100)
        self.Cart_Table.column("price",width=90)
        self.Cart_Table.column("qty",width=30)
        self.Cart_Table.column("status",width=90)

        self.Cart_Table.pack(fill=BOTH,expand=1)
        #self.Cart_Table.bind("<ButtonRelease-1>",self.get_data)
        
        
        #====menu frame====ADD CART buttons
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_stock=StringVar()


        Add_cartWidgetsFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Add_cartWidgetsFrame.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name=Label(Add_cartWidgetsFrame,text="Product Name",font=("times new roman",15),bg='white').place(x=5,y=5)
        txt_p_name=Entry(Add_cartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg='lightyellow',state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(Add_cartWidgetsFrame,text="Price per Qty",font=("times new roman",15),bg='white').place(x=230,y=5)
        txt_p_price=Entry(Add_cartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg='lightyellow',state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_cartWidgetsFrame,text="Quantity",font=("times new roman",15),bg='white').place(x=390,y=5)
        txt_p_qty=Entry(Add_cartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg='lightyellow',).place(x=390,y=35,width=120,height=22)
        
        self.lbl_instock=Label(Add_cartWidgetsFrame,text="In Stock",font=("times new roman",15),bg='white')
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_cartWidgetsFrame,text='Clear',font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_cartWidgetsFrame,text='ADD  |  Update Cart',command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)


        #================billing area=====
        
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)
        
        btitle=Label(billFrame,text="Customer Bill Area ",font=("goudy old style",20,"bold"),bg='#f44336',fg='white').pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #=====Billing buttons=====
        billmenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billmenuFrame.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amnt=Label(billmenuFrame,text='Bill Amount\n[0]',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white')
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billmenuFrame,text='Discount\n[5%]',font=('goudy old style',15,'bold'),bg='#8bc34a',fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(billmenuFrame,text='Net Pay\n[0]',font=('goudy old style',15,'bold'),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(billmenuFrame,text='print',font=('goudy old style',15,'bold'),bg='lightgreen',cursor='hand2')
        btn_print.place(x=2,y=80,width=120,height=50)
        
        btn_clear_all=Button(billmenuFrame,text='Clear All',font=('goudy old style',15,'bold'),bg='gray',cursor='hand2')
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        
        btn_generate=Button(billmenuFrame,text='Generate/Save Bill',font=('goudy old style',15,'bold'),bg='#009688',cursor='hand2')
        btn_generate.place(x=246,y=80,width=160,height=50)
        
        #=======footer=====
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by Aakash Palliwar\n For any Technical issue Contact:9399866672",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.show()
        #===== All functions=====
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))      
        
        
        
    def show(self):
        con= sqlite3.connect(database=r'ims.db1')
        cur=con.cursor()    
        try:

            cur.execute("select pid,name,price,qty,status from product")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def search(self):
        con= sqlite3.connect(database=r'ims.db1')
        cur=con.cursor()    
        try:
            
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:   
                cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error",f"No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root) 
            
    def get_data(self, ev):
         f=self.product_Table.focus()
         content=(self.product_Table.item(f))
         row=content['values'] 
         self.var_pid.set(row[0])
         self.var_pname.set(row[1])
         self.var_price.set(row[2])
         self.lbl_instock.config(text=f"In Stock[{str(row[3])}]")
         
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)

        elif self.var_qty=="":
            messagebox.showerror('Error',"Quantity is Rquired",parent=self.root)
        else:
            price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get() ]
            
            #====update cart======
            present='no'
            index_=-0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm','Product already present\nDo you want to Update | Remove from the Cart list',parent=self.root)  
                if op==True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get() #quantity
                        
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
    
    
    def bill_updates(self):
        bill_amnt=0
        net_pay=0
        for row in self.cart_list:
            bill_amnt=bill_amnt+float(row[2])
        net_pay=bill_amnt-((bill_amnt*5)/100)
        self.lbl_amnt.config(text=f"Bill Amnt.(Rs.)\n[{str(bill_amnt)}]")
        self.lbl_net_pay.config(text=f"Net Amount(Rs.)\n[{str(net_pay)}]")
        self.carttitle.config(text=f"Cart \tTotal Product: [{str(len(self.cart_list))}]")

                 
            
    
    def show_cart(self):    
        try:
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
       
if __name__=="__main__":      
    root=Tk()
    obj=billClass(root)
    root.mainloop()