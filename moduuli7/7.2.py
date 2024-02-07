def main():
    nimet = set()
    syote = input("Syötä nimi: ")

    while syote != "":
        if syote in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(syote)
        syote = input("Syötä nimi: ")

    print("Syötit seuraavat nimet:")
    for nimi in nimet:
        print(nimi)

main()