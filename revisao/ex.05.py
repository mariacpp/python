entrd = input('digite a sequencia: ')

up = 0
low = 0
for i in entrd:
    if i.isupper():
        up += 1
    if i.islower():
        low +=1

print(f'maiúscula: {up} /n minúscula: {low}')
