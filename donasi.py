import tkinter as tk
from tkinter import messagebox
import csv
import os

# Nama file CSV
campaigns_file = 'campaigns.csv'
donations_file = 'donations.csv'

# Kode pembayaran berdasarkan metode pembayaran
payment_codes = {
    'E-Money': {
        'ShopeePay': '0031',
        'GoPay': '0032',
        'OVO': '0033'
    },
    'Transfer Bank': {
        'BCA': '771',
        'BRI': '991',
        'Mandiri': '551'
    }
}

# Fungsi untuk membaca kampanye dari file CSV
def read_campaigns():
    campaigns = []
    if os.path.exists(campaigns_file):
        with open(campaigns_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            campaigns = list(reader)
    return campaigns

# Fungsi untuk menulis donasi ke file CSV
def write_donation(campaign, amount, method, code):
    is_new_file = not os.path.exists(donations_file)
    with open(donations_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(['campaign', 'amount', 'method', 'code'])
        writer.writerow([campaign, amount, method, code])

# Fungsi untuk membersihkan layar
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

# Fungsi untuk menampilkan halaman donasi
def show_donation_page():
    clear_screen()
    tk.Label(window, text="Halaman Donasi").pack()
    tk.Button(window, text="Pilih Kampanye", command=show_campaign_page).pack()
    tk.Button(window, text="Kembali", command=show_home_page).pack()

# Fungsi untuk menampilkan halaman kampanye
def show_campaign_page():
    clear_screen()
    tk.Label(window, text="Pilih Kampanye untuk Donasi").pack()
    
    # Membaca kampanye dari file CSV
    campaigns = read_campaigns()
    
    for campaign in campaigns:
        campaign_name = campaign['title']
        tk.Button(window, text=campaign_name, command=lambda c=campaign_name: check_campaign_availability(c)).pack()

    tk.Button(window, text="Kembali", command=show_donation_page).pack()

# Fungsi untuk memeriksa ketersediaan kampanye
def check_campaign_availability(campaign):
    # Asumsi kampanye tersedia (karena dibaca dari CSV yang ada)
    campaign_available = True

    if campaign_available:
        show_campaign_details(campaign)
    else:
        messagebox.showerror("Kampanye", "Kampanye Tidak Tersedia")
        show_campaign_page()

# Fungsi untuk menampilkan detail kampanye dan donasi
def show_campaign_details(campaign):
    clear_screen()
    tk.Label(window, text=f"Detail {campaign}").pack()
    tk.Label(window, text="Masukkan Jumlah Donasi:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    tk.Button(window, text="Konfirmasi Donasi", command=lambda: confirm_donation(campaign, amount_entry.get())).pack()
    tk.Button(window, text="Kembali", command=show_campaign_page).pack()

# Fungsi untuk mengkonfirmasi donasi
def confirm_donation(campaign, amount):
    clear_screen()
    tk.Label(window, text=f"Konfirmasi Donasi untuk {campaign}").pack()
    tk.Label(window, text=f"Jumlah Donasi: {amount}").pack()
    
    tk.Button(window, text="Proses Pembayaran", command=lambda: process_payment(campaign, amount)).pack()
    tk.Button(window, text="Kembali", command=lambda: show_campaign_details(campaign)).pack()

# Fungsi untuk memproses pembayaran
def process_payment(campaign, amount):
    clear_screen()
    tk.Label(window, text=f"Proses Pembayaran untuk {campaign}").pack()
    tk.Label(window, text="Pilih Metode Pembayaran:").pack()
    
    tk.Button(window, text="E-Money", command=lambda: choose_emoney(campaign, amount)).pack()
    tk.Button(window, text="Transfer Bank", command=lambda: choose_bank_transfer(campaign, amount)).pack()
    tk.Button(window, text="Kembali", command=lambda: confirm_donation(campaign, amount)).pack()

# Fungsi untuk memilih metode E-Money
def choose_emoney(campaign, amount):
    clear_screen()
    tk.Label(window, text="Pilih E-Money").pack()
    tk.Button(window, text="ShopeePay", command=lambda: payment_success(campaign, amount, "ShopeePay", payment_codes['E-Money']['ShopeePay'])).pack()
    tk.Button(window, text="GoPay", command=lambda: payment_success(campaign, amount, "GoPay", payment_codes['E-Money']['GoPay'])).pack()
    tk.Button(window, text="OVO", command=lambda: payment_success(campaign, amount, "OVO", payment_codes['E-Money']['OVO'])).pack()
    tk.Button(window, text="Kembali", command=lambda: process_payment(campaign, amount)).pack()

# Fungsi untuk memilih metode Transfer Bank
def choose_bank_transfer(campaign, amount):
    clear_screen()
    tk.Label(window, text="Pilih Bank").pack()
    tk.Button(window, text="BCA", command=lambda: payment_success(campaign, amount, "BCA", payment_codes['Transfer Bank']['BCA'])).pack()
    tk.Button(window, text="BRI", command=lambda: payment_success(campaign, amount, "BRI", payment_codes['Transfer Bank']['BRI'])).pack()
    tk.Button(window, text="Mandiri", command=lambda: payment_success(campaign, amount, "Mandiri", payment_codes['Transfer Bank']['Mandiri'])).pack()
    tk.Button(window, text="Kembali", command=lambda: process_payment(campaign, amount)).pack()

# Fungsi untuk menampilkan sukses donasi
def payment_success(campaign, amount, method, code):
    clear_screen()
    write_donation(campaign, amount, method, code)
    tk.Label(window, text="Donasi Telah Berhasil").pack()
    tk.Label(window, text=f"Donasi ke {campaign} sebesar {amount} menggunakan {method} berhasil.").pack()
    tk.Label(window, text=f"Kode Pembayaran: {code}").pack()
    tk.Button(window, text="Kembali ke Beranda", command=show_home_page).pack()

# Fungsi untuk menampilkan halaman beranda
def show_home_page():
    clear_screen()
    tk.Label(window, text="Selamat Datang di Beranda!").pack()
    tk.Button(window, text="Donasi", command=show_donation_page).pack()
    tk.Button(window, text="Keluar", command=window.quit).pack()

# Main program
window = tk.Tk()
window.title("Sistem Donasi WeCann")

show_home_page()

window.mainloop()