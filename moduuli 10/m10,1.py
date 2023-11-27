class Hissi:
    def __init__(self, alin_kerroks, ylim_kerroks):
        self.alin_kerroks = alin_kerroks
        self.ylim_kerroks = ylim_kerroks
        self.kerroks = alin_kerroks

    def siirry_kerrokseen(self, kerrok):
        if kerrok > self.ylim_kerroks or kerrok < self.alin_kerroks:
            return "Sisäänpitämätön kerroksen numero."
        while self.kerroks != kerrok:
            if self.kerroks < kerrok:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.kerroks < self.ylim_kerroks:
            self.kerroks += 1
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.kerroks > self.alin_kerroks:
            self.kerroks -= 1
        else:
            print("Hissi on jo alimmaisessa kerroksessa.")

h = Hissi(0, 10)
h.siirry_kerrokseen(5)
print("Hissi on nyt", h.kerroks, "kerroksessa.")
h.siirry_kerrokseen(0)
print("Hissi on nyt", h.kerroks, "kerroksessa.")