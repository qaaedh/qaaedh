halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Syötä toisen pizzan hinta (€): "))

yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)

if yksikköhinta1 < yksikköhinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")