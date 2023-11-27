class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamankentinnopeus = 0
        self.kuljettu_matka = 0

def main():
    auto = Auto("ABC-123", 142)

    print("Rekisteritunnus:", auto.rekisteritunnus)
    print("Huippunopeus:", auto.huippunopeus)
    print("Tämänhetkinen nopeus:", auto.tamankentinnopeus)
    print("Kuljettu matka:", auto.kuljettu_matka)

if __name__ == "__main__":
    main()