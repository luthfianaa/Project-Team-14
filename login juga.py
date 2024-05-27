import tkinter as tk
from tkinter import Frame, Canvas, Label, Entry, Checkbutton, Button, BOTH, W, X, ttk
from tkinter import messagebox




def login():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return
    # Add your validation logic here
    if username == "user" and password == "pass":  # Dummy validation
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")


def signup():
    signup_window = tk.Toplevel()
    signup_window.title("Signup")
    signup_window.geometry("900x500")
    signup_window.configure(bg="#FFFFFF")
    signup_window.resizable(False, False)

    # Frame untuk sisi kanan dengan warna gradasi
    right_frame2 = Frame(signup_window, width=450, height=500)
    right_frame2.pack(side="right", fill=BOTH)
    right_frame2.pack_propagate(False)

    canvas = Canvas(right_frame2, width=450, height=500)
    canvas.pack(fill=BOTH, expand=True)
    
    # Gradient background
    gradient = canvas.create_rectangle(0, 0, 450, 500, fill="#9EB895")
    canvas.itemconfig(gradient, outline="")
    canvas.create_text(200, 250, text="Get ready to be", font=("Barlow", 40, "bold"), fill="white")
    canvas.create_text(135, 295, text="the savior", font=("Barlow", 40, "bold"), fill="white")
    
    # Frame untuk sisi kiri
    left_frame2 = Frame(signup_window, width=450, height=500, bg="white")
    left_frame2.pack(side="left", fill=BOTH, expand=True)
    left_frame2.pack_propagate(False)

    Label(left_frame2, text="Signup", font=("Barlow", 24, "bold"), bg="white", fg="#333333").pack(pady=30)
    Label(left_frame2, text="Create a new account.", font=("Droid Serif", 12), bg="white", fg="#666666").pack(pady=5)

    # Username Entry
    username_label_signup = Label(left_frame2, text="Username", font=("Droid Serif", 12), bg="white", fg="#666666")
    username_label_signup.pack(pady=5, anchor=W, padx=30)
    username_entry_signup = Entry(left_frame2, width=30, font=("Droid Serif", 12), bd=1, relief="solid")
    username_entry_signup.pack(pady=5, padx=30)

    # Email Entry
    email_label_signup = Label(left_frame2, text="Email", font=("Droid Serif", 12), bg="white", fg="#666666")
    email_label_signup.pack(pady=5, anchor=W, padx=30)
    email_entry_signup = Entry(left_frame2, width=30, font=("Droid Serif", 12), bd=1, relief="solid")
    email_entry_signup.pack(pady=5, padx=30)

    # Password Entry
    password_label_signup = Label(left_frame2, text="Password", font=("Droid Serif", 12), bg="white", fg="#666666")
    password_label_signup.pack(pady=5, anchor=W, padx=30)
    password_entry_signup = Entry(left_frame2, width=30, font=("Droid Serif", 12), bd=1, relief="solid", show='*')
    password_entry_signup.pack(pady=5, padx=30)

   

    # Signup Button
    signup_button = Button(left_frame2, text="Signup", font=("Barlow", 14, "bold"), bg="#6C63FF", fg="white", width=25, height=2, relief="flat",
                           command=lambda: process_signup(username_entry_signup, email_entry_signup, password_entry_signup, confirm_password_entry_signup))
    signup_button.pack(pady=20)

    # Login
    signup_label = Label(left_frame2, text="Have an account? Login", font=("Arial", 10), bg="white", fg="#6C63FF", cursor="hand2")
    signup_label.pack(pady=10)
    signup_label.bind("<Button-1>", lambda e: halaman_login())

def process_signup(username_entry, email_entry, password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Signup Error", "All fields are required.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Signup Error", "Passwords do not match.")
        return
    
    # Add your signup logic here (e.g., save to database)
    messagebox.showinfo("Signup", f"Account created for {username}!")
    # You might want to close the signup window after successful signup
    # signup_window.destroy()  # Uncomment this line if you want to close the signup window

def forgot_password():
    messagebox.showinfo("Forgot Password", "Redirecting to Forgot Password Page...")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide')
    

def halaman_login():
    global username_entry, password_entry, toggle_button
    window = tk.Tk()
    window.title("Login")
    window.geometry("900x500")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    # Frame untuk sisi kiri dengan warna gradasi
    left_frame = Frame(window, width=450, height=500)
    left_frame.pack(side="left", fill=BOTH)
    left_frame.pack_propagate(False)

    canvas = Canvas(left_frame, width=450, height=500)
    canvas.pack(fill=BOTH, expand=True)
    
    # Gradient background
    gradient = canvas.create_rectangle(0, 0, 450, 500, fill="#9EB895")
    canvas.itemconfig(gradient, outline="")
    canvas.create_text(250, 250, text="Welcome Back", font=("Barlow", 40, "bold"), fill="white")
    canvas.create_text(350, 295, text="Savior", font=("Barlow", 40, "bold"), fill="white")
    
    # Frame untuk sisi kanan
    right_frame = Frame(window, width=450, height=500, bg="white")
    right_frame.pack(side="right", fill=BOTH, expand=True)
    right_frame.pack_propagate(False)

    Label(right_frame, text="Login", font=("Barlow", 24, "bold"), bg="white", fg="#333333").pack(pady=30)
    Label(right_frame, text="Welcome back! Please login to your account.", font=("Droid Serif", 12), bg="white", fg="#666666").pack(pady=5)

    # Username Entry
    username_label = Label(right_frame, text="Username", font=("Droid Serif", 12), bg="white", fg="#666666")
    username_label.pack(pady=5, anchor=W, padx=50)
    username_entry = Entry(right_frame, width=30, font=("Droid Serif", 12), bd=1, relief="solid")
    username_entry.pack(pady=5, padx=50)

    # Password Entry
    password_label = Label(right_frame, text="Password", font=("Droid Serif", 12), bg="white", fg="#666666")
    password_label.pack(pady=5, anchor=W, padx=50)
    password_entry = Entry(right_frame, width=30, font=("Droid Serif", 12), bd=1, relief="solid", show='*')
    password_entry.pack(pady=5, padx=50)

    # Toggle Password Visibility
    toggle_button = Button(right_frame, text='Show', font=("Droid Serif", 10), bg="white", fg="#6C63FF", bd=0, command=toggle_password)
    toggle_button.pack(pady=5, padx=50, anchor=W)

    # Remember Me and Forgot Password
    remember_frame = Frame(right_frame, bg="white")
    remember_frame.pack(pady=10, fill=X, padx=50)
    remember_check = Checkbutton(remember_frame, text="Remember Me", font=("Droid Serif", 10), bg="white", fg="#666666")
    remember_check.pack(side="left")
    forgot_password_link = Label(remember_frame, text="Forgot Password?", font=("Droid Serif", 10), bg="white", fg="#666666", cursor="hand2")
    forgot_password_link.pack(side="right")
    forgot_password_link.bind("<Button-1>", lambda e: forgot_password())

    # Login Button
    login_button = Button(right_frame, text="Login", font=("Barlow", 14, "bold"), bg="#6C63FF", fg="white", width=25, height=2, relief="flat", command=login)
    login_button.pack(pady=20)

    # Signup
    signup_label = Label(right_frame, text="New User? Signup", font=("Arial", 10), bg="white", fg="#6C63FF", cursor="hand2")
    signup_label.pack(pady=10)
    signup_label.bind("<Button-1>", lambda e: signup())

    window.mainloop()

halaman_login()
