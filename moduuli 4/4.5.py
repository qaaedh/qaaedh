import math
from getpass import getpass

def authenticate_customer():
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        username = input("Anna käyttäjätunnus: ")
        password = getpass("Anna salasana: ")

        if username == "python" and password == "rules":
            print("Tervetuloa")
            return create_customer(username)
        else:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
            attempts += 1

    print("Pääsy evätty. Yritä uudelleen myöhemmin.")
    return 