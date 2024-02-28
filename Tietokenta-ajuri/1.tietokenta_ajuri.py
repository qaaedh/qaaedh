import mysql.connector
def haeKentanTiedot(icao):
    sql = "select name, municipality from airport where ident="+icao+"";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kuusori.fetcha()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user= 'root',
    password ='Kkaae1997**',
    autocommit = True
    )

icao = input("Anna haluamasi kentäntn ICAO-koodi")
haeKentanTiedot(icao)