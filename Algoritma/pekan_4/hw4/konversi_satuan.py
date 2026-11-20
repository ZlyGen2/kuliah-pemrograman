km = float(input("Jarak (km): "))
kg = float(input("Berat (kg): "))
celsius = float(input("Suhu (derajat C): "))

mil = km * 0.621371
pon = kg * 2.20462
fahrenheit = (celsius * 9 / 5) + 32

print(f"{km:.2f} km = {mil:.2f} mil")
print(f"{kg:.2f} kg = {pon:.2f} pon")
print(f"{celsius:.1f} C = {fahrenheit:.1f} F")