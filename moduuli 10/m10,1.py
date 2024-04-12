import random
class Hissi:
    def __init__(self, alimman_kerros, ylimmän_kerros):
        self.alimman = alimman_kerros
        self.ylimmän = ylimmän_kerros
        self.nykyinen_kerros = alimman_kerros

    def siirrykrrokseen(self, siirtokerros):
        if siirtokerros < self.alimman:
            siirtokerros = self.alimman
        elif siirtokerros > self.ylimmän:
            siirtokerros = self.ylimmän

        while self.nykyinen_kerros > siirtokerros:
            self.kerros_alas()
        while self.nykyinen_kerros < siirtokerros:
            self.kerros_ylös()


    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylimmän:
            self.nykyinen_kerros += 1
            print(f"Hissi siirtyy kerrokseen {self.nykyinen_kerros}")
    def kerros_alas(self):
        if self.nykyinen_kerros > self.alimman:
            self.nykyinen_kerros -= 1
            print(f"Hissi siirtyy kerrokseen {self.nykyinen_kerros}")


hissi = Hissi(1, 10)
print("Hissi on alimmassa kerroksessa.")
hissi.siirrykrrokseen(3)
print(f"Hissi on {hissi.nykyinen_kerros} kerroksessa.")