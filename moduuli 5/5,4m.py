kaupungit = []

for i in range(5):
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)