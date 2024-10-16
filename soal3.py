#membuat input untuk nilai n
n = int(input("Masukan Angka: "))

#dua angka pertama dari daret fibonacci
a, b= 0, 1
# a akan menyimpan nilai saat ini dalam deret Fibonacci.
# b akan menyimpan nilai berikutnya dalam deret Fibonacci.

#menampilkan deret fibonacci sampai nilai n pada angka yang kita masukkan 
while a <= n:
    print(a, end=" ") # Menggunakan end=" " untuk mencetak angka dalam satu baris dg spasi sebagai pemisah.
    a, b = b, a + b