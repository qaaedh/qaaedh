from geopy.distance import geodesic

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

def main():
    auto = Auto("ABC-123", 142)

    print("Rekisteritunnus: ", auto.rekisteritunnus)
    print("Huippunopeus: ", auto.huippunopeus)
    print("Tämänhetkinen nopeus: ", auto.nopeus)
    print("Kuljettu matka: ", auto.kuljettu_matka)

if __name__ == "__main__":
    main()