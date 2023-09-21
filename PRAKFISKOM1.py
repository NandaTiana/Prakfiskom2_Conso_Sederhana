# Konstanta
m = 0.1  # Massa benda dalam kg
h1 = 2  # Jarak yang ditempuh benda dalam pasir dalam meter
s = -0.02 # Jarak pasir sebelum berhenti
h2 = 0 # Dasar
g = 10 # dalam satuan meter per sekon kuadrat

#perubahan tenaga potensial sama dengan kerja benda masuk ke pasir.
#dari rumus ini W = - delta Ep di dapatkan rumus F = -m.g(h2-h1)/s

# Menghitung gaya yang dilakukan pasir
F = -m*g*(h2-h1)/s

# Menampilkan hasil
print(f"Besar gaya rata-rata yang dilakukan pasir untuk menghambat benda adalah {F} Newton")
print ("Gaya bernilai negatif artinya gaya penghambat berlawanan arah dengan arah gerak benda.")
print ("Referensi : TWIN MASTER outlines FISIKA")
