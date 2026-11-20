# Kartu 1: Zakat Penghasilan
print("=== Kartu 1: Zakat Penghasilan ===")
penghasilan = 8_500_000
zakat = penghasilan * 0.025
print(f"Zakat: Rp{zakat:,.0f}")

# Kartu 2: PPN 11%
print("\n=== Kartu 2: PPN 11% ===")
harga = 2_400_000
ppn = harga * 0.11
print(f"PPN: Rp{ppn:,.0f}")

# Kartu 3: Diskon
print("\n=== Kartu 3: Diskon ===")
harga, diskon = 200_000, 0.1
bayar = harga - (harga * diskon)
print(f"Bayar: Rp{bayar:,.0f}")

# Kartu 4: Rata-rata 3 Nilai
print("\n=== Kartu 4: Rata-rata 3 Nilai ===")
a, b, c = 80, 70, 90
rata = (a + b + c) / 3
print(f"Rata-rata: {rata:.2f}")

# Kartu 5: Luas Lingkaran
print("\n=== Kartu 5: Luas Lingkaran ===")
import math
r = 7
luas = math.pi * r ** 2
print(f"Luas: {luas:.2f}")
