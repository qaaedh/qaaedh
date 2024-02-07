def tulosta_vuodenaja(kuukausi):
    vuodenajat = {
        (12, 1, 2): "talvi",
        (3, 4, 5): "kevät",
        (6, 7, 8): "kesä",
        (9, 10, 11): "syksy"
    }

    for kuukaudet, vuodenaja in vuodenajat.items():
        if kuukausi in kuukaudet:
            return vuodenaja

    return "Virheellinen kuukauden numero"

def main():
    kuukausi = int(input("Syötä kuukauden numero: "))
    vuodenaja = tulosta_vuodenaja(kuukausi)
    print("Vuodenajan on", vuodenaja)

main()