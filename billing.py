from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class billClass:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  |  Developed by Aakash Palliwar")
        self.root.config(bg="white")
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

        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",cursor='hand2').place(x=280,y=45,width=100,height=25)
        btn_showall=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",cursor='hand2').place(x=280,y=10,width=100,height=25)
        
         
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
        
        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)

        self.product_Table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
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
        
        Cal_Frame=Frame(Cal_Cart_Frame,bd=4,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)
        carttitle=Label(Cart_Frame,text="Cart \tTotal Product:[0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        
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
        
        self.lbl_instock=Label(Add_cartWidgetsFrame,text="In Stock [9999]",font=("times new roman",15),bg='white')
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_cartWidgetsFrame,text='Clear',font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_cartWidgetsFrame,text='ADD   |  Update Cart',font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

            
        

        
if __name__=="__main__":      
    root=Tk()
    obj=billClass(root)
    root.mainloop()