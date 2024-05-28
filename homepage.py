# File: homepage.py
import customtkinter as ctk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class SlideShowApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()

        self.username = username
        
        self.geometry("800x500")
        self.title("WeCan")

        # Set appearance mode
        ctk.set_appearance_mode("light")  # "light", "dark", or system
        ctk.set_default_color_theme("blue")  

        # Top frame
        top_frame = ctk.CTkFrame(self, height=40, width=800, corner_radius=0, fg_color="#9EB895")
        top_frame.place(relwidth=1, y=0)

        logo_orang = Image.open("foto2/profile_icon1.png")
        logo_orang = logo_orang.resize((50, 43), Image.LANCZOS)  
        self.logo_orang = ImageTk.PhotoImage(logo_orang)
        logo_label_orang = ctk.CTkLabel(top_frame, image=self.logo_orang)
        logo_label_orang.pack(side="left", pady=0, padx=5, anchor="w")
        profile_name = ctk.CTkLabel(top_frame, text=self.username, font=("Arial", 14))
        profile_name.place(x=50, y=10)

        logo_wecan = Image.open("foto2/wecan.png")  
        logo_wecan = logo_wecan.resize((200, 50), Image.LANCZOS)  
        self.logo_wecan = ImageTk.PhotoImage(logo_wecan)
        logo_logo_wecan = ctk.CTkLabel(top_frame, image=self.logo_wecan)
        logo_logo_wecan.pack(side="left", pady=0, padx=500, anchor="w")
        

        # Main content frame
        self.image_frame = ctk.CTkFrame(self, fg_color="#D6D2D2")
        self.image_frame.place(rely=0.074, relwidth=1, relheight=0.6)

        # Ubah path di sini sesuai dengan lokasi file gambar Anda
        image_dir = r"D:\Maulana\Kuliah\Semester 2\Latihan prokom\coba\foto2"  # Sesuaikan dengan direktori gambar Anda
        self.image_paths = [
            os.path.join(image_dir, "i1.jpg"),
            os.path.join(image_dir, "i2.jpg"),
            os.path.join(image_dir, "i3.jpg"),
            os.path.join(image_dir, "i4.jpg"),
            os.path.join(image_dir, "i5.jpg"),
            os.path.join(image_dir, "i6.jpg"),
            os.path.join(image_dir, "i7.jpg"),
            os.path.join(image_dir, "i8.jpg")
        ]

        self.images = [ImageTk.PhotoImage(Image.open(img).resize((1913, 650), Image.LANCZOS)) for img in self.image_paths]
        self.current_image_index = 0
        self.image_label = ctk.CTkLabel(self.image_frame, image=self.images[self.current_image_index])
        self.image_label.pack(fill="both", expand=True)

        self.update_slide_show()

        # Bottom frame
        bottom_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#9EB895")
        bottom_frame.place(rely=0.68, relwidth=1, relheight=0.32)

        # Load and resize the logo image
        logo_image = Image.open("foto2/logo.png")  # Ganti dengan path logo Anda
        logo_image = logo_image.resize((300, 300), Image.LANCZOS)  # Sesuaikan ukuran logo sesuai kebutuhan

        # Convert the image for tkinter
        self.logo = ImageTk.PhotoImage(logo_image)

        # Add label to display the logo in bottom frame
        logo_label = ctk.CTkLabel(bottom_frame, image=self.logo)
        logo_label.pack(side="left", padx=30, pady=10)  # Atur posisi logo sesuai kebutuhan

        # Bottom frame content using place
        left_frame2 = ctk.CTkFrame(bottom_frame, fg_color="#D6D2D2",corner_radius=20)
        left_frame2.place(relx=0.3, rely=0.18, relwidth=0.33, relheight=0.8)
        left_frame = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=20)
        left_frame.place(relx=0.3, rely=0.1, relwidth=0.33, relheight=0.8)
        right_frame2 = ctk.CTkFrame(bottom_frame, fg_color="#D6D2D2", corner_radius=20)
        right_frame2.place(relx=0.65, rely=0.18, relwidth=0.33, relheight=0.8)
        right_frame = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=20)
        right_frame.place(relx=0.65, rely=0.1, relwidth=0.33, relheight=0.8)
        
        #shadow_frame_left = ctk.CTkFrame(bottom_frame, bg_color="#D6D2D2", corner_radius=20)
        #shadow_frame_left.place(relx=0.3, rely=0.82, relwidth=0.33, relheight=0.15)

        # Left frame content
        logo_image2 = Image.open("foto2\logo2.png")  
        logo_image2 = logo_image2.resize((140, 140), Image.LANCZOS)  
        self.logo2 = ImageTk.PhotoImage(logo_image2)
        left_text = ctk.CTkLabel(left_frame, text="Ingin Menggalang Dana?", font=("Barlow", 24, "bold"))
        left_text.pack(side="top", pady=10, padx=10,anchor="w")
        left_text2 = ctk.CTkLabel(left_frame, text="Dengan dukungan anda, kami dapat membuat \nperubahan nyata", font=("TT Hoves", 14, "bold"), text_color="#A5A5A5",justify="left")
        left_text2.pack(side="top", pady=0, padx=10,anchor="w")    
        logo_label2 = ctk.CTkLabel(left_frame, image=self.logo2)
        logo_label2.pack(side="right", pady=0, padx=40, anchor="w")    
        fundraise_button = ctk.CTkButton(left_frame, text="Galang Dana", fg_color="purple", corner_radius=20)
        fundraise_button.pack(side="bottom", pady=20, padx=70,anchor="w")

    
        # Right frame content   
        logo_image3 = Image.open("foto2\logo3.png")  
        logo_image3 = logo_image3.resize((140, 140), Image.LANCZOS)  
        self.logo3 = ImageTk.PhotoImage(logo_image3)
        right_text = ctk.CTkLabel(right_frame, text="Yuk Berbagi", font=("Barlow", 24, "bold"))
        right_text.pack(side="top", pady=10, padx=10,anchor="w")
        right_text2 = ctk.CTkLabel(right_frame, text="Setiap rupiah anda merupakan harapan baru \nbagi mereka",  font=("TT Hoves", 14, "bold"), text_color="#A5A5A5",justify="left")
        right_text2.pack(side="top", pady=0, padx=10,anchor="w")
        logo_label3 = ctk.CTkLabel(right_frame, image=self.logo3)
        logo_label3.pack(side="right", pady=0, padx=40, anchor="w") 
        donate_button = ctk.CTkButton(right_frame, text="Donasi", fg_color="purple", corner_radius=20)
        donate_button.pack(side="bottom", pady=20, padx=70,anchor="w")

        # Add other widgets to the right side of the bottom frame
        # Example:
        some_button = ctk.CTkButton(top_frame, text="Logout", fg_color="purple", corner_radius=20, command=self.logout)
        some_button.pack(side="right", padx=5, pady=10)  # Atur posisi tombol sesuai kebutuhan


    def update_slide_show(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.image_label.configure(image=self.images[self.current_image_index])
        self.after(3000, self.update_slide_show)  # Mengganti gambar setiap 3 detik

    def logout(self):
        self.destroy()
        halaman_login()

if __name__ == "__main__":
    def halaman_login():
        import login
        login.halaman_login()
        return

    username = "User"  # Placeholder, you should replace this with the actual username after login
    app = SlideShowApp(username)
    app.mainloop()
