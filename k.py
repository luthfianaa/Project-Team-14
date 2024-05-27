import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# Inisialisasi file CSV
def init_csv():
    if not os.path.exists('donasi_wecan.csv'):
        with open('donasi_wecan.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['jumlah', 'metode', 'kode_bayar'])

    if not os.path.exists('kampanye_wecan.csv'):
        with open('kampanye_wecan.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['detail', 'target', 'durasi', 'foto'])

def main_menu():
    root = tk.Tk()
    root.title("Sistem Donasi WeCan")

    def pilih_donasi():
        donasi_window = tk.Toplevel(root)
        donasi_window.title("Pilih Donasi")
        
        tk.Label(donasi_window, text="Masukkan jumlah donasi:").grid(row=0, column=0)
        donasi_entry = tk.Entry(donasi_window)
        donasi_entry.grid(row=0, column=1)
        
        tk.Label(donasi_window, text="Pilih metode pembayaran (e-money/bank transfer):").grid(row=1, column=0)
        metode_pembayaran_entry = tk.Entry(donasi_window)
        metode_pembayaran_entry.grid(row=1, column=1)
        
        def proses_donasi():
            jumlah_donasi = donasi_entry.get()
            metode_pembayaran = metode_pembayaran_entry.get()
            if metode_pembayaran in ['e-money', 'bank transfer']:
                kode_bayar = simpledialog.askstring("Kode Bayar", "Masukkan kode bayar:")
                if kode_bayar:
                    save_donasi(jumlah_donasi, metode_pembayaran, kode_bayar)
                    messagebox.showinfo("Donasi", "Donasi Telah Berhasil")
                    donasi_window.destroy()
            else:
                messagebox.showerror("Donasi", "Metode pembayaran tidak valid.")
        
        tk.Button(donasi_window, text="Donasi", command=proses_donasi).grid(row=2, columnspan=2)

    def galang_dana():
        galang_dana_window = tk.Toplevel(root)
        galang_dana_window.title("Galang Dana")
        
        tk.Label(galang_dana_window, text="Detail Kampanye:").grid(row=0, column=0)
        tk.Label(galang_dana_window, text="Target Dana:").grid(row=1, column=0)
        tk.Label(galang_dana_window, text="Durasi Kampanye:").grid(row=2, column=0)
        tk.Label(galang_dana_window, text="Unggah Foto/Video:").grid(row=3, column=0)
        
        detail_entry = tk.Entry(galang_dana_window)
        target_entry = tk.Entry(galang_dana_window)
        durasi_entry = tk.Entry(galang_dana_window)
        foto_entry = tk.Entry(galang_dana_window)
        
        detail_entry.grid(row=0, column=1)
        target_entry.grid(row=1, column=1)
        durasi_entry.grid(row=2, column=1)
        foto_entry.grid(row=3, column=1)
        
        def simpan_galang_dana():
            detail = detail_entry.get()
            target = target_entry.get()
            durasi = durasi_entry.get()
            foto = foto_entry.get()
            save_kampanye(detail, target, durasi, foto)
            messagebox.showinfo("Galang Dana", "Galang dana berhasil dibuat")
            galang_dana_window.destroy()
        
        tk.Button(galang_dana_window, text="Galang Dana", command=simpan_galang_dana).grid(row=4, columnspan=2)

    tk.Label(root, text="Sistem Donasi WeCan").pack(pady=10)
    tk.Button(root, text="Pilih Donasi", command=pilih_donasi).pack(pady=5)
    tk.Button(root, text="Galang Dana", command=galang_dana).pack(pady=5)
    tk.Button(root, text="Keluar", command=root.quit).pack(pady=5)

    root.mainloop()

def save_donasi(jumlah, metode, kode_bayar):
    with open('donasi_wecan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jumlah, metode, kode_bayar])

def save_kampanye(detail, target, durasi, foto):
    with open('kampanye_wecan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([detail, target, durasi, foto])

if __name__ == "__main__":
    init_csv()
    main_menu()
