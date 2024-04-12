class Hissi:
    def __init__(self, hissi_numero):
        self.hissi_numero = hissi_numero
        self.kerros = 0

    def aja_ylos(self):
        self.kerros += 1

    def aja_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, alin_kerroks, ylim_kerroks, hissien_lukumaara):
        self.hisset = []
        for i in range(hissien_lukumaara):
            self.hisset.append(Hissi(i))
        self.alin_kerroks = alin_kerroks
        self.ylim_kerroks = ylim_kerroks

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        hissi = self.hisset[hissi_numero]
        while hissi.kerros != kohde_kerros:
            if hissi.kerros < kohde_kerros:
                hissi.aja_ylos()
            else:
                hissi.aja_alas()

talon_hisseilla = Talo(0, 10, 2)
#talon_hisseilla.ajaiset_hissiä(0, 5)
#talon_hisseilla.ajaiset_hissiä(1, 3)
print("Hissi 0 on nyt kerroksessa", talon_hisseilla.hisset[0].kerros)
print("Hissi 1 on nyt kerroksessa", talon_hisseilla.hisset[1].kerros)