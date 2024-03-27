import json

import requests

#hakusana = input("Anna hakusana: ")

hakusana='girls'

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls

pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana

print(pyyntö)

vastaus = requests.get(pyyntö).json()

print(hakusana)
print(json.dumps(vastaus,indent=2))
print(vastaus[0]['shwo']['genres'])