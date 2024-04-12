class Hissi:
    def __init__(self, alimmän_kerros, ylimmän_kerros):
        self.alimmän_kerros = alimmän_kerros
        self.ylimmän_kerros = ylimmän_kerros
        self.nykyinen = alimmän_kerros

    def siirtokerros(self, siirto_kerros):
        if siirto_kerros < self.alimmän_kerros:
            siirto_kerros = self.alimmän_kerros
        elif siirto_kerros > self.ylimmän_kerros:
            siirto_kerros = self.ylimmän_kerros

        elif siirto_kerros == self.nykyinen:
            return


        while self.nykyinen > siirto_kerros:
            self.alaskerros()
        while self.nykyinen < siirto_kerros:
            self.yläkerros()
        print(f"Hissi siirtyi kerrokseen {self.nykyinen}")


    def alaskerros(self):
        if self.nykyinen > self.alimmän_kerros:
           self.nykyinen -= 1
           print(f'Hissi siirtyi kerrokseen {self.nykyinen}')
    def yläkerros(self):
        if self.nykyinen < self.ylimmän_kerros:
           self.nykyinen += 1
           print(f'Hissi siirtyi kerrokseen {self.nykyinen}')

class Talo:
    def __init__(self, alimmän_kerros, ylimmän_kerros, hissi_lukumäärä):
        self.alimmän = alimmän_kerros
        self.ylimmän = ylimmän_kerros
        self.hissit = [Hissi(alimmän_kerros, ylimmän_kerros) for _ in range(hissi_lukumäärä)]

    def aja_hissiä(self, hissin_num, kohdekerros):
        if 0 <= hissin_num < len(self.hissit):
            hissi = self.hissit[hissin_num]
            hissi.siirtokerros(kohdekerros)
        else:
            print(f"Hissiä numero {hissin_num} ei löydy talosta")


if __name__ == "__main__":
    talo = Talo(1, 10, 3)

    print("Talo on luotu ja siinä on 3 hissiä.")
    talo.aja_hissiä(0, 5)
    talo.aja_hissiä(1, 3)
    talo.aja_hissiä(2, 8)