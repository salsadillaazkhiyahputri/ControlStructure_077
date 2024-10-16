#membuat input masukkan untuk nilai n
n = int(input("Masukkan angka: "))

#pengulangan (loop) untuk membentuk setengabh setengah piramid
for i in range(1, n + 1):
    # range(1, n + 1) menghasilkan angka mulai dari 1 sampai n.
    print((str(i)+ ' ' )* i )  # Mencetak angka i sebanyak i kali dalam satu baris.
# Output ini menciptakan efek piramid dengan menambah jumlah angka di setiap baris.