entrd = input('digite a sequencia: ')

l = 0
n = 0
for i in entrd:
    if i.isalpha():
        l += 1
    if i.isnumeric():
        n +=1
        
print(f'letras: {l} /n digitos: {n}')
