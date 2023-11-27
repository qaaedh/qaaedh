
def karsi_parittomat(lista):
    uusi_lista = [luku for luku in lista if luku % 2 == 0]
    return uusi_lista

alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu_lista = karsi_parittomat(alkuperäinen_lista)

print("Alkuperäinen lista:", alkuperäinen_lista)
print("Karsittu lista:", karsittu_lista)