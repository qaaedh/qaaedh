lentoasemat = {"EFHK" : "helsinki-vantaa lentoasema",
               "EFHF":"helsinki-malmi lentoasema",
               "EFTP":"Tampere lentoasema",
               "EFTU":"Turku lentoasema",
               "EFFO":"forssa lentoasema"}
while True:
    päätös = input("""
uusi lentoasema: 
hakea lentoasema: 
lopeta: 
  """)
    if päätös == "uusi":
      koodi = input("Anna ICAO-koodi: ")
      kenttä = input("Anna lentoasema: ")
      if koodi in lentoasemat:
       print("koodi on jo olemassa. ")
      else:
       lentoasemat[koodi] = kenttä
       print("uusi lentokenttä lisätty!")


    elif päätös == "hakea":
        koodi = input("Anna ICAO-koodi: ")
        if koodi in lentoasemat:
         print(f"ICAO-koodi {koodi} on {lentoasemat[koodi]}")
        if koodi not in lentoasemat:
         print("valitettavasti, koodi ei löytää, yritä uudelleen tai lisää sitä. ")
         päätös = input("""
uusi lentoasema: 
hakea lentoasema: 
lopeta: 
""")
    elif päätös == "lopeta":
        break
    else:
        print("Anteeksi, en ymmärtää mitä haluat, yritä uudelleen")

print("lopettaa")