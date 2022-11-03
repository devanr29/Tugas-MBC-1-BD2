print ("\n\n\nKalkulator Energi Kinetik\n\n\n")
def rumuskinetik(m,v):
    kinetik = m*v**2/2
    return kinetik

massa = int (input("Nilai Massa : "))
kecepatan = int (input("Kecepatan : "))

print ("\n\nNilai Energi Kinetik dari data diatas : ", massa, "*", kecepatan, "=", rumuskinetik(massa, kecepatan))

print ("\n\n\nKalkulator Energi Potensial\n\n\n")
def rumuspotensial(m,g,h):
    potensial = m*g*h
    return potensial
massa = int (input("Nilai Massa : "))
gravitasi = 10
tinggi = int (input("Ketinggian : "))
print ("Nilai Energi Potensial dari data diatas : ", massa, "", gravitasi, "", tinggi, "=", rumuspotensial(massa, gravitasi, tinggi))

print("\n\n\nKalkulator Energi Mekanik \n\n\n")
def rumusmekanik(rumuskinetik,rumuspotensial):
    mekanik = rumuskinetik+rumuspotensial
    return mekanik
print ("\n\nNilai Energi Mekanik dari data diatas adalah gi", rumusmekanik(rumuskinetik,rumuspotensial))