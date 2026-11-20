harga_emas = float(input("Harga emas per gram (Rp): "))
penghasilan = float(input("Penghasilan per bulan (Rp): "))
harga_alat = float(input("Harga alat kerja (Rp): "))

nisab_bulan = (85 * harga_emas) / 12
wajib_zakat = penghasilan >= nisab_bulan
zakat = penghasilan * 0.025
ppn = harga_alat * 0.11

print(f"Nisab/bulan : Rp{nisab_bulan:,.0f}")
print(f"Wajib zakat : {wajib_zakat}")
print(f"Zakat       : Rp{zakat:,.0f}")
print(f"PPN alat    : Rp{ppn:,.0f}")
print(f"Total alat  : Rp{harga_alat + ppn:,.0f}")