from tkinter import*
from PIL import ImageTk
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
        txt_username=Entry(login_frame,font=("times new roman",15),bg='#ECECEC').place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Elaphant",15),bg='white',fg='#767171').place(x=50,y=200)
        txt_pass=Entry(login_frame,font=("times new roman",15),bg='#ECECEC').place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,text="Log In",font=("Arial"),bg="Blue",fg='black',cursor='hand2').place(x=50,y=300,width=250,height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=360,width=250,height=2)
        or_=Label(login_frame,text="OR",bg='white',fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=345)

        btn_forget=Button(login_frame,text="Forget Password?",font=("Arial",13),bg="white",fg='#00759E',bd=0).place(x=100,y=390)
        
        #====frame 2

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="Don't have and account?",font=("times new roman",13),bg='white').place(x=40,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("Arial",13,"bold"),bg="white",fg='#00759E',bd=0).place(x=200,y=17)

        
root=Tk()
obj=Login_system(root)
root.mainloop()