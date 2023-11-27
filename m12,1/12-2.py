import requests
hakusana = input("Anna hakusana: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&lang=FI&appid=2dad8fccc27001a1decd65df6ec0125d"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        S = json_vastaus["weather"][0]["description"]
        K = json_vastaus["main"]["temp"]
        C = K - 273.15
        print(f"Säätila: {hakusana}")
        print(S)
        print(C)
except requests.exceptions.RequestException as e:
    print("haku ei voitu suorittaa")