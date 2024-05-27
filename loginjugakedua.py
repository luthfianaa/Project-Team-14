import tkinter as tk
from tkinter import Frame, Canvas, Label, Entry, Checkbutton, Button, BOTH, W, X, ttk
from tkinter import messagebox


filename = open("Project-Team-14/database.csv")

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
    global signup_screen, username_entry_signup, password_entry_signup

    window.destroy()
    signup_screen = tk.Tk()
    signup_screen.title("Signup")
    signup_screen.geometry("900x500")
    signup_screen.configure(bg="#FFFFFF")
    signup_screen.resizable(False, False)

    # Frame untuk sisi kanan dengan warna gradasi
    right_frame2 = Frame(signup_screen, width=450, height=500)
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
    left_frame2 = Frame(signup_screen, width=450, height=500, bg="white")
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
    email_label_signup = Label(left_frame2, text="Password", font=("Droid Serif", 12), bg="white", fg="#666666")
    email_label_signup.pack(pady=5, anchor=W, padx=30)
    email_entry_signup = Entry(left_frame2, width=30, font=("Droid Serif", 12), bd=1, relief="solid")
    email_entry_signup.pack(pady=5, padx=30)

    # Password Entry
    password_label_signup = Label(left_frame2, text="Confirm Password", font=("Droid Serif", 12), bg="white", fg="#666666")
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

    signup_screen.mainloop()

def sign_up():
    global username2
    username2 = username_entry_signup.get()
    password2 = password_entry_signup.get()
    with open(filename, "r") as file1:
        for i in file1:
            z = 0
            a,b = i.split(",")
            b = b.strip()
            
            if username2 == "" or username2 == "Username" or password2 == "" or password2 == "Password":
                messagebox.showinfo("Error", "Username/Password tidak boleh kosong \nSilahkan isi Username dan Password")
                break
            elif username2 == a:
                messagebox.showinfo("Error", "Username sudah digunakan silahkan ganti username")
                break
            else:
                z += 1
        if z == len(i[0]):
            with open(filename, "a") as file:
                file.write(f"{username2},{password2}\n")
            os.makedirs(f"Project-Kelompok-11/database/{username2}", exist_ok=True)
            
            messagebox.showinfo("Berhasil", "Username dan Password telah diregristrasi")
            signup_screen.destroy()
            halaman_login()
    
# Function to handle login
def login():
    global username
    username = username_entry.get()
    password = password_entry.get()
    c = 0
    
    if username == "" or username == "Username" or password == "" or password == "Password":
        messagebox.showinfo("Error", "Username/Password tidak boleh kosong \nSilahkan isi username")
    else:
        with open(filename, "r") as file:
            for i in file:
                c += 1
                a,b = i.split(",")
                b = b.strip()
                
                if a == username and b == password:
                    window.destroy()
                    messagebox.showinfo("Berhasil", "Login sukses")
                    break
            else:
                messagebox.showinfo("Error", "Akun tidak ditemukan")


def back_login():
    signup_screen.destroy()
    halaman_login()

def halaman_login():
    global username_entry, password_entry, toggle_button, window

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
    login_button = Button(right_frame, text="Login", font=("Barlow", 14, "bold"), bg="#6C63FF", fg="white", width=25, height=2, relief="flat", command=back_login)
    login_button.pack(pady=20)

    # Signup
    signup_label = Label(right_frame, text="New User? Signup", font=("Arial", 10), bg="white", fg="#6C63FF", cursor="hand2")
    signup_label.pack(pady=10)
    signup_label.bind("<Button-1>", lambda e: signup())

    window.mainloop()

halaman_login()
