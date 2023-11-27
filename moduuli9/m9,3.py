class Auto:
    def __init__(self, nopeus):
        self.nopeus = nopeus
        self.kuljettu_matka = 0

    def kulje(self, tuntimäärä):
        matka_ajalla = self.nopeus * tuntimäärä
        self.kuljettu_matka += matka_ajalla
        return self.kuljettu_matka

auto = Auto(60)
auto.kuljettu_matka = 2000

tunnit = 1.5
kuljetettu_matka = auto.kulje(tunnit)
print(f"Auto kuljetti {kuljetettu_matka} km {tunnit} tunnin ajalla.")