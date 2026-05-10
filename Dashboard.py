from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


def welcome_window(root, username, emailid,
                   gender, state, address,
                   phone, dept, salary):

    root.withdraw()

    win = Toplevel(root)
    win.geometry("900x550+300+80")
    win.title("Employee Dashboard")
    win.resizable(False, False)

    # -------- WINDOW BG --------
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

    # -------- HOME --------
    def show_home():

        clear_content()

        Label(
            content,
            text=f"Welcome, {username}",
            font=("Segoe UI", 24, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        ).pack(pady=180)

    # -------- PROFILE --------
    def show_profile():

        clear_content()

        Label(
            content,
            text="My Profile",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        ).pack(pady=15)

        card = Frame(
            content,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(pady=10)

        def row(label, value):

            row_frame = Frame(card, bg="white")
            row_frame.pack(fill="x", padx=20, pady=8)

            Label(
                row_frame,
                text=label,
                font=("Segoe UI", 11, "bold"),
                bg="white",
                fg="#2c3e50",
                width=14,
                anchor="w"
            ).pack(side="left")

            Label(
                row_frame,
                text=value,
                font=("Segoe UI", 11),
                bg="white",
                fg="#555"
            ).pack(side="left")

        row("Name", username)
        row("Email", emailid)
        row("Phone", phone)
        row("Department", dept)
        row("Salary", salary)
        row("State", state)
        row("Address", address)
        row("Gender", gender)

    # -------- ADD EMPLOYEE --------
    def show_add_employee():

        clear_content()

        Label(
            content,
            text="Add Employee",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        ).pack(pady=15)

        form_card = Frame(
            content,
            bg="white",
            bd=1,
            relief="solid"
        )

        form_card.place(
            x=130,
            y=70,
            width=450,
            height=420
        )

        # Entries
        name_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid"
        )

        email_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid"
        )

        password_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid",
            show="*"
        )

        phone_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid"
        )

        dept_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid"
        )

        salary_entry = Entry(
            form_card,
            font=("Segoe UI", 11),
            width=25,
            bd=1,
            relief="solid"
        )

        address_box = Text(
            form_card,
            font=("Segoe UI", 10),
            width=25,
            height=3,
            bd=1,
            relief="solid"
        )

        gender_var = StringVar(value="Male")
        state_var = StringVar(value="Select State")

        # Row Function
        def row(y, text, widget):

            Label(
                form_card,
                text=text,
                bg="white",
                fg="#2c3e50",
                font=("Segoe UI", 10, "bold"),
                width=12,
                anchor="w"
            ).place(x=30, y=y)

            widget.place(x=170, y=y)

        row(30, "Name", name_entry)
        row(70, "Email", email_entry)
        row(110, "Password", password_entry)
        row(150, "Phone", phone_entry)
        row(190, "Department", dept_entry)
        row(230, "Salary", salary_entry)

        # Gender
        Label(
            form_card,
            text="Gender",
            bg="white",
            fg="#2c3e50",
            font=("Segoe UI", 10, "bold"),
            width=12,
            anchor="w"
        ).place(x=30, y=270)

        Radiobutton(
            form_card,
            text="Male",
            variable=gender_var,
            value="Male",
            bg="white"
        ).place(x=170, y=270)

        Radiobutton(
            form_card,
            text="Female",
            variable=gender_var,
            value="Female",
            bg="white"
        ).place(x=250, y=270)

        # State
        Label(
            form_card,
            text="State",
            bg="white",
            fg="#2c3e50",
            font=("Segoe UI", 10, "bold"),
            width=12,
            anchor="w"
        ).place(x=30, y=310)

        OptionMenu(
            form_card,
            state_var,
            "Select State",
            "Himachal Pradesh",
            "Delhi",
            "Haryana",
            "Rajasthan",
            "Chhattisgarh"
        ).place(x=170, y=305)

        # Address
        Label(
            form_card,
            text="Address",
            bg="white",
            fg="#2c3e50",
            font=("Segoe UI", 10, "bold"),
            width=12,
            anchor="w"
        ).place(x=30, y=350)

        address_box.place(x=170, y=340)

        # SAVE FUNCTION
        def save_user():

            name = name_entry.get().strip()
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            phone = phone_entry.get().strip()
            dept = dept_entry.get().strip()
            salary = salary_entry.get().strip()

            address = address_box.get(
                "1.0",
                END
            ).strip()

            gender = gender_var.get()
            state = state_var.get()

            if not name:
                messagebox.showerror(
                    "Error",
                    "Name Required"
                )
                return

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Kamal@1224",
                    database="Python_GuiDb"
                )

                cursor = db.cursor()

                q = """
                INSERT INTO newuser
                (name,email,password,gender,state,address,phone,department,salary)

                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                cursor.execute((
                    q
                ), (

                    name,
                    email,
                    password,
                    gender,
                    state,
                    address,
                    phone,
                    dept,
                    salary

                ))

                db.commit()

                messagebox.showinfo(
                    "Success",
                    "Employee Added Successfully"
                )

                cursor.close()
                db.close()

                show_add_employee()

            except Exception as e:

                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

        Button(
            form_card,
            text="Add",
            bg="#2ecc71",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=10,
            bd=0,
            cursor="hand2",
            command=save_user
        ).place(x=345, y=365)

    # -------- DELETE EMPLOYEE --------
    def show_delete_employee():

        clear_content()

        Label(
            content,
            text="Delete Employee",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f6f7",
            fg="red"
        ).pack(pady=20)

        employee_list = Listbox(
            content,
            font=("Segoe UI", 11),
            width=50,
            height=15,
            bd=1,
            relief="solid"
        )

        employee_list.pack(pady=10)

        try:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kamal@1224",
                database="Python_GuiDb"
            )

            mycursor = mydb.cursor()

            q = """
            SELECT Sno, name, email
            FROM newuser
            WHERE email != %s
            """

            mycursor.execute(q, (emailid,))

            employees = mycursor.fetchall()

            for emp in employees:

                employee_list.insert(
                    END,
                    f"ID: {emp[0]} | {emp[1]} | {emp[2]}"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

        def delete_selected():

            selected = employee_list.curselection()

            if not selected:

                messagebox.showerror(
                    "Error",
                    "Select Employee"
                )

                return

            data = employee_list.get(selected[0])

            emp_id = data.split("|")[0]
            emp_id = emp_id.replace("ID:", "").strip()

            confirm = messagebox.askyesno(
                "Confirm",
                "Delete this employee?"
            )

            if confirm:

                try:

                    q = "DELETE FROM newuser WHERE Sno=%s"

                    mycursor.execute(q, (emp_id,))

                    mydb.commit()

                    messagebox.showinfo(
                        "Success",
                        "Employee Deleted"
                    )

                    show_delete_employee()

                except Exception as e:
                    messagebox.showerror(
                        "Error",
                        str(e)
                    )

        Button(
            content,
            text="Delete Employee",
            bg="red",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=20,
            bd=0,
            cursor="hand2",
            command=delete_selected
        ).pack(pady=10)

    # -------- COMPLAINT --------
    def show_complaint():

        clear_content()

        Label(
            content,
            text="Raise Complaint",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        ).pack(pady=20)

        Entry(
            content,
            width=40,
            font=("Segoe UI", 11)
        ).pack(pady=10)

        Text(
            content,
            height=6,
            width=42,
            font=("Segoe UI", 10)
        ).pack(pady=10)

        Button(
            content,
            text="Submit",
            bg="#3498db",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=20,
            bd=0
        ).pack(pady=10)

    # -------- TOP BAR --------
    top = Frame(win, bg="#dfe6e9", height=50)
    top.pack(fill="x")

    Label(
        top,
        image=user_icon,
        text=f" Welcome, {username}",
        compound="left",
        font=("Segoe UI", 16, "bold"),
        bg="#dfe6e9"
    ).pack(side="left", padx=15)

    Label(
        top,
        image=mail_icon,
        text=f" {emailid}",
        compound="left",
        font=("Segoe UI", 11),
        bg="#dfe6e9"
    ).pack(side="right", padx=15)

    top.user_icon = user_icon
    top.mail_icon = mail_icon

    # -------- MAIN AREA --------
    main = Frame(win, bg="#ecf0f1")
    main.pack(fill="both", expand=True)

    # -------- SIDEBAR --------
    sidebar = Frame(main, bg="#2c3e50", width=220)
    sidebar.pack(side="left", fill="y")

    sidebar.pack_propagate(False)

    # -------- CONTENT --------
    content = Frame(main, bg="#f4f6f7")
    content.pack(side="left", fill="both", expand=True)

    # -------- BUTTONS --------
    Button(
        sidebar,
        text="My Profile",
        width=20,
        height=2,
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        cursor="hand2",
        command=show_profile
    ).pack(pady=12)

    Button(
        sidebar,
        text="Add Employee",
        width=20,
        height=2,
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        cursor="hand2",
        command=show_add_employee
    ).pack(pady=12)

    Button(
        sidebar,
        text="Delete Employee",
        width=20,
        height=2,
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        cursor="hand2",
        command=show_delete_employee
    ).pack(pady=12)

    Button(
        sidebar,
        text="Complaint",
        width=20,
        height=2,
        bg="#34495e",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        cursor="hand2",
        command=show_complaint
    ).pack(pady=12)

    Button(
        sidebar,
        text="Logout",
        width=20,
        height=2,
        bg="red",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        bd=0,
        cursor="hand2",
        command=logout
    ).pack(pady=20)

    # -------- DEFAULT --------
    show_home()