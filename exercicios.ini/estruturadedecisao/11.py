'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até R$ 280,00 (incluindo) : aumento de 20%
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.'''

sal = float(input('digite o salário: R$ '))
print()
if sal<=280:
    perc = sal*0.20
    nvsal = sal + perc
    print(f'salário: R${sal}')
    print('percentual de aumento: 20%')
    print(f'valor do aumento: R${perc}')
    print(f'novo salário: R$ {nvsal}')
elif sal>280 and sal<700:
    perc = sal*0.15
    nvsal = sal + perc
    print(f'salário: R${sal}')
    print('percentual de aumento: 15%')
    print(f'valor do aumento: R${perc}')
    print(f'novo salário: R$ {nvsal}')
elif sal>700 and sal<1500:
    perc = sal*0.10
    nvsal = sal + perc
    print(f'salário: R${sal}')
    print('percentual de aumento: 10%')
    print(f'valor do aumento: R${perc}')
    print(f'novo salário: R$ {nvsal}')
elif sal>1500:
    perc = sal*0.05
    nvsal = sal + perc
    print(f'salário: R${sal}')
    print('percentual de aumento: 5%')
    print(f'valor do aumento: R${perc}')
    print(f'novo salário: R$ {nvsal}')
