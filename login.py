from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  |  Developed by Aakash Palliwar")
        self.root.config(bg="#fafafa")
        #========images
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)   
        
        #===Login Frame====
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login System",font=("Elephant",40,"bold"),bg='white').place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Username",font=("Elephant",15),bg='white',fg='#767171').place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()

        txt_username=Entry(login_frame,font=("times new roman",15),textvariable=self.username,bg='#ECECEC').place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Elaphant",15),bg='white',fg='#767171').place(x=50,y=200)
        txt_pass=Entry(login_frame,font=("times new roman",15),textvariable=self.password,show="*",bg='#ECECEC').place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,text="Log In",font=("Arial"),command=self.login,bg="Blue",fg='black',cursor='hand2').place(x=50,y=300,width=250,height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=360,width=250,height=2)
        or_=Label(login_frame,text="OR",bg='white',fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=345)

        btn_forget=Button(login_frame,text="Forget Password?",font=("Arial",13),bg="white",fg='#00759E',bd=0).place(x=100,y=390)
        
        #====frame 2

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="Don't have and account?",font=("times new roman",13),bg='white').place(x=40,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("Arial",13,"bold"),bg="white",fg='#00759E',bd=0).place(x=200,y=17)
        
        #======= Animation Images===
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")
        
        self.lbl_change_image=Label(self.root,bg='white')
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    
    def login(self):
        if self.username.get()=='' or self.password.get()=='':
            messagebox.showerror("Error","All feilds are required")
            
        elif self.username.get()!='Aakash' or self.password.get()!='123456':
            messagebox.showerror("Error","Invalid username and password\n try with another credential")
        else:
            messagebox.showinfo("Information",f"Welcome:{self.username.get()}\n Your Password:{self.password.get()}")
        
        
root=Tk()
obj=Login_system(root)
root.mainloop()