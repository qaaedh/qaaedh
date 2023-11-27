import random
n=random.randrange(1,10)
Arvaus =int(input('Anna luku: '))
while n!= Arvaus:
    if Arvaus < n:
        print('liian pieni arvaus!')
        Arvaus =int(input('Anna luku taas: '))
    elif Arvaus > n:
        print('liian suuri arvaus!')
        Arvaus = int(input('Anna luku tass.'))

    else:
        break
print('Sinä olet oikkein!!')