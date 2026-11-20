harga = float(input("Harga satuan (Rp): "))
jumlah = int(input("Jumlah barang: "))
diskon_persen = float(input("Diskon (%): "))

subtotal = harga * jumlah                     
potongan = subtotal * (diskon_persen / 100)    
dpp = subtotal - potongan                      
ppn = dpp * (11 / 100)                         
total = dpp + ppn

print(f"Subtotal : Rp{subtotal:,.0f}")
print(f"Diskon   : Rp{potongan:,.0f}")
print(f"PPN 11%  : Rp{ppn:,.0f}")
print(f"Total    : Rp{total:,.0f}")