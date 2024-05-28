import tkinter as tk
from tkinter import messagebox
import csv
import os
import galang_dana
from PIL import ImageTk, Image

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

def write_donation(campaign, amount, method, code):
    is_new_file = not os.path.exists(donations_file)
    with open(donations_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(['campaign', 'amount', 'method', 'code'])
        writer.writerow([campaign, amount, method, code])

def clear_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

def show_donation_page(window):
    clear_screen(window)
    tk.Label(window, text="Halaman Donasi").pack()
    tk.Button(window, text="Pilih Kampanye", command=lambda: show_campaign_page(window)).pack()
    tk.Button(window, text="Kembali ke Beranda", command=lambda: show_main_page(window)).pack()

def show_campaign_page(window):
    clear_screen(window)
    tk.Label(window, text="Pilih Kampanye untuk Donasi").pack()
    campaigns = read_campaigns()
    for campaign in campaigns:
        campaign_name = campaign['title']
        #campaign_image = campaign['image']
        
        frame = tk.Frame(window)
        frame.pack(fill='x', padx=10, pady=5)
        
        #img = Image.open(campaign_image)
        #img = img.resize((100, 100), Image.LANCZOS)
        #photo = ImageTk.PhotoImage(img)
        
        #label = tk.Label(frame, image=photo)
        #label.image = photo  # Keep a reference to avoid garbage collection
        #label.pack(side='left')

        tk.Button(frame, text=campaign_name, command=lambda c=campaign_name: check_campaign_availability(window, c)).pack(side='left')
    tk.Button(window, text="Kembali", command=lambda: show_donation_page(window)).pack()

def check_campaign_availability(window, campaign):
    campaign_available = True
    if campaign_available:
        show_campaign_details(window, campaign)
    else:
        messagebox.showerror("Kampanye", "Kampanye Tidak Tersedia")
        show_campaign_page(window)

def show_campaign_details(window, campaign):
    clear_screen(window)
    tk.Label(window, text=f"Detail {campaign}").pack()
    tk.Label(window, text="Masukkan Jumlah Donasi:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()
  
    confirm_button = tk.Button(window, text="Konfirmasi Donasi", command=lambda: validate_and_confirm(window, campaign, amount_entry.get()))
    confirm_button.pack()
    tk.Button(window, text="Kembali", command=lambda: show_campaign_page(window)).pack()

def validate_and_confirm(window, campaign, amount):
        if amount == "":
            messagebox.showerror("Error", "Harap isi jumlah donasi!")
        else:
            confirm_donation_process(window, campaign, amount)

def confirm_donation_process(window, campaign, amount):
    tk.Label(window, text=f"Jumlah Donasi: {amount}").pack()
    tk.Button(window, text="Proses Pembayaran", command=lambda: process_payment(window, campaign, amount)).pack()
    tk.Button(window, text="Kembali", command=lambda: show_campaign_page(window)).pack()

def process_payment(window, campaign, amount):
    clear_screen(window)
    tk.Label(window, text=f"Proses Pembayaran untuk {campaign}").pack()
    tk.Label(window, text="Pilih Metode Pembayaran:").pack()
    tk.Button(window, text="E-Money", command=lambda: choose_emoney(window, campaign, amount)).pack()
    tk.Button(window, text="Transfer Bank", command=lambda: choose_bank_transfer(window, campaign, amount)).pack()
    tk.Button(window, text="Kembali", command=lambda: show_campaign_details(window, campaign)).pack()

def choose_emoney(window, campaign, amount):
    clear_screen(window)
    tk.Label(window, text="Pilih E-Money").pack()
    tk.Button(window, text="ShopeePay", command=lambda: enter_account_number(window, campaign, amount, "ShopeePay", payment_codes['E-Money']['ShopeePay'])).pack()
    tk.Button(window, text="GoPay", command=lambda: enter_account_number(window, campaign, amount, "GoPay", payment_codes['E-Money']['GoPay'])).pack()
    tk.Button(window, text="OVO", command=lambda: enter_account_number(window, campaign, amount, "OVO", payment_codes['E-Money']['OVO'])).pack()
    tk.Button(window, text="Dana", command=lambda: enter_account_number(window, campaign, amount, "Dana", payment_codes['E-Money']['Dana'])).pack()
    tk.Button(window, text="Kembali", command=lambda: process_payment(window, campaign, amount)).pack()

def choose_bank_transfer(window, campaign, amount):
    clear_screen(window)
    tk.Label(window, text="Pilih Bank").pack()
    tk.Button(window, text="BCA", command=lambda: enter_account_number(window, campaign, amount, "BCA", payment_codes['Transfer Bank']['BCA'])).pack()
    tk.Button(window, text="BRI", command=lambda: enter_account_number(window, campaign, amount, "BRI", payment_codes['Transfer Bank']['BRI'])).pack()
    tk.Button(window, text="Mandiri", command=lambda: enter_account_number(window, campaign, amount, "Mandiri", payment_codes['Transfer Bank']['Mandiri'])).pack()
    tk.Button(window, text="BNI", command=lambda: enter_account_number(window, campaign, amount, "BNI", payment_codes['Transfer Bank']['BNI'])).pack()
    tk.Button(window, text="BSI", command=lambda: enter_account_number(window, campaign, amount, "BSI", payment_codes['Transfer Bank']['BSI'])).pack()
    tk.Button(window, text="Panin", command=lambda: enter_account_number(window, campaign, amount, "Panin", payment_codes['Transfer Bank']['Panin'])).pack()
    tk.Button(window, text="Kembali", command=lambda: process_payment(window, campaign, amount)).pack()

def enter_account_number(window, campaign, amount, method, code):
    clear_screen(window)
    tk.Label(window, text=f"Masukkan Nomor Rekening untuk {method}").pack()
    tk.Label(window, text=f"Kode Pembayaran: {code}").pack()
    account_number_entry = tk.Entry(window)
    account_number_entry.pack()

    def validate_and_confirm():
        account_number = account_number_entry.get()
        if not account_number.startswith(code):
            messagebox.showerror("Error", f"Nomor rekening harus diawali dengan kode pembayaran {code}")
            return
        payment_success(window, campaign, amount, method, code + account_number[len(code):])

    tk.Button(window, text="Konfirmasi Donasi", command=validate_and_confirm).pack()
    tk.Button(window, text="Kembali", command=lambda: process_payment(window, campaign, amount)).pack()

def payment_success(window, campaign, amount, method, code):
    clear_screen(window)
    write_donation(campaign, amount, method, code)
    tk.Label(window, text="Terima Kasih!").pack()
    tk.Label(window, text=f"Donasi ke {campaign} sebesar {amount} menggunakan {method} berhasil.").pack()
    tk.Button(window, text="Kembali ke Beranda", command=lambda: show_main_page(window)).pack()

def show_main_page(window):
    clear_screen(window)
    tk.Label(window, text="Selamat Datang di Sistem Donasi WeCann").pack()
    tk.Button(window, text="Donasi", command=lambda: show_donation_page(window)).pack()
    tk.Button(window, text="Galang Dana", command=lambda: galang_dana.show_fundraising_page(window)).pack()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Sistem Donasi WeCann")

    show_main_page(window)
    window.mainloop()
