import  math

lopeta_toistot = False
suurin = -math.inf

pienin =math.inf

while not lopeta_toistot:
    syota= input('Anna luku tai return =nlopetus:')
    if syota !='':
        uusi_luku = input(syota)
        # suurin=pienin = uusi_luku= int(syoto)

        if uusi_luku > suurin:
            suurin =uusi_luku

        elif uusi_luku < pienin:
            pienin = uusi_luku