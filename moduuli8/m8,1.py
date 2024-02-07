import sqlite3

def hae_lentoaseman_tiedot(icao):
    conn = sqlite3.connect('lentokentatietokanta.db')
    c = conn.cursor()

    c.execute("SELECT name FROM airport WHERE ident=?", (icao,))
    lentoasema = c.fetchone()

    conn.close()

    if lentoasema is not None:
        print("Lentoaseman nimi: " + lentoasema[0])
        print("Sijaintikunta: " + lentoasema[1])
    else:
        print("Lentoasemaa ei löytynyt.")

def main():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    hae_lentoaseman_tiedot(icao)

main()