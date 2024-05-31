import customtkinter as ctk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import csv
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

campaigns_file = 'campaigns.csv'
donations_file = 'donations.csv'
payment_codes = {
    'E-Money': {
        'ShopeePay': '0031',
        'GoPay': '0032',
        'OVO': '0033',
        'Dana': '0034'
    },
    'Transfer Bank': {
        'BCA': '771',
        'BRI': '991',
        'Mandiri': '551',
        'BNI': '661',
        'BSI': '881',
        'Panin': '441'
    }
}

def read_campaigns():
    campaigns = []
    if os.path.exists(campaigns_file):
        with open(campaigns_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            campaigns = list(reader)
    return campaigns

def read_donations():
    donations = []
    if os.path.exists(donations_file):
        with open(donations_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            donations = list(reader)
    return donations

def write_donation(campaign, amount, method, code):
    is_new_file = not os.path.exists(donations_file)
    with open(donations_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(['campaign', 'amount', 'method', 'code'])
        writer.writerow([campaign, amount, method, code])

def calculate_total_donation_by_title(title):
    donations = read_donations()
    total_donation = sum(float(donation['amount']) for donation in donations if donation['campaign'] == title and donation['amount'])
    return total_donation

def calculate_total_donations_by_titles():
    campaigns = read_campaigns()
    total_donations_by_title = {}
    for campaign in campaigns:
        title = campaign['title']
        total_donation = calculate_total_donation_by_title(title)
        total_donations_by_title[title] = total_donation
    return total_donations_by_title

def read_target_donation(campaign_title):
    with open('campaigns.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['title'] == campaign_title:
                return float(row['target'])
    return 0  # Jika tidak ditemukan, kembalikan nilai 0

def read_total_donations():
    total_donations = 0
    donations = read_donations()
    for donation in donations:
        total_donations += float(donation['amount'])
    return total_donations

def calculate_remaining_donation(selected_campaign):
    target_donation = read_target_donation(selected_campaign)
    total_donation = read_total_donations()
    remaining_donation = max(0, target_donation - total_donation)
    return remaining_donation

def clear_screen(self):
    for widget in self.winfo_children():
        widget.destroy()

class DonationApp(ctk.CTk):
    def kembali(self):
        from homepage import SlideShowApp
        self.destroy()
        app1 = SlideShowApp(self.username)
        app1.mainloop()

    def update_progressbar(self):
        total_donations_by_titles = calculate_total_donations_by_titles()
        selected_campaign = self.campaign_entry.get()
        if selected_campaign in total_donations_by_titles:
            total_donation = total_donations_by_titles[selected_campaign]
            target_donation = read_target_donation(selected_campaign)  # Ambil target donasi dari kampanye yang dipilih
            percentage = min(100, (total_donation / target_donation) * 100) if target_donation != 0 else 0  # Hitung persentase relatif terhadap target_donation
            self.progressbar["value"] = percentage
            self.progressbar.update()
        else:
            self.progressbar["value"] = 0


    def __init__(self, username):
        super().__init__()
        self.username = username

        self.right_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=20)

        self.geometry("800x500")
        self.title("Donation Page")
        self.bind("<Configure>", self.on_resize)

        self.right_frame.place(relx=0.508, rely=0.09, relwidth=0.49, relheight=0.87)

        self.top_frame = ctk.CTkFrame(self, height=40, fg_color="#9EB895")
        self.top_frame.place(relx=0, rely=0, relwidth=1)

        logo_orang = Image.open("foto2/profile_icon1.png")
        logo_orang = logo_orang.resize((50, 43), Image.LANCZOS)
        self.logo_orang = ImageTk.PhotoImage(logo_orang)
        self.logo_label_orang = ctk.CTkLabel(self.top_frame, image=self.logo_orang, text=" ")
        self.logo_label_orang.place(x=5, y=10)

        self.profile_name = ctk.CTkLabel(self.top_frame, text=self.username, font=("Arial", 14))
        self.profile_name.place(x=50, y=10)
        some_button = ctk.CTkButton(self.top_frame, text="Back", fg_color="purple", corner_radius=20, command=self.kembali)
        some_button.pack(side="right", padx=1, pady=10)

        self.left_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=20)
        self.left_frame.place(relx=0, rely=0.09, relwidth=0.5, relheight=0.65)

        self.name_label = ctk.CTkLabel(self.left_frame, text="Nama", font=("Arial", 14))
        self.name_label.place(relx=0.05, rely=0.05)

        self.name_entry = ctk.CTkEntry(self.left_frame, font=("Arial", 14))
        self.name_entry.place(relx=0.05, rely=0.12, relwidth=0.9)
        self.name_entry.insert(0, self.username)

        self.campaign_label = ctk.CTkLabel(self.left_frame, text="Kampanye", font=("Arial", 14))
        self.campaign_label.place(relx=0.05, rely=0.22)

        self.campaigns = read_campaigns()
        campaign_titles = [campaign['title'] for campaign in self.campaigns]
        self.campaign_entry = ctk.CTkComboBox(self.left_frame, values=campaign_titles, font=("Arial", 14), command=self.on_campaign_selected)
        self.campaign_entry.place(relx=0.05, rely=0.29, relwidth=0.9)

        self.amount_label = ctk.CTkLabel(self.left_frame, text="Nominal Donasi", font=("Arial", 14))
        self.amount_label.place(relx=0.05, rely=0.39)

        self.amount_entry = ctk.CTkEntry(self.left_frame, font=("Arial", 14))
        self.amount_entry.place(relx=0.05, rely=0.46, relwidth=0.9)

        self.pay_button = ctk.CTkButton(self.left_frame, text="Metode Pembayaran", fg_color="purple", text_color="white", command=self.show_bayar)
        self.pay_button.place(relx=0.25, rely=0.56, relwidth=0.5)

        self.bottom_left_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=20)
        self.bottom_left_frame.place(relx=0, rely=0.76, relwidth=0.5, relheight=0.2)
        self.bottom_label = ctk.CTkLabel(self.bottom_left_frame, text="Dengan setiap kebaikan yang kamu berikan,\nkamu telah menjadi sumber harapan bagi\nbanyak orang yang membutuhkan. Semoga\ndapat menjadi inspirasi bagi orang lain.", font=("Glacial Indifference", 20, "bold"), text_color="#555555", justify="left")
        self.bottom_label.place(relx=0.02, rely=0.2)

        box_heart_image = Image.open("foto2/logo3.png")
        box_heart_image = box_heart_image.resize((150, 150), Image.LANCZOS)
        self.box_heart_image = ImageTk.PhotoImage(box_heart_image)
        self.box_heart_label = ctk.CTkLabel(self.bottom_left_frame, image=self.box_heart_image, text=" ")
        self.box_heart_label.place(relx=0.79, rely=0.22)

        # Create image label for the right frame (initially empty)
        self.image_label = ctk.CTkLabel(self.right_frame, text=" ")
        self.image_label.place(relx=0.05, rely=0.05)

        self.progressbar = ttk.Progressbar(self.right_frame, orient="horizontal", length=200, mode="determinate")
        self.progressbar.place(relx=0.05, rely=0.95)

        # Create title label for the right frame (initially empty)
        self.title_label = ctk.CTkLabel(self.right_frame, text=" ", font=("Arial", 20, "bold"), text_color="#333333")
        self.title_label.place(relx=0.05, rely=0.8)

        # Create description label for the right frame (initially empty)
        self.description_label = ctk.CTkLabel(self.right_frame, text=" ", font=("Arial", 14), text_color="#555555", wraplength=350)
        self.description_label.place(relx=0.05, rely=0.85)

        # Create total donasi for the right frame (initially empty)
        self.total_donation_label = ctk.CTkLabel(self.right_frame, text="Total Donasi: ", font=("Arial", 14), text_color="#333333")
        self.total_donation_label.place(relx=0.05, rely=0.90)

        self.update_progressbar()
        self.update_total_donation()

    def update_total_donation(self):
        total_donations_by_titles = calculate_total_donations_by_titles()
        selected_campaign = self.campaign_entry.get()
        if selected_campaign in total_donations_by_titles:
            total_donation = total_donations_by_titles[selected_campaign]
            self.total_donation_label.configure(text=f"Total Donasi: {total_donation}")
        else:
            self.total_donation_label.configure(text="Total Donasi: 0")

    def on_campaign_selected(self, event=None):
        selected_campaign = self.campaign_entry.get()
        for campaign in self.campaigns:
            if campaign['title'] == selected_campaign:
                self.update_campaign_info(campaign)
                remaining_donation = calculate_remaining_donation(selected_campaign)
                print(f"Remaining donation needed for {selected_campaign}: ${remaining_donation}")
                break

   

    def update_campaign_info(self, campaign):
        self.title_label.configure(text=campaign['title'])
        self.description_label.configure(text=campaign['description'])
        image_path = campaign['image']
        if image_path:
            try:
                image = Image.open(image_path)
                image = image.resize((855, 630), Image.LANCZOS)
                self.image_photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=self.image_photo)
            except FileNotFoundError:
                self.image_label.configure(text="Image not found")
        else:
            self.image_label.configure(text="No image path provided")

    def show_bayar(self):
        selected_campaign = self.campaign_entry.get()
        amount = self.amount_entry.get()
        if selected_campaign and amount:
            from pembayaran import BayarApp
            bayar_app = BayarApp(self, selected_campaign, amount)
            bayar_app.grab_set()  # Ensure BayarApp window is modal
            bayar_app.mainloop()
        else:
            messagebox.showerror("Error", "Pilih kampanye dan masukkan jumlah donasi!")

    def confirm_payment(self):
        method = self.payment_method.get()
        if not method:
            messagebox.showwarning("Selection Error", "Please select a payment method")
            return
        
        codes = payment_codes[method]
        code_message = "\n".join([f"{key}: {value}" for key, value in codes.items()])
        messagebox.showinfo("Payment Codes", code_message)

        selected_campaign = self.campaign_entry.get()
        amount = self.amount_entry.get()
        write_donation(selected_campaign, amount, method, "N/A")

        self.update_total_donation()
        self.pay_window.destroy()

    def on_resize(self, event):
        self.update_idletasks()

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    username = "Nama"
    app = DonationApp(username)
    app.mainloop()

