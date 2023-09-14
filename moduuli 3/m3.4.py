vuosiluku = int(input("Syötä vuosiluku: "))

if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0:
        if vuosiluku % 400 == 0:
            print("Vuosi", vuosiluku, "on karkausvuosi.")
        else:
            print("Vuosi", vuosiluku, "ei ole karkausvuosi.")
    else:
        print("Vuosi", vuosiluku, "on karkausvuosi.")
else:
    print("Vuosi", vuosiluku, "ei ole karkausvuosi.")