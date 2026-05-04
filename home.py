from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import newUser
import mysql.connector
import Dashboard

myroot = Tk()
myroot.geometry("800x400+400+100")
myroot.title("Employee Management System")

# Background Image
bg_image = Image.open("images/Login.jpg")
bg_image = bg_image.resize((800, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(myroot, image=bg_photo)
bg_label.place(x=0, y=0)
bg_label.image = bg_photo

# ------- Login Frame ---------

# Shadow effect
shadow_frame = Frame(myroot, bg="#cfcfcf")
shadow_frame.place(x=195, y=80, width=400, height=260)

# Main card
login_frame = Frame(myroot, bg='white')
login_frame.place(x=190, y=75, width=400, height=260)

# Heading
login_heading = Label(
    login_frame,
    text="Employee Login Panel",
    font=("Segoe UI", 20, "bold"),
    bg="white",
    fg="#333"
)
login_heading.place(x=40, y=15)

# Email
email_label = Label(login_frame, text="Email", font=("Segoe UI", 11), bg="white", fg="#555")
email_label.place(x=70, y=70)

email_entry = Entry(login_frame, font=("Segoe UI", 12), width=25, bd=1, relief="solid")
email_entry.place(x=70, y=95)

# Password
password_label = Label(login_frame, text="Password", font=("Segoe UI", 11), bg="white", fg="#555")
password_label.place(x=70, y=130)

password_entry = Entry(login_frame, font=("Segoe UI", 12), width=25, bd=1, relief="solid", show="*")
password_entry.place(x=70, y=155)

def Logic_check():
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    # Validation
    if email == "":
        messagebox.showerror("Error", "Please enter email")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email format")
        return

    if password == "":
        messagebox.showerror("Error", "Please enter password")
        return

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kamal@1224",
            database="Python_GuiDb"
        )

        mycursor = mydb.cursor()

        q = "SELECT * FROM newuser WHERE email=%s AND password=%s"
        mycursor.execute(q, (email, password))

        data = mycursor.fetchone()
        if data:
            username = data[1]   # name column
            user_email = data[2] # email column
            gender = data[4]
            state = data[5]
            address = data[6]
            phone = data[8]
            dept = data[9]
            salary = data[10]
            password_entry.delete(0,END)
            email_entry.delete(0,END)
            

            Dashboard.welcome_window(myroot, username, user_email,
                                    gender, state, address,
        phone, dept, salary)
        else:
            messagebox.showerror("Error", "Invalid Email or Password")        

        mycursor.close()
        mydb.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
     

# Login Button
login_button = Button(
    login_frame,
    text="Login",
    font=("Segoe UI", 11, "bold"),
    bg="#4a90e2",
    fg="white",
    activebackground="#357ABD",
    cursor="hand2",
    command=Logic_check,
    bd=0,
    width=12
)
login_button.place(x=60, y=205)

# New User Button
new_user_button = Button(
    login_frame,
    text="Add Employee",
    font=("Segoe UI", 11, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    cursor="hand2",
    bd=0,
    width=12
)
new_user_button.place(x=200, y=205)

new_user_button.bind("<Button-1>", lambda k: newUser.signup(myroot))

myroot.mainloop()