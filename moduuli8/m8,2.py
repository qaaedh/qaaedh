import requests

def hae_lentokenttien_lukumaarat(maakoodi):
    url = f"https://api.openaip.net/v1/airports?countrycode={maakoodi}"
    response = requests.get(url)

    if response.status_code == 200:
        lentokentat = response.json()
        lentokenttien_lukumaarat = {}

        for lentokentta in lentokentat:
            tyyppi = lentokentta["type"]
            if tyyppi in lentokenttien_lukumaarat:
                lentokenttien_lukumaarat[tyyppi] += 1
            else:
                lentokenttien_lukumaarat[tyyppi] = 1

        for tyyppi, lukumaara in lentokenttien_lukumaarat.items():
            print(f"{tyyppi}: {lukumaara} kappaletta")
    else:
        print("Virhe lentokenttätietojen haussa.")

def main():
    maakoodi = input("Syötä maakoodi: ")
    hae_lentokenttien_lukumaarat(maakoodi)

main()