
def ambil_daftar_kampanye():
    # Di sini Anda dapat menambahkan logika untuk mengambil daftar kampanye
    # dari server Kitabisa menggunakan API atau dari database lokal.
    daftar_kampanye = [
        {"id": 1, "judul": "Bantuan Kemanusiaan untuk Korban Banjir"},
        {"id": 2, "judul": "Penyediaan Pendidikan bagi Anak Miskin"},
        {"id": 3, "judul": "Penghijauan Lingkungan Sekitar"},
    ]
    return daftar_kampanye

def ambil_detail_kampanye(id_kampanye):
    # Di sini Anda dapat menambahkan logika untuk mengambil detail kampanye
    # berdasarkan ID dari server Kitabisa menggunakan API atau dari database lokal.
    detail_kampanye = {
        "id": id_kampanye,
        "judul": "Bantuan Kemanusiaan untuk Korban Banjir",
        "deskripsi": "Kami mengumpulkan dana untuk membantu korban banjir di daerah terdampak.",
        "target": 10000000,
        "terkumpul": 5000000,
    }
    return detail_kampanye
