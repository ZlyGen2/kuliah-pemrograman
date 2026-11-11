# meminta input dari pengguna
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi_cm = float(input("Masukkan tinggi badan Anda: "))
berat = float(input("Masukkan berat badan Anda: "))
status = input("Berkerja? (ya/tidak): ")
# menghitung umur tahun depan, tinggi dalam meter, dan indeks massa tubuh (IMT)
umur_tahun_depan = umur + 1
tinggi = tinggi_cm / 100
imt = berat / (tinggi ** 2)
# menentukan status berkerja berdasarkan input pengguna
bekerja = status.lower() in ("ya", "y")   # bool: True atau False
# menampilkan hasil perhitungan
print(f"""
Nama Anda adalah: {nama}
Umur Anda adalah: {umur} tahun
Umur tahun depan Anda adalah: {umur_tahun_depan} tahun
Tinggi badan Anda adalah: {tinggi:.2f} m
Berat badan Anda adalah: {berat:.2f} kg
Indeks Massa Tubuh (IMT) Anda adalah: {imt:.2f}
Status berkerja: {bekerja}""")