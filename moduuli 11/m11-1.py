class julkasiu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")
class kirja(julkasiu):
    def __init__(self, nimi , kirjoittaja , sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjailija: {self.kirjoittaja}, {self.sivumäärä} sivua. ")
class lehti(julkasiu):
    def __init__(self, nimi, päätoimttaja):
        self.päätoimttaja = päätoimttaja
        super().__init__(nimi)


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja {self.päätoimttaja}")

Julkaisut = []
Julkaisut.append(kirja("Hytti n:o 6", "Rosa Liksom", 200))
Julkaisut.append(lehti("Aku Ankka", "Aki Hyyppä"))
for j in Julkaisut:
    j.tulosta_tiedot()