# Array 
mahasiswa = ["ana", "fuad", "yemima", "tya", "chya"]

# Menampilkan semua nama
print("Daftar Mahasiswa:", mahasiswa)

# Mengakses 
print("Mahasiswa pertama:", mahasiswa[0])

# Menambah data 
mahasiswa.append("hijria")
print("Setelah ditambah:", mahasiswa)

# Menghapus 
mahasiswa.remove("fuad")
print("Setelah fuad dihapus:", mahasiswa)

# Dictionary 
mahasiswa = {
    "nama": "cyntia angreni",
    "nim": "D0425315",
    "jurusan": "Teknik Sistem Informasi",
    "kelas": " A ",
    "angkatan": 2025,
    "alamat": "Mamasa, Sulawesi Barat",

    "nilai": {
        "algoritma_pemrograman": 98,
        "struktur_data": 78,
        "basis_data": 80,
        "pemrograman_python": 90
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan seluruh data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Nilai Python:", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 98
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])

