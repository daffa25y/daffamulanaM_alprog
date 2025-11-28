#  operasi aritmatika x : + -

# operasi penjumlahan 
a = 25
b = 20
hasil = a + b
print(a, "+" , b, "=" , hasil)

#pengurangan 
a = 25
b = 20
hasil = a - b
print(a, "-" , b, "=" , hasil)

#perkalian
a = 25
b = 20
hasil = a * b 
print(a, "*" , b, "=" , hasil)

#pembagian
a = 25
b = 20
hasil = a / b
print(a, "/" , b, "=" , hasil)

#pangkat
a = 25
b = 20
hasil = a ** b
print(a, "**" , b, "=" , hasil)

#modulus
a = 25
b = 20
hasil = a % b
print(a, "%" , b, "=" , hasil)

#floor division
a = 25
b = 20
hasil = a // b
print(a, "//" , b, "=" , hasil)

#buat operasi aritmatika yang menggabungkan semua operasi di atas
a = 25
b = 20
hasil = a + b - a * b / a ** b % b // b
print(a, "+", b, "-", a, "*", b, "/", a, "**", b, "%", b, "//", b, "=" , hasil)


#operasi prioritas
# 1. ()
# 2. pangkat akar
# 3. : x
# 4. + -