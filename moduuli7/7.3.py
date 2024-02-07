def lisaa_lentoasema(lentoasemat):
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao] = nimi
    print("Lentoasema lisätty onnistuneesti.")

def hae_lentoasema(lentoasemat):
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    if icao in lentoasemat:
        print("Lentoaseman nimi: " + lentoasemat[icao])
    else:
        print("Lentoasemaa ei löytynyt.")

def main():
    lentoasemat = {}
    while True:
        print("Valitse toiminto:")
        print("1. Lisää uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            lisaa_lentoasema(lentoasemat)
        elif valinta == "2":
            hae_lentoasema(lentoasemat)
        elif valinta == "3":
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

main()