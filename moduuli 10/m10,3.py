class Hissi:
    def __init__(self, alimman_kerros, ylimman_kerros):
        self.alimman_kerros = alimman_kerros
        self.ylimman_kerros = ylimman_kerros
        self.nykyinen = alimman_kerros


    def siirtokerros(self, siirtokerros):
        if siirtokerros < self.alimman_kerros:
            siirtokerros = self.alimman_kerros
        elif siirtokerros > self.ylimman_kerros:
            siirtokerros = self.ylimman_kerros

        elif siirtokerros == self.nykyinen:
            return

        while self.nykyinen > siirtokerros:
              self.alakerros()
        while self.nykyinen < siirtokerros:
              self.yläkerros()
              print(self.nykyinen)
    def alakerros(self):
        if self.nykyinen > self.alimman_kerros:
            self.nykyinen -= 1
            print(self.nykyinen)
    def yläkerros(self):
        if self.nykyinen < self.ylimman_kerros:
           self.nykyinen += 1
           print(self.nykyinen)
class Talo:
    def __init__(self, alimman_kerros, ylimman_kerros, hissi_lukumaara):
        self.alimman_kerros = alimman_kerros
        self.ylimman_kerros = ylimman_kerros
        self.hissit = [Hissi(alimman_kerros, ylimman_kerros) for _ in range(hissi_lukumaara)]

    def aja_hissiä(self, hissin_num, kohdekerros):
        if 0 <= hissin_num < len(self.hissit):
          hissi = self.hissit[hissin_num]
          hissi.siirtokerros(kohdekerros)

        else:
            print(f"Hissiä numero {hissin_num} ei löydy talosta.")


    def palohälytys(self):
        print("palohälytys! Kaikki hissit kutsutaan pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirtokerros(self.alimman_kerros)

talo = Talo(1,10,3)
print("Talo on luotu ja siinä on 3 hissiä.")
talo.aja_hissiä(0,5)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 8)
talo.palohälytys()