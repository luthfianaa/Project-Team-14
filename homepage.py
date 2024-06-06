import customtkinter as ctk
from tkinter import messagebox
import os
from PIL import Image
from donasii import DonationApp
from kampanye import KampanyeApp


class SlideShowApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()

        self.username = username

        self.geometry("800x500")
        self.attributes('-fullscreen', False)
        
        self.title("WeCan")

        # Set appearance mode
        ctk.set_appearance_mode("light")  # "light", "dark", or system
        ctk.set_default_color_theme("blue")  

        # Top frame
        top_frame = ctk.CTkFrame(self, height=40, width=800, corner_radius=0, fg_color="#9EB895")
        top_frame.place(relwidth=1, y=0)

        logo_orang = Image.open("foto2/profile_icon1.png").resize((40, 26), Image.LANCZOS)
        self.logo_orang = ctk.CTkImage(light_image=logo_orang, size=(40, 26))
        logo_label_orang = ctk.CTkLabel(top_frame, image=self.logo_orang, text=" ")
        logo_label_orang.pack(side="left", pady=0, padx=5, anchor="w")

        profile_name = ctk.CTkLabel(top_frame, text=self.username, font=("Arial", 14))
        profile_name.place(x=50, y=10)

        logo_wecan = Image.open("foto2/wecan.png").resize((150, 30), Image.LANCZOS)
        self.logo_wecan = ctk.CTkImage(light_image=logo_wecan, size=(150, 30))
        logo_logo_wecan = ctk.CTkLabel(top_frame, image=self.logo_wecan, text=" ")
        logo_logo_wecan.pack(side="left", pady=0, padx=500, anchor="w")

        # Main content frame
        self.image_frame = ctk.CTkFrame(self, fg_color="#D6D2D2")
        self.image_frame.place(rely=0.074, relwidth=1, relheight=0.6)

        image_dir = r"D:\Maulana\Kuliah\Semester 2\Latihan prokom\coba\foto2"
        self.image_paths = [
            os.path.join(image_dir, "i1.jpg"),
            os.path.join(image_dir, "i2.jpg"),
            os.path.join(image_dir, "i3.jpg"),
            os.path.join(image_dir, "i4.jpg"),
            os.path.join(image_dir, "i5.jpg"),
            os.path.join(image_dir, "i6.jpg"),
            os.path.join(image_dir, "i7.jpg"),
            os.path.join(image_dir, "i8.jpg"),
            os.path.join(image_dir, "i9.jpg"),
            os.path.join(image_dir, "i10.jpg"),
            os.path.join(image_dir, "i11.jpg")
        ]

        self.images = [ctk.CTkImage(light_image=Image.open(img).resize((1913, 650), Image.LANCZOS), size=(1913, 650)) for img in self.image_paths]
        self.current_image_index = 0
        self.image_label = ctk.CTkLabel(self.image_frame, image=self.images[self.current_image_index], text=" ")
        self.image_label.pack(fill="both", expand=True)

        self.update_slide_show()

        # Bottom frame
        bottom_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#9EB895")
        bottom_frame.place(rely=0.68, relwidth=1, relheight=0.32)

        logo_image = Image.open("foto2/logo.png").resize((200, 200), Image.LANCZOS)
        self.logo = ctk.CTkImage(light_image=logo_image, size=(200, 200))
        logo_label = ctk.CTkLabel(bottom_frame, image=self.logo, text=" ")
        logo_label.pack(side="left", padx=30, pady=10)

        left_frame = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=20)
        left_frame.place(relx=0.3, rely=0.1, relwidth=0.33, relheight=0.8)

        right_frame = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=20)
        right_frame.place(relx=0.65, rely=0.1, relwidth=0.33, relheight=0.8)

        logo_image2 = Image.open("foto2/logo2.png").resize((100, 100), Image.LANCZOS)
        self.logo2 = ctk.CTkImage(light_image=logo_image2, size=(100, 100))
        left_text = ctk.CTkLabel(left_frame, text="Ingin Menggalang Dana?", font=("Barlow", 24, "bold"))
        left_text.pack(side="top", pady=10, padx=10, anchor="w")
        left_text2 = ctk.CTkLabel(left_frame, text="Dengan dukungan anda, kami dapat membuat \nperubahan nyata", font=("TT Hoves", 14, "bold"), text_color="#A5A5A5", justify="left")
        left_text2.pack(side="top", pady=0, padx=10, anchor="w")
        logo_label2 = ctk.CTkLabel(left_frame, image=self.logo2, text=" ")
        logo_label2.pack(side="right", pady=0, padx=40, anchor="w")
        fundraise_button = ctk.CTkButton(left_frame, text="Galang Dana", fg_color="purple", corner_radius=20, command=self.show_kampanye)
        fundraise_button.pack(side="bottom", pady=20, padx=70, anchor="w")

        logo_image3 = Image.open("foto2/logo3.png").resize((100, 100), Image.LANCZOS)
        self.logo3 = ctk.CTkImage(light_image=logo_image3, size=(100, 100))
        right_text = ctk.CTkLabel(right_frame, text="Yuk Berbagi", font=("Barlow", 24, "bold"))
        right_text.pack(side="top", pady=10, padx=10, anchor="w")
        right_text2 = ctk.CTkLabel(right_frame, text="Setiap rupiah anda merupakan harapan baru \nbagi mereka", font=("TT Hoves", 14, "bold"), text_color="#A5A5A5", justify="left")
        right_text2.pack(side="top", pady=0, padx=10, anchor="w")
        logo_label3 = ctk.CTkLabel(right_frame, image=self.logo3, text=" ")
        logo_label3.pack(side="right", pady=0, padx=40, anchor="w")
        donate_button = ctk.CTkButton(right_frame, text="Donasi", fg_color="purple", corner_radius=20, command=self.show_donasi)
        donate_button.pack(side="bottom", pady=20, padx=70, anchor="w")

        some_button = ctk.CTkButton(top_frame, text="Logout", fg_color="purple", corner_radius=20, command=self.logout)
        some_button.pack(side="right", padx=5, pady=10)

    def update_slide_show(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.image_label.configure(image=self.images[self.current_image_index])
        self.after(3000, self.update_slide_show)

    def halaman_login(self):
        import login
        login.halaman_login()
        return

    def show_donasi(self):
        self.destroy()
        app1 = DonationApp(self.username)
        app1.mainloop()

    def show_kampanye(self):
        self.destroy()
        app2 = KampanyeApp(self.username)
        app2.mainloop()

    def logout(self):
        self.destroy()
        self.halaman_login()


if __name__ == "__main__":
    username = "User"  # Placeholder, you should replace this with the actual username after login
    app = SlideShowApp(username)
    app.mainloop()
