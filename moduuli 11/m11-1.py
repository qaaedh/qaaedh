class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Julkaisun nimi:", self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumäärä)

class Lehti(Julkaisu):
    def __init__(self, nimi, paa_toimittaja):
        super().__init__(nimi)
        self.paa_toimittaja = paa_toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Päätoimittaja:", self.paa_toimittaja)

# Pääohjelma
aku_ankka = Kirja("Aku Ankka", "Aki Hyyppä", 200)
hytti_n6 = Lehti("Hytti n:o 6", "Rosa Liksom")

aku_ankka.tulosta_tiedot()
print()
hytti_n6.tulosta_tiedot()