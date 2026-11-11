uang = 1_800_000
uang2 = 2_500_000
uang3 = 3_600_000
uang4 = 4_000_000
uang5 = 150_000

print("5 Temuan")
print("- Rp", uang)
print("""otomatis menambah spasi di antara Rp dan angka, 
sedangkan f-string tidak, jadi spasinya harus kita atur sendiri.""")

print(f"""
- Rp{uang2:,} Menambahkan tanda koma sebagai pemisah ribuan
- Rp{uang3:.0f} Menampilkan 0 angka di belakang koma
- Rp{uang4:.2f} Menampilkan 2 angka di belakang koma
- Rp{uang5:>8} Menambahkan spasi di depan angka agar rata kanan""")
