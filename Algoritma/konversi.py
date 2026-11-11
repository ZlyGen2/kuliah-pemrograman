print("""
==========================
    Kuis Sederhana
==========================""")

kuis = [
    # soal-soal kuis
    {
        "soal": "1. Presiden Indonesia sekarang adalah Prabowo?", # str
        "jawaban": "Benar" # str
    },
    {
        "soal": "2. Ibukota Indonesia adalah Bandung?",
        "jawaban": "Salah"
    },
    {
        "soal": "3. Bahasa resmi Indonesia adalah Bahasa Indonesia!",
        "jawaban": "Benar"
    },
    {
        "soal": "4. Indonesia memiliki 34 provinsi?",
        "jawaban": "Benar"
    },
    {
        "soal": "5. Indonesia berada di benua africa?",
        "jawaban": "Salah"
    }
]

nyawa = 3 # 1. atur nyawa ke 3
skor = 0 # atur skor ke 0
benar = 0 # atur benar ke 0
salah = 0 # atur salah ke 0

for i in range(5): # 2. ulangi 5 kali (perulangan)
    
    jawaban = input(kuis[i]["soal"] + " ").lower() # 3. tanya ... dan tunggu
    if jawaban == kuis[i]["jawaban"].lower(): # 4. jika ... jika tidak
        skor += 20 # ubah skor sebesar 20
        benar += 1 # ubah benar sebesar 1
        print("Jawaban kamu benar!") # 5. katakan (output)
    else:
        skor -= 30 # ubah skor sebesar -30
        salah += 1 # ubah salah sebesar 1
        nyawa -= 1 # ubah nyawa sebesar -1
        print("Jawaban kamu salah!")
# hasil akhir
print(f"""
==========================
    Hasil Kuis
==========================
Skor: {skor}
Nyawa tersisa: {nyawa}
Jumlah Jawaban Benar: {benar}
Jumlah Jawaban Salah: {salah}""")