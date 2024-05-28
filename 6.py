import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")  # "light" atau "dark"
ctk.set_default_color_theme("blue")  # Mengatur tema warna

class DonationApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.geometry("800x500")
        self.title("kampanye Page")
        self.bind("<Configure>", self.on_resize)

        self.top_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#9EB895")
        self.top_frame.place(relx=0, rely=0, relwidth=1)

        logo_orang = Image.open("foto2/profile_icon1.png")
        logo_orang = logo_orang.resize((50, 43), Image.LANCZOS)
        self.logo_orang = ImageTk.PhotoImage(logo_orang)
        self.logo_label_orang = ctk.CTkLabel(self.top_frame, image=self.logo_orang)
        self.logo_label_orang.place(x=5, y=10)

        self.profile_name = ctk.CTkLabel(self.top_frame, text=self.username, font=("Arial", 14))
        self.profile_name.place(x=60, y=20)

        # Frame kiri
        self.left_frame = ctk.CTkFrame(self, fg_color="#FFFFFF",corner_radius=20)
        self.left_frame.place(relx=0, rely=0.09, relwidth=0.5, relheight=0.65)

        # Label "Masukkan detail kampanye baru"
        self.title_label = ctk.CTkLabel(self.left_frame, text="Masukkan Detail Kampanye Baru", font=("Glacial Indifference", 20 , "bold"))
        self.title_label.place(relx=0.05, rely=0.05)

        # Label dan Entry untuk Judul Kampanye
        self.name_label = ctk.CTkLabel(self.left_frame, text="Judul Kampanye", font=("Droid Serif", 14),text_color="#666666")
        self.name_label.place(relx=0.05, rely=0.15)
        self.name_entry = ctk.CTkEntry(self.left_frame, font=("Droid Serif", 14))
        self.name_entry.place(relx=0.05, rely=0.22, relwidth=0.9)

        # Label dan Entry untuk Keterangan Kampanye
        self.description_label = ctk.CTkLabel(self.left_frame, text="Keterangan Kampanye", font=("Droid Serif", 14),text_color="#666666")
        self.description_label.place(relx=0.05, rely=0.30)
        self.description_entry = ctk.CTkEntry(self.left_frame, font=("Droid Serif", 14))
        self.description_entry.place(relx=0.05, rely=0.37, relwidth=0.9)

        # Label dan Entry untuk Target Donasi
        self.target_label = ctk.CTkLabel(self.left_frame, text="Target Donasi", font=("Droid Serif", 14),text_color="#666666")
        self.target_label.place(relx=0.05, rely=0.45)
        self.target_entry = ctk.CTkEntry(self.left_frame, font=("Droid Serif", 14))
        self.target_entry.place(relx=0.05, rely=0.52, relwidth=0.9)

        # Label dan Entry untuk Durasi (hari)
        self.duration_label = ctk.CTkLabel(self.left_frame, text="Durasi (hari)", font=("Droid Serif", 14),text_color="#666666")
        self.duration_label.place(relx=0.05, rely=0.60)
        self.duration_entry = ctk.CTkEntry(self.left_frame, font=("Droid Serif", 14))
        self.duration_entry.place(relx=0.05, rely=0.67, relwidth=0.9)

        # Label dan Entry untuk Pilih Foto Kampanye
        self.photo_label = ctk.CTkLabel(self.left_frame, text="Pilih Foto Kampanye", font=("Droid Serif", 14),text_color="#666666")
        self.photo_label.place(relx=0.05, rely=0.75)
        self.photo_entry = ctk.CTkEntry(self.left_frame, font=("Droid Serif", 14))
        self.photo_entry.place(relx=0.05, rely=0.82, relwidth=0.9)

        # Tombol Buat Kampanye
        self.create_button = ctk.CTkButton(self.left_frame, text="Buat Kampanye", fg_color="purple", text_color="white",corner_radius=20)
        self.create_button.place(relx=0.25, rely=0.8, relwidth=0.5,relheight=0.08)

        # Frame kanan
        self.right_frame = ctk.CTkFrame(self, fg_color="#FFFFFF",corner_radius=20)
        self.right_frame.place(relx=0.508, rely=0.09, relwidth=0.49, relheight=0.4)

        # Label besar di kanan
        self.big_label = ctk.CTkLabel(self.right_frame, text="Semoga kami dapat membantu untuk menjadi\nperantara bagi mereka para pahlawan", font=("Glacial Indifference", 25, "bold"), justify="center")
        self.big_label.place(relx=0.05, rely=0.35)

        # Gambar hati di kanan bawah
        heart_image = Image.open("foto2/logo4.png")  # Sesuaikan path gambar hati Anda
        heart_image = heart_image.resize((150, 150), Image.LANCZOS)
        self.heart_image = ImageTk.PhotoImage(heart_image)
        self.heart_label = ctk.CTkLabel(self.right_frame, image=self.heart_image)
        self.heart_label.place(relx=0.3, rely=0.3)

        # Label di bawah kiri
        self.bottom_left_frame = ctk.CTkFrame(self, fg_color="white",corner_radius=20)
        self.bottom_left_frame.place(relx=0, rely=0.76, relwidth=0.5, relheight=0.2)
        self.bottom_label = ctk.CTkLabel(self.bottom_left_frame, text="Tidak ada kebaikan yang terlalu kecil untuk\nmembuat perbedaan. Bergabunglah dengan\nkami dalam memberi harapan dan kehidupan baru.", font=("Glacial Indifference", 20, "bold"), text_color="#555555", justify="left")
        self.bottom_label.place(relx=0.02, rely=0.3)

        # Gambar kotak hati di kiri bawah
        box_heart_image = Image.open("foto2/logo2.png")  # Sesuaikan path gambar hati dalam kotak Anda
        box_heart_image = box_heart_image.resize((150, 150), Image.LANCZOS)
        self.box_heart_image = ImageTk.PhotoImage(box_heart_image)
        self.box_heart_label = ctk.CTkLabel(self.bottom_left_frame, image=self.box_heart_image)
        self.box_heart_label.place(relx=0.79, rely=0.22)

        # logo wecan
        self.bottom_right_frame = ctk.CTkFrame(self, fg_color="#9EB895",corner_radius=20)
        self.bottom_right_frame.place(relx=0.51, rely=0.5, relwidth=0.49, relheight=0.458)
        self.bottomr_label = ctk.CTkLabel(self.bottom_right_frame, text="T", font=("Glacial Indifference", 20, "bold"), text_color="#555555", justify="left")
        self.bottomr_label.place(relx=0.508, rely=0.59)
        wecan_logo = Image.open("foto2/logo.png")  # Sesuaikan path gambar hati dalam kotak Anda
        wecan_logo = wecan_logo.resize((450, 450), Image.LANCZOS)
        self.wecan_logo = ImageTk.PhotoImage(wecan_logo)
        self.wecan_logo_label = ctk.CTkLabel(self.bottom_right_frame, image=self.wecan_logo)
        self.wecan_logo_label.place(relx=0.3, rely=0.055)


    def on_resize(self, event):
        # Mengubah posisi dan ukuran elemen dalam left_frame
        self.name_entry.place(relwidth=0.9)
        self.description_entry.place(relwidth=0.9)
        self.target_entry.place(relwidth=0.9)
        self.duration_entry.place(relwidth=0.9)
        self.photo_entry.place(relwidth=0.9)
        self.create_button.place(relx=0.25, rely=0.90, relwidth=0.5)

        # Mengubah posisi dan ukuran elemen dalam right_frame
        self.big_label.place(relx=0.05, rely=0.35)
        self.heart_label.place(relx=0.75, rely=0.75)

if __name__ == "__main__":
    username = "Nama"
    app = DonationApp(username)
    app.mainloop()
