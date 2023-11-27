import random

def heita_noppaa(tahkojen_maara):
    tulos = 0
    while True:
        silmaluku = random.randint(1, tahkojen_maara)
        print("Heitit", tahkojen_maara, "-tahkoista noppaa ja sait silmäluvun", silmaluku)
        if silmaluku == tahkojen_maara:
            break
        tulos += silmaluku
    return tulos

maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))
tulos = heita_noppaa(maksimisilmaluku)
print("Nopan maksimisilmäluku saavutettiin! Silmälukujen summa oli", tulos)