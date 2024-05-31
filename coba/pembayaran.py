import customtkinter as ctk
from tkinter import messagebox
import os
import csv

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

class BayarApp(ctk.CTkToplevel):
    def __init__(self, parent, campaign, amount):
        super().__init__(parent)
        self.campaign = campaign
        self.amount = amount

        self.geometry("550x450")
        self.title("Metode Pembayaran")
        self.attributes('-fullscreen', True)

        self.label = ctk.CTkLabel(self, text=f"Donasi untuk {self.campaign}\nJumlah: {self.amount}", font=("Arial", 14))
        self.label.pack(pady=70)

        self.e_money_button = ctk.CTkButton(self, text="E-Money", command=lambda: self.choose_emoney(campaign, amount))
        self.e_money_button.pack(pady=10)

        self.bank_transfer_button = ctk.CTkButton(self, text="Transfer Bank", command=lambda: self.choose_bank_transfer(campaign, amount))
        self.bank_transfer_button.pack(pady=10)

        # Ensure the Toplevel window appears in front
        self.lift()
        self.focus_force()

    def initialize_ui(self):
        self.clear_window_content()

        campaigns = self.read_campaigns()

        if campaigns:
            campaign = campaigns[0]['title']
            amount = campaigns[0]['target']

            self.show_campaign_details(campaign, amount)
        else:
            messagebox.showerror("Kesalahan", "Tidak ada kampanye yang tersedia.")

    def show_campaign_details(self, campaign, amount):
        self.clear_window_content()
        frame1 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame1.place(rely=0.4, relx=0.3, relheight=0.35, relwidth=0.4)
        ctk.CTkLabel(frame1, text=f"Detail {campaign}").pack(pady=0.58)
        ctk.CTkLabel(frame1, text="Pastikan Nominal Donasi:").pack()
        amount_entry = ctk.CTkEntry(frame1)
        amount_entry.pack()
        amount_entry.insert(0, amount)
        confirm_button = ctk.CTkButton(frame1, text="Konfirmasi Donasi", command=lambda: self.validate_and_confirm(campaign, amount_entry.get()))
        confirm_button.pack(pady=1)
        ctk.CTkButton(frame1, text="Back", command=self.destroy).pack(pady=1.3)

    def validate_and_confirm(self, campaign, amount):
        if amount == "":
            messagebox.showerror("Error", "Harap isi jumlah donasi!")
        else:
            self.confirm_donation_process(campaign, amount)

    def confirm_donation_process(self, campaign, amount):
        self.clear_window_content()
        frame2 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame2.place(rely=0.4, relx=0.3, relheight=0.32, relwidth=0.4)
        ctk.CTkLabel(frame2, text=f"Jumlah Donasi: {amount}").pack(pady=10)
        ctk.CTkButton(frame2, text="Proses Pembayaran", command=lambda: self.process_payment(campaign, amount)).pack(pady=5)
        ctk.CTkButton(frame2, text="Back", command=self.destroy).pack(pady=10)

    def process_payment(self, campaign, amount):
        self.clear_window_content()
        frame3 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame3.place(rely=0.3, relx=0.25, relheight=0.37, relwidth=0.5)
        ctk.CTkLabel(frame3, text=f"Proses Pembayaran untuk  \n({campaign})").pack()
        ctk.CTkLabel(frame3, text="Pilih Metode Pembayaran:").pack()
        ctk.CTkButton(frame3, text="E-Money", command=lambda: self.choose_emoney(campaign, amount)).pack()
        ctk.CTkButton(frame3, text="Transfer Bank", command=lambda: self.choose_bank_transfer(campaign, amount)).pack(pady=2)
        ctk.CTkButton(frame3, text="Back", command=self.destroy).pack(pady=5)

    def choose_emoney(self, campaign, amount):
        self.clear_window_content()
        frame4 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame4.place(rely=0.35, relx=0.25, relheight=0.42, relwidth=0.5)
        ctk.CTkLabel(frame4, text="Pilih E-Money").pack()
        for method, code in payment_codes['E-Money'].items():
            ctk.CTkButton(frame4, text=method, command=lambda m=method, c=code: self.enter_account_number(campaign, amount, m, c), corner_radius=30).pack(pady=1)
        ctk.CTkButton(frame4, text="Back", command=lambda: self.process_payment(campaign, amount)).pack(pady=3)

    def choose_bank_transfer(self, campaign, amount):
        self.clear_window_content()
        frame5 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame5.place(rely=0.3, relx=0.25, relheight=0.58, relwidth=0.5)
        ctk.CTkLabel(frame5, text="Pilih Bank").pack()
        for method, code in payment_codes['Transfer Bank'].items():
            ctk.CTkButton(frame5, text=method, command=lambda m=method, c=code: self.enter_account_number(campaign, amount, m, c), corner_radius=30).pack(pady=1)
        ctk.CTkButton(frame5, text="Back", command=lambda: self.process_payment(campaign, amount)).pack(pady=3.2)

    def enter_account_number(self, campaign, amount, method, code):
        self.clear_window_content()
        frame6 = ctk.CTkFrame(self, corner_radius=20, fg_color="#7F7F7F")
        frame6.place(rely=0.3, relx=0.15, relheight=0.58, relwidth=0.7)
        ctk.CTkLabel(frame6, text=f"Masukkan Nomor Rekening untuk {method}").pack(pady=15)
        ctk.CTkLabel(frame6, text=f"Pastikan Tulis Kode Pembayaran Sebelum No. Rekening \nNo. Rekening : 77657835 \nKode Pembayaran: {code}").pack(pady=5)
        account_number_entry = ctk.CTkEntry(frame6)
        account_number_entry.pack(pady=7)

        def validate_and_confirm():
            account_number = account_number_entry.get()
            if not account_number.startswith(code):
                messagebox.showerror("Error", f"Nomor rekening harus diawali dengan kode pembayaran {code}")
                return
            self.payment_success(campaign, amount, method, code + account_number[len(code):])

        ctk.CTkButton(frame6, text="Konfirmasi Donasi", command=validate_and_confirm).pack(pady=5)
        ctk.CTkButton(frame6, text="Back", command=lambda: self.process_payment(campaign, amount)).pack(pady=8)

    def clear_window_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def payment_success(self, campaign, amount, method, code):
        self.clear_window_content()
        ctk.CTkLabel(self, text="Terima Kasih! \nSemoga Berkah :)", font=("Arial", 25, "bold")).pack(pady=120)
        ctk.CTkLabel(self, text=f"Donasi ke {campaign} sebesar {amount} menggunakan {method} berhasil.").pack()
        ctk.CTkButton(self, text="Back", command=self.show_confirmation_message).pack()


        # Save the donation details to CSV
        self.save_donation_to_csv(campaign, amount, method, code)

    def show_confirmation_message(self):
        messagebox.showinfo("MAKASIII ORANG BAIKKK", "PANJANG-PANJANG ORANG BAIKK :)")
        self.destroy()

    def save_donation_to_csv(self, campaign, amount, method, code):
        file_exists = os.path.isfile(donations_file)
        with open(donations_file, mode='a', newline='') as file:
            fieldnames = ['title', 'amount', 'method', 'code']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({'title': campaign, 'amount': amount, 'method': method, 'code': code})

    def read_campaigns(self):
        campaigns = []
        if os.path.exists(campaigns_file):
            with open(campaigns_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                campaigns = list(reader)
        return campaigns

if __name__ == "__main__":
    app = BayarApp(None, "Kampanye Contoh", 100000)
    app.mainloop()
