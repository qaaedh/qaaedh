luku = int(input(' Anna luku '))


on_alkuluku = True
for jakaja in range(2,luku):
    if luku % jakaja == 0:
        on_alkuluku = False
        break

if on_alkuluku:
    print('on alkuluku')
else:
    print('Ei ole alkuluku')