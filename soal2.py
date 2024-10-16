num1 = float(input("Enter the first number: "))  #Meminta input angka pertama dan mengubahnya menjadi float
num2 = float(input("Enter the second number: ")) #Meminta input angka kedua dan mengubahnya menjadi float
num3 = float(input("Enter the third number: "))  #Meminta input angka ketiga dan mengubahnya menjadi float

# Jika num1 lebih besar atau sama dengan num2 dan num3
if num1 >= num2 and num1 >= num3:
    largest = num1    
elif num2 >= num1 and num2 >= num3:
    largest = num2    
else:
    largest = num3  

print ("The largest number is:", largest) # Mencetak angka terbesar