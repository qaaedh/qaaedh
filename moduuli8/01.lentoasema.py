






import mysql.connector
def get_airport_by_icao(icao):
    sql ='SELECT name,municipality FROM airport WHERE ident ="EFHK;"'
    print(sql)
    cursor=db_connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone
    print(result)
    return
db_connection= mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='12345',
         autocommit=True
         )
icao= input('Anna ICAO-Koodi:')

airport= get_airport_by_icao(icao)
print(airport)
def main():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    print(icao)
main()