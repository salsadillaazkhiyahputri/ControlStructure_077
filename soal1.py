#Program untuk evaluasi kinerja siswa berdasarkan persentasi 1
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Bellow average performance" 
#function ini digunakan untuk membuat sebuah proses yg mengetahui performa dari siswa menggunakan if
#percentage adalah variabel yg digunakan untuk menyimpan data inputan dari user

#memasukkan persentase siswa
percentage = float(input("Memasukkan nilai n untuk melihat performa dari siswa tersebut: "))
#sebuah inputan yang user akan memasukkan nilai 
print(evaluate_performance(percentage))
#output yang digunakan untuk memanggil function yang telah dibuat