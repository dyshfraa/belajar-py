berat = int(input("Masukkan Berat Badan Anda (kg): "))
tinggi = float(input("Maukkan Tinggi Badan Anda (cm): "))

BMI = berat / (( tinggi/180)**2)

if (BMI < 18.5) :
    kategori = "Kurus (Underweight)"
    keterangan = "Perlu tambah berat badan"
elif (BMI < 24.9) :
    kategori = "Normal (ideal)"
    keterangan = "Pertahankan gaya hidup sehat"
elif (BMI < 29.9) :
    kategori = "Gemuk (Overweight)"
    keterengan = "Perlu olaraga lebih"
else :
    kategori = "Obesitas"
    keterangan = "Konsultasi dokter"

print("Nilai BMI : ", BMI)
print("Kategori  : ", kategori)
print("Keterangan :", keterengan)