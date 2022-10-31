senha = input('digite a senha: ')

low = 0
up = 0
simb = 0
num = 0

while True:
    for i in senha:
        if i.islower():
            low += 1
        if i.isupper():
            up += 1
        if i.isnumeric():
            num += 1
        if i in '@#$%&*!':
            simb +=1
    if low >= 1 and up >=1 and num >=1 and simb >= 1 and len(senha) >=6 and len(senha) <= 12:
        True
        print("Senha válida!")
        break
    else:
        print("Senha não cumpre os requisitos!")
        break
