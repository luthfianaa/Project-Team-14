def main_menu():
    while True:
        print("\n--- Main Menu Sistem Donasi WeCan ---")
        print("1. Login")
        print("2. Register")
        print("3. Pilih Donasi")
        print("4. Galang Dana")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            pilih_donasi()
        elif choice == '4':
            galang_dana()
        elif choice == '5':
            print("Terima kasih telah menggunakan Sistem Donasi WeCan.")
            break
        else:
            print("Opsi tidak valid, silakan pilih lagi.")

def login():
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")
    
    if authenticate_user(email, password):
        print("Anda Berhasil Masuk")
        beranda()
    else:
        print("Email dan Password Anda Salah")

def register():
    email = input("Masukkan email: ")
    password1 = input("Masukkan password: ")
    password2 = input("Konfirmasi password: ")
    
    if email_already_registered(email):
        print("Email sudah terdaftar, silakan login")
    elif password1 != password2:
        print("Password1 dan Password2 harus sama")
    else:
        save_new_user(email, password1)
        print("Anda berhasil Registrasi")

def pilih_donasi():
    print("\n--- Halaman Donasi ---")
    kampanye_tersedia = check_kampanye()
    
    if kampanye_tersedia:
        jumlah_donasi = input("Masukkan jumlah donasi: ")
        metode_pembayaran = input("Pilih metode pembayaran (e-money/bank transfer): ")
        if metode_pembayaran == 'e-money':
            kode_bayar = input("Masukkan kode bayar: ")
            konfirmasi_donasi()
        elif metode_pembayaran == 'bank transfer':
            kode_bayar = input("Masukkan kode bayar: ")
            konfirmasi_donasi()
        else:
            print("Metode pembayaran tidak valid.")
    else:
        print("Kampanye Tidak Tersedia")

def galang_dana():
    print("\n--- Halaman Galang Dana ---")
    detail_kampanye = input("Masukkan detail kampanye: ")
    target_dana = input("Masukkan target dana: ")
    durasi_kampanye = input("Masukkan durasi kampanye: ")
    foto_video = input("Unggah foto/video terkait kampanye: ")
    
    save_new_campaign(detail_kampanye, target_dana, durasi_kampanye, foto_video)
    print("Galang dana berhasil dibuat")
    beranda()

def beranda():
    print("\n--- Beranda ---")
    print("1. Pilih Donasi")
    print("2. Galang Dana")
    print("3. Logout")

    choice = input("Pilih opsi (1-3): ")

    if choice == '1':
        pilih_donasi()
    elif choice == '2':
        galang_dana()
    elif choice == '3':
        print("Anda yakin ingin keluar aplikasi?")
    else:
        print("Opsi tidak valid, silakan pilih lagi.")

# Placeholder functions for user authentication and data handling
def authenticate_user(email, password):
    # Implement authentication logic here
    return True

def email_already_registered(email):
    # Check if email is already registered
    return False

def save_new_user(email, password):
    # Save new user to database
    pass

def check_kampanye():
    # Check if there are available campaigns
    return True

def konfirmasi_donasi():
    print("Donasi Telah Berhasil")

def save_new_campaign(detail, target, durasi, foto_video):
    # Save new campaign to database
    pass

if __name__ == "__main__":
    main_menu()
