def muunna_galloneiksi(litramäärä):
    return litramäärä / 3.785

while True:
    gallonamäärä = float(input("Syötä bensiinin määrä gallonoina: "))
    if gallonamäärä < 0:
        break
    litramäärä = muunna_galloneiksi(gallonamäärä)
    print("Bensiinin määrä litroina on", litramäärä)

print("Kiitos, että käytit ohjelmaa!")