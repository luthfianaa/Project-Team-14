import customtkinter as ctk
from tkinter import messagebox
import csv
import os

# Setup file CSV
CSV_FILE = 'users.csv'

def create_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'email', 'password'])

create_csv()

ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")  

def login():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return
    
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                nama_pengguna = row['username']  # Ambil nama pengguna dari baris yang sesuai
                show_slideshow_app(nama_pengguna)  # Teruskan nama pengguna ke fungsi show_slideshow_app() 
                return
        messagebox.showerror("Login Error", "Invalid username or password.")

def show_slideshow_app(nama_pengguna):
    global window
    window.destroy()  
    from homepage import SlideShowApp
    app = SlideShowApp(nama_pengguna)  # Teruskan nama pengguna ke SlideShowApp
    app.mainloop()

def process_signup(username_entry, email_entry, password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not username or not email or not password:
        messagebox.showerror("Signup Error", "All fields are required.")
        return
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password])
        messagebox.showinfo("Signup", f"Account created for {username}!")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Redirecting to Forgot Password Page...")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
        toggle_button.configure(text='Show')
    else:
        password_entry.configure(show='')
        toggle_button.configure(text='Hide')

def halaman_login():
    global username_entry, password_entry, toggle_button, window
    if 'signup_window' in globals():
        signup_window.destroy()
    window = ctk.CTk()
    window.title("Login")
    window.geometry("900x500")
    window.resizable(1440, 900)

    # Frame untuk sisi kiri dengan warna gradasi
    left_frame = ctk.CTkFrame(window, width=600, height=500, fg_color=("white", "#9EB895"))
    left_frame.pack(side="left", fill="both", expand=True)

    canvas = ctk.CTkCanvas(left_frame, width=450, height=500)
    canvas.pack(fill="both", expand=True)
    
    # Gradient background
    gradient = canvas.create_rectangle(0, 0, 900, 1200, fill="#9EB895")
    canvas.itemconfig(gradient, outline="")
    canvas.create_text(520, 450, text="Welcome Back", font=("Barlow", 70, "bold"), fill="white")
    canvas.create_text(700, 525, text="Savior", font=("Barlow", 70, "bold"), fill="white")
    
    # Frame untuk sisi kanan
    right_frame = ctk.CTkFrame(window, width=450, height=500, fg_color="white")
    right_frame.pack(side="right", fill="both", expand=True)

    ctk.CTkLabel(right_frame, text="Login", font=("Barlow", 24, "bold"), text_color="#333333").pack(pady=30)
    ctk.CTkLabel(right_frame, text="Welcome back! Please login to your account.", font=("Droid Serif", 12), text_color="#666666").pack(pady=5)

    # Username Entry
    username_label = ctk.CTkLabel(right_frame, text="Username", font=("Droid Serif", 14), text_color="#666666")
    username_label.pack(pady=5, anchor="w", padx=50)
    username_entry = ctk.CTkEntry(right_frame, width=300, font=("Droid Serif", 12))
    username_entry.pack(pady=5, padx=50)

    # Password Entry
    password_label = ctk.CTkLabel(right_frame, text="Password", font=("Droid Serif", 14), text_color="#666666")
    password_label.pack(pady=5, anchor="w", padx=50)
    password_entry = ctk.CTkEntry(right_frame, width=300, font=("Droid Serif", 12), show='*')
    password_entry.pack(pady=5, padx=50)

    # Toggle Password Visibility
    toggle_button = ctk.CTkButton(right_frame, text='Show', font=("Droid Serif", 10), text_color="White", command=toggle_password)
    toggle_button.pack(pady=5, padx=50, anchor="w")

    # Remember Me and Forgot Password
    remember_frame = ctk.CTkFrame(right_frame, fg_color="white")
    remember_frame.pack(pady=10, fill="x", padx=50)                                 
    remember_check = ctk.CTkCheckBox(remember_frame, text="Remember Me", font=("Droid Serif", 10), text_color="#666666", corner_radius=20)
    remember_check.pack(side="left")
    forgot_password_link = ctk.CTkLabel(remember_frame, text="Forgot Password?", font=("Droid Serif", 10), text_color="#666666", cursor="hand2")
    forgot_password_link.pack(side="right")
    forgot_password_link.bind("<Button-1>", lambda e: forgot_password())

    # Login Button
    login_button = ctk.CTkButton(right_frame, text="Login", font=("Barlow", 14, "bold"), width=300, height=40, fg_color="#6C63FF", text_color="white", command=login)
    login_button.pack(pady=20)
    
    # Signup
    signup_label = ctk.CTkLabel(right_frame, text="New User? Signup", font=("Arial", 10), text_color="#6C63FF", cursor="hand2")
    signup_label.pack(pady=10)
    signup_label.bind("<Button-1>", lambda e: signup())

    window.mainloop()

def signup():
    global signup_window
    if 'window' in globals():
        window.destroy()
    signup_window = ctk.CTkToplevel()
    signup_window.title("Signup")
    signup_window.geometry("900x500")
    signup_window.resizable(1440, 900)
    

    # Frame untuk sisi kanan dengan warna gradasi
    right_frame2 = ctk.CTkFrame(signup_window, width=600, height=500, fg_color=("white", "#9EB895"))
    right_frame2.pack(side="right", fill="both", expand=True)

    canvas = ctk.CTkCanvas(right_frame2, width=450, height=500)
    canvas.pack(fill="both", expand=True)
    
    # Gradient background
    gradient = canvas.create_rectangle(0, 0, 900, 1200, fill="#9EB895")
    canvas.itemconfig(gradient, outline="")
    canvas.create_text(360, 500, text="Get ready to be", font=("Barlow", 70, "bold"), fill="white")
    canvas.create_text(240, 575, text="the savior", font=("Barlow", 70, "bold"), fill="white")
    
    # Frame untuk sisi kiri
    left_frame2 = ctk.CTkFrame(signup_window, width=450, height=500, fg_color="white")
    left_frame2.pack(side="left", fill="both", expand=True)

    ctk.CTkLabel(left_frame2, text="Signup", font=("Barlow", 24, "bold"), text_color="#333333").pack(pady=30)
    ctk.CTkLabel(left_frame2, text="Create a new account.", font=("Droid Serif", 12), text_color="#666666").pack(pady=5)

    # Username Entry
    username_label_signup = ctk.CTkLabel(left_frame2, text="Username", font=("Droid Serif", 12), text_color="#666666")
    username_label_signup.pack(pady=5, anchor="w", padx=30)
    username_entry_signup = ctk.CTkEntry(left_frame2, width=300, font=("Droid Serif", 12))
    username_entry_signup.pack(pady=5, padx=30)

    # Email Entry
    email_label_signup = ctk.CTkLabel(left_frame2, text="Email", font=("Droid Serif", 12), text_color="#666666")
    email_label_signup.pack(pady=5, anchor="w", padx=30)
    email_entry_signup = ctk.CTkEntry(left_frame2, width=300, font=("Droid Serif", 12))
    email_entry_signup.pack(pady=5, padx=30)

    # Password Entry
    password_label_signup = ctk.CTkLabel(left_frame2, text="Password", font=("Droid Serif", 12), text_color="#666666")
    password_label_signup.pack(pady=5, anchor="w", padx=30)
    password_entry_signup = ctk.CTkEntry(left_frame2, width=300, font=("Droid Serif", 12), show='*')
    password_entry_signup.pack(pady=5, padx=30)

    # Signup Button
    signup_button = ctk.CTkButton(left_frame2, text="Signup", font=("Barlow", 14, "bold"), width=300, height=40, fg_color="#6C63FF", text_color="white",
                           command=lambda: process_signup(username_entry_signup, email_entry_signup, password_entry_signup))
    signup_button.pack(pady=20)

    # Login
    signup_label = ctk.CTkLabel(left_frame2, text="Have an account? Login", font=("Arial", 10), text_color="#6C63FF", cursor="hand2")
    signup_label.pack(pady=10)
    signup_label.bind("<Button-1>", lambda e: halaman_login())

halaman_login()
