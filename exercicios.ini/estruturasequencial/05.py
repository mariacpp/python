metro = float(input('digite o comprimento(m) para conversão: '))

con = metro * 100

if metro <2:
    print(f'{metro} metro em centimentos são: {con} cm')
else:
    print(f'{metro} metros em centimentos são: {con} cm')