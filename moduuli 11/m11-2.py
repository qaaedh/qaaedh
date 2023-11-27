class Auto:
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus

    def ajamaan(self, aika):
        etaisyys = self.huippunopeus * aika
        print("Ajaa {} minuuttia, matkaa yhteensä {} km.".format(aika, etaisyys))
        return etaisyys

class Sahkoauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        super().__init__(rekisterinumero, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankki):
        super().__init__(rekisterinumero, huippunopeus)
        self.bensatankki = bensatankki

# Pääohjelma
auto_sahko = Sahkoauto("ABC-15", 180, 52.5)
auto_poltto = Polttomoottoriauto("ACD-123", 165, 32.3)

auto_sahko.ajamaan(180)
print()
auto_poltto.ajamaan(180)