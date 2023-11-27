kuhan_pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if kuhan_pituus < 37:
    puuttuu = 37 - kuhan_pituus
    print("Laske kuha takaisin järveen! Puuttuu", puuttuu, "senttiä alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha ei ole soppi.!")