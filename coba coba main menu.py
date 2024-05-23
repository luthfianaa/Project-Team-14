import tkinter as tk
from tkinter import messagebox, simpledialog

def main_menu():
    """Menampilkan halaman menu utama wecan"""
    window = tk.Tk()
    window.title("wecan - Menu Utama")
    window.geometry("1200x675")
    window.configure(bg="White")

    label_welcome = tk.Label(window, text="## Selamat datang di wecan! ##")
    label_welcome.pack(pady=20)

    button_bantuan_dana = tk.Button(window, text="1. Memberikan Bantuan Dana", command=lambda: memberikan_bantuan_dana(window))
    button_bantuan_dana.pack(pady=10)

    button_kampanye_dana = tk.Button(window, text="2. Membuat Kampanye Penggalangan Dana", command=lambda: membuat_kampanye_penggalangan_dana(window))
    button_kampanye_dana.pack(pady=10)

    button_keluar = tk.Button(window, text="0. Keluar", command=window.destroy)
    button_keluar.pack(pady=20)

    window.mainloop()

def memberikan_bantuan_dana(parent_window):
    """Menampilkan halaman untuk memberikan bantuan dana"""
    parent_window.withdraw()  # Hide the main window
    window = tk.Toplevel()
    window.title("Memberikan Bantuan Dana")

    label_info = tk.Label(window, text="Silakan pilih campaign yang ingin Anda donasikan.")
    label_info.pack(pady=20)

    # Example list of campaigns
    campaigns = ["Campaign 1", "Campaign 2", "Campaign 3"]
    entry_campaign = tk.Entry(window)
    entry_campaign.pack(pady=5)

    def check_campaign():
        campaign = entry_campaign.get()
        if campaign in campaigns:
            messagebox.showinfo("Donasi", "Kampanye Tersedia")
            choose_donation_amount(campaign, window, parent_window)
        else:
            messagebox.showerror("Donasi", "Kampanye Tidak Tersedia")
            window.deiconify()

    button_check = tk.Button(window, text="Cek Kampanye", command=check_campaign)
    button_check.pack(pady=10)

    button_kembali = tk.Button(window, text="Kembali", command=lambda: kembali_ke_menu_utama(window, parent_window))
    button_kembali.pack(pady=20)

def choose_donation_amount(campaign, current_window, parent_window):
    """Memilih jumlah donasi"""
    current_window.withdraw()
    window = tk.Toplevel()
    window.title("Pilih Jumlah Donasi")

    label_info = tk.Label(window, text=f"Masukkan jumlah donasi untuk {campaign}")
    label_info.pack(pady=20)

    entry_amount = tk.Entry(window)
    entry_amount.pack(pady=5)

    button_proses = tk.Button(window, text="Proses Pembayaran", command=lambda: process_payment(entry_amount.get(), window, parent_window))
    button_proses.pack(pady=10)

def process_payment(amount, current_window, parent_window):
    """Proses pembayaran"""
    current_window.withdraw()
    window = tk.Toplevel()
    window.title("Proses Pembayaran")

    label_info = tk.Label(window, text=f"Pilih metode pembayaran untuk donasi sebesar {amount}")
    label_info.pack(pady=20)

    def choose_payment_method(method):
        if method == "E-Money":
            e_money_payment(window, parent_window)
        else:
            transfer_payment(window, parent_window)

    button_emoney = tk.Button(window, text="E-Money", command=lambda: choose_payment_method("E-Money"))
    button_emoney.pack(pady=10)

    button_transfer = tk.Button(window, text="Transfer", command=lambda: choose_payment_method("Transfer"))
    button_transfer.pack(pady=10)

def e_money_payment(current_window, parent_window):
    """Pembayaran menggunakan e-money"""
    current_window.withdraw()
    window = tk.Toplevel()
    window.title("E-Money Payment")

    label_info = tk.Label(window, text="Masukkan kode bayar E-Money Anda")
    label_info.pack(pady=20)

    entry_code = tk.Entry(window)
    entry_code.pack(pady=5)

    button_confirm = tk.Button(window, text="Konfirmasi Donasi", command=lambda: confirm_donation(window, parent_window))
    button_confirm.pack(pady=10)

def transfer_payment(current_window, parent_window):
    """Pembayaran menggunakan transfer"""
    current_window.withdraw()
    window = tk.Toplevel()
    window.title("Transfer Payment")

    label_info = tk.Label(window, text="Masukkan kode bayar transfer Anda")
    label_info.pack(pady=20)

    entry_code = tk.Entry(window)
    entry_code.pack(pady=5)

    button_confirm = tk.Button(window, text="Konfirmasi Donasi", command=lambda: confirm_donation(window, parent_window))
    button_confirm.pack(pady=10)

def confirm_donation(current_window, parent_window):
    """Konfirmasi donasi"""
    messagebox.showinfo("Donasi", "Donasi Telah Berhasil.")
    kembali_ke_menu_utama(current_window, parent_window)

def membuat_kampanye_penggalangan_dana(parent_window):
    """Menampilkan halaman untuk membuat campaign penggalangan dana"""
    parent_window.withdraw()  # Hide the main window
    window = tk.Toplevel()
    window.title("Membuat Kampanye Penggalangan Dana")

    label_info = tk.Label(window, text="Silakan isi detail campaign baru Anda.")
    label_info.pack(pady=20)

    label_name = tk.Label(window, text="Nama Campaign:")
    label_name.pack(pady=5)
    entry_name = tk.Entry(window)
    entry_name.pack(pady=5)

    label_goal = tk.Label(window, text="Target Donasi:")
    label_goal.pack(pady=5)
    entry_goal = tk.Entry(window)
    entry_goal.pack(pady=5)

    label_duration = tk.Label(window, text="Durasi Kampanye (hari):")
    label_duration.pack(pady=5)
    entry_duration = tk.Entry(window)
    entry_duration.pack(pady=5)

    label_media = tk.Label(window, text="Unggah Foto/Video:")
    label_media.pack(pady=5)
    entry_media = tk.Entry(window)
    entry_media.pack(pady=5)

    button_submit = tk.Button(window, text="Submit", command=lambda: submit_campaign(entry_name.get(), entry_goal.get(), entry_duration.get(), entry_media.get(), window, parent_window))
    button_submit.pack(pady=10)

    button_kembali = tk.Button(window, text="Kembali", command=lambda: kembali_ke_menu_utama(window, parent_window))
    button_kembali.pack(pady=20)

def submit_campaign(name, goal, duration, media, current_window, parent_window):
    """Mengirimkan detail campaign baru"""
    if name and goal and duration and media:
        messagebox.showinfo("Campaign", f"Campaign '{name}' dengan target donasi {goal} telah dibuat! Verifikasi dan publikasi dalam proses.")
        kembali_ke_menu_utama(current_window, parent_window)
    else:
        messagebox.showerror("Error", "Silakan isi semua detail campaign.")

def kembali_ke_menu_utama(current_window, main_window):
    """Kembali ke menu utama"""
    current_window.destroy()  # Close the current window
    main_window.deiconify()  # Show the main window

# Jalankan program
main_menu()