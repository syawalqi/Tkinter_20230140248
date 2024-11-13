import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Memeriksa setiap input yang dimasukkan, memastikan nilainya valid (antara 0 dan 100)
        for entry in entries:
            nilai = int(entry.get())  # Mengambil nilai dari entry
            if not (0 <= nilai <= 100):  # Mengecek apakah nilai di luar rentang 0 hingga 100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Jika nilai tidak valid, munculkan error
        # Menampilkan hasil prediksi jika semua input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Inisialisasi window utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menentukan judul window
root.geometry("500x600")  # Mengatur ukuran window
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang window

# Label Judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Menampilkan label judul dengan sedikit padding

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")  # Membuat frame untuk menampung input nilai
frame_input.pack(pady=10)  # Memberikan sedikit jarak di sekitar frame

# Membuat input untuk 10 mata pelajaran
entries = []  # List untuk menampung entry (input nilai)
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di grid
    # Membuat entry untuk input nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry di grid
    entries.append(entry)  # Menyimpan entry ke dalam list

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#305fb8", fg="black")
prediksi_button.pack(pady=30)  # Menampilkan tombol dengan padding di sekitarnya

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Menampilkan label hasil prediksi dengan padding di sekitarnya

# Menjalankan aplikasi GUI
root.mainloop()
