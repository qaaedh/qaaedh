class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += self.huippunopeus * tuntimaara

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def alusta(self, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def alusta(self, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko

def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.alusta(52.5)
    polttomoottoriauto.alusta(32.3)

    sähköauto.aja(3)
    polttomoottoriauto.aja(3)

    print(f"Sähköauton matkamittari: {sähköauto.matkamittari} km")
    print(f"Polttomoottoriauton matkamittari: {polttomoottoriauto.matkamittari} km")

if __name__ == "__main__":
    main()