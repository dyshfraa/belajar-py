# Program Biodata Siswa
print("=" * 35)
print("   FORM BIODATA SISWA")
print("=" * 35)

nama    = input("Nama lengkap       :Anindya Shafira Yasmin ")
kelas   = input("Kelas              :X RPL  ")
umur    = int(input("Umur (tahun)   :17 "))
tinggi  = float(input("Tinggi (cm)  :155 cm "))

print()
print("_" * 35)
print("   DATA TERSIMPAN")
print("=" * 35)
print("Nama  :", nama)
print("Kelas :", kelas)
print("Umur  :", umur, "tahun")
print("Tinggi:", tinggi, "cm")
print("Sudah dewasa:", umur >= 17)