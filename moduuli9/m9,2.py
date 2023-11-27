class Auto:
    def __init__(self, nimi, nopeus, vari):
        self.nimi = nimi
        self.nopeus = nopeus
        self.vari = vari

    def kiihdytä(self, nopeusmuutos):
        self.nopeus += nopeusmuutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > 120:
            self.nopeus = 120

# Pääohjelma
auto = Auto("BMW", 100, "takka")
print("Auton alkuperäinen nopeus:", auto.nopeus)

auto.kiihdytä(+30)
auto.kiihdytä(+70)
auto.kiihdytä(+50)
print("Auton uusi nopeus:", auto.nopeus)

auto.kiihdytä(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", auto.nopeus)