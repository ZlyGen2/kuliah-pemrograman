print("""
==========================
    Nilai Rata-rata
==========================
""")

nilai_tugas = float(input("Masukkan nilai tugas Anda: "))
nilai_uts = float(input("Masukkan nilai UTS Anda: "))
nilai_uas = float(input("Masukkan nilai UAS Anda: "))

rata_nilai = (nilai_tugas + nilai_uts + nilai_uas) / 3

print(f"""
    Hasil Perhitungan
==========================

Nilai Tugas: {nilai_tugas}
Nilai UTS: {nilai_uts}
Nilai UAS: {nilai_uas}
Rata-rata Nilai: {rata_nilai:.1f}
""")