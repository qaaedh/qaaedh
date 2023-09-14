lukumaara = int(input("Syötä arpakuutioiden lukumäärä: "))
tulos = 0

for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    tulos += silmaluku