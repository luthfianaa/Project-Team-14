import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os
from PIL import ImageTk, Image

campaigns_file = 'campaigns.csv'

def write_campaign(title, target, duration, image):
    is_new_file = not os.path.exists(campaigns_file)
    with open(campaigns_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(['title', 'target', 'duration', 'image'])
        writer.writerow([title, target, duration, image])

def clear_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

def show_fundraising_page(window):
    clear_screen(window)
    tk.Label(window, text="Halaman Galang Dana").pack()
    tk.Label(window, text="Masukkan Detail Kampanye Baru").pack()
    
    tk.Label(window, text="Judul Kampanye:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()

    tk.Label(window, text="Keterangan Kampanye:").pack()
    description_entry = tk.Entry(window)
    description_entry.pack()
    
    tk.Label(window, text="Target Donasi:").pack()
    target_entry = tk.Entry(window)
    target_entry.pack()
    
    tk.Label(window, text="Durasi (hari):").pack()
    duration_entry = tk.Entry(window)
    duration_entry.pack()
    
    tk.Label(window, text="Pilih Foto Kampanye:").pack()
    image_path_entry = tk.Entry(window, state='readonly')
    image_path_entry.pack()
    
    tk.Button(window, text="Browse", command=lambda: select_image(window, image_path_entry)).pack()
    
    tk.Button(window, text="Simpan Kampanye", command=lambda: save_campaign(window, title_entry.get(), target_entry.get(), duration_entry.get(), image_path_entry.get())).pack()
    tk.Button(window, text="Kembali", command=lambda: show_main_page(window)).pack()

def select_image(window, entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.insert(0, file_path)
    entry.config(state='readonly')

def save_campaign(window, title, target, duration, image):
    if title and target and duration and image:
        write_campaign(title, target, duration, image)
        clear_screen(window)
        tk.Label(window, text="Kampanye Baru Telah Berhasil Disimpan").pack()
        tk.Button(window, text="Kembali ke Beranda", command=lambda: show_main_page(window)).pack()
    else:
        messagebox.showerror("Galang Dana", "Semua field harus diisi!")

def show_main_page(window):
    import donasi
    donasi.show_main_page(window)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Sistem Galang Dana WeCann")

    show_fundraising_page(window)

    window.mainloop()
