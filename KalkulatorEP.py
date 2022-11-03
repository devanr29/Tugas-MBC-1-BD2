print ("\n\n\nKalkulator Energi Potensial\n\n\n")

def rumuspotensial(m,g,h):
    potensial = m*g*h
    return potensial

massa = int (input("Nilai Massa : "))
gravitasi = 10
tinggi = int (input("Ketinggian : "))

print ("Nilai Energi Potensial dari data diatas : ", massa, "", gravitasi, "", tinggi, "=", rumuspotensial(massa, gravitasi, tinggi))