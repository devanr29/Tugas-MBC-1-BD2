print ("\n\n\nKalkulator Energi Kinetik\n\n\n")

def rumuskinetik(m,v):
    kinetik = m*v**2/2
    return kinetik

massa = int (input("Nilai Massa : "))
kecepatan = int (input("Kecepatan : "))

print ("\n\nNilai Energi Kinetik dari data diatas : ", massa, "*", kecepatan, "=", rumuskinetik(massa, kecepatan))