'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

v = float(input('digite o valor da hora: '))
h = float(input('digite a quantidade de horas trabalhadas: '))

salb = v*h
percinss = 0

if salb<=1320:
    percinss = 0.075
elif salb>1320 and salb<=2571.29:
    percinss = 0.09
elif salb>2571.29 and salb< 3856.94:
    percinss = 0.12
elif salb>3856.94 and salb<=7507.29:
    percinss = 0.14


if salb<=900:
    IR = 0
    sind = salb * 0.03
    fgts = salb * 0.11
    inss = salb * percinss
    sall = salb - sind - inss
    td = IR + inss
    print(f'Salário Bruto ({v} * {h})\t\t: R$ {salb}')
    print(f'(-) IR \t\t\t\t: ISENTO')
    print(f'(-) INSS (7,5%)\t\t\t\t: R$ {inss}')
    print(f'FGTS (11%)\t\t\t\t: R$ {fgts}')
    print(f'Total de descontos\t\t\t: R$ {td}')
    print(f'Salário Liquido\t\t\t\t: R$ {sall}')

if salb>900 and salb<=1500:
    IR = salb * 0.05
    sind = salb * 0.03
    fgts = salb * 0.11
    inss = salb * percinss
    sall = salb - sind - inss
    td = IR + inss
    print(f'Salário Bruto ({v} * {h})\t\t: R$ {salb}')
    print(f'(-) IR (5%)\t\t\t\t: R$ {IR}')
    print(f'(-) INSS ({percinss*100}%)\t\t\t\t: R$ {inss}')
    print(f'FGTS (11%)\t\t\t\t: R$ {fgts}')
    print(f'Total de descontos\t\t\t: R$ {td}')
    print(f'Salário Liquido\t\t\t\t: R$ {sall}')

elif salb>1500 and salb<=2500:
    IR = salb * 0.10
    sind = salb * 0.03
    fgts = salb * 0.11
    inss = salb * percinss
    sall = salb - sind - inss
    td = IR + inss
    print(f'Salário Bruto ({v} * {h})\t\t: R$ {salb}')
    print(f'(-) IR (10%)\t\t\t\t: R$ {IR}')
    print(f'(-) INSS ({percinss*100}%)\t\t\t\t: R$ {inss}')
    print(f'FGTS (11%)\t\t\t\t: R$ {fgts}')
    print(f'Total de descontos\t\t\t: R$ {td}')
    print(f'Salário Liquido\t\t\t\t: R$ {sall}')

elif salb>2500:
    IR = salb * 0.20
    sind = salb * 0.03
    fgts = salb * 0.11
    inss = salb * percinss
    sall = salb - sind - inss
    td = IR + inss
    print(f'Salário Bruto ({v} * {h})\t\t: R$ {salb}')
    print(f'(-) IR (20%)\t\t\t\t: R$ {IR}')
    print(f'(-) INSS ({percinss*100}%)\t\t\t\t: R$ {inss}')
    print(f'FGTS (11%)\t\t\t\t: R$ {fgts}')
    print(f'Total de descontos\t\t\t: R$ {td}')
    print(f'Salário Liquido\t\t\t\t: R$ {sall}')

