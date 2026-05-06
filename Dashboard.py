from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import newUser


def welcome_window(root, username, emailid,
                   gender, state, address,
                   phone, dept, salary):

    root.withdraw()

    win = Toplevel(root)
    win.geometry("800x450+400+100")
    win.title("Employee Dashboard")
    win.resizable(False, False)

    # -------- MAIN WINDOW COLOR --------
    win.configure(bg="#ecf0f1")

    # -------- ICONS --------
    user_img = Image.open("images/user.png").resize((20, 20))
    user_icon = ImageTk.PhotoImage(user_img)

    mail_img = Image.open("images/mail.png").resize((20, 20))
    mail_icon = ImageTk.PhotoImage(mail_img)

    # -------- FUNCTIONS --------
    def logout():
        win.destroy()
        root.deiconify()

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    def show_home():
        clear_content()
        Label(content, text=f"Welcome, {username}",
              font=("Segoe UI", 20, "bold"),
              bg="white").pack(pady=80)

    def show_profile():
        clear_content()

        Label(content, text="My Profile",
              font=("Segoe UI", 20, "bold"),
              bg="white", fg="#2c3e50").pack(pady=15)

        card = Frame(content, bg="#f8f9fa", bd=1, relief="solid")
        card.pack(padx=40, pady=10)

        def row(label, value):
            row_frame = Frame(card, bg="#f8f9fa")
            row_frame.pack(fill="x", padx=20, pady=5)

            Label(row_frame, text=label,
                  font=("Segoe UI", 11, "bold"),
                  bg="#f8f9fa", fg="#333", width=12, anchor="w").pack(side="left")

            Label(row_frame, text=value,
                  font=("Segoe UI", 11),
                  bg="#f8f9fa", fg="#555").pack(side="left")

        row("Name", username)
        row("Email", emailid)
        row("Phone", phone)
        row("Department", dept)
        row("Salary", salary)
        row("State", state)
        row("Address", address)
        row("Gender", gender)

    def show_edit():
        clear_content()

        Label(content, text="Edit Profile",
              font=("Segoe UI", 18, "bold"),
              bg="white").pack(pady=10)

        Entry(content).pack(pady=5)
        Entry(content).pack(pady=5)

        Button(content, text="Save").pack(pady=10)

    def show_complaint():
        clear_content()

        Label(content, text="Raise Complaint",
              font=("Segoe UI", 18, "bold"),
              bg="white").pack(pady=10)

        Entry(content).pack(pady=5)
        Text(content, height=5).pack(pady=5)

        Button(content, text="Submit").pack(pady=10)

    # -------- MENU BAR --------
    menubar = Menu(win)

    # FILE MENU
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Logout", command=logout)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=win.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    # EMPLOYEE MENU
    emp_menu = Menu(menubar, tearoff=0)
    emp_menu.add_command(label="Add Employee", command=lambda: newUser.signup(win))
    emp_menu.add_separator()
    emp_menu.add_command(label="My Profile", command=show_profile)
    emp_menu.add_separator()
    emp_menu.add_command(label="Edit Profile", command=show_edit)
    menubar.add_cascade(label="Employee", menu=emp_menu)

    # HELP MENU
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="About",
        command=lambda: messagebox.showinfo(
            "About", "Employee Management System\nVersion 1.0"))
    menubar.add_cascade(label="Help", menu=help_menu)

    win.config(menu=menubar)

    # -------- TOP BAR --------
    top = Frame(win, bg="#ecf0f1", height=50)
    top.pack(fill="x")

    Label(top, image=user_icon, text=f" Welcome, {username}",
          compound="left",
          font=("Segoe UI", 14, "bold"),
          bg="#ecf0f1").pack(side="left", padx=10)

    Label(top, image=mail_icon, text=f" {emailid}",
          compound="left",
          font=("Segoe UI", 10),
          bg="#ecf0f1").pack(side="right", padx=10)

    top.user_icon = user_icon
    top.mail_icon = mail_icon

    # -------- MAIN AREA --------
    main = Frame(win, bg="#ecf0f1")
    main.pack(fill="both", expand=True)

    # SIDEBAR
    sidebar = Frame(main, bg="#2c3e50", width=180)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    # CONTENT
    content = Frame(main, bg="white")
    content.pack(side="left", fill="both", expand=True)

    # -------- SIDEBAR BUTTONS --------
    Button(sidebar, text="My Profile",
           width=20, bg="#34495e", fg="white",
           command=show_profile).pack(pady=10)

    Button(sidebar, text="Edit Profile",
           width=20, bg="#34495e", fg="white",
           command=show_edit).pack(pady=10)

    Button(sidebar, text="Add Employee",
           width=20, bg="#34495e", fg="white",
           command=lambda: newUser.signup(win)).pack(pady=10)

    Button(sidebar, text="Complaint",
           width=20, bg="#34495e", fg="white",
           command=show_complaint).pack(pady=10)

    Button(sidebar, text="Logout",
           width=20, bg="red", fg="white",
           command=logout).pack(pady=20)

    # -------- DEFAULT --------
    show_home()