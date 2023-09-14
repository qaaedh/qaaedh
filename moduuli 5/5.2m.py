numerot = []

while True:
    luku = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    if luku == "":
        break
    numerot.append(int(luku))

numerot.sort(reverse=True)
viisi_suurinta = numerot[:5]

print("Viisi suurinta lukua:", viisi_suurinta)