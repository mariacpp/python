'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

vlr = float(input('digite o valor da hora: '))
hr = float(input('digite a quantidade de horas trabalhadas no mês: '))

salb = vlr * hr
ir = salb * (11/100)
inss = salb * (8/100)
sind = salb * (5/100)

sall = salb - ir - inss - sind

print(f'+ salario bruto : R$ {salb}\n- IR (11%) : R$ {ir}\n- INSS (8%) : R$ {inss}\n- sindicato (5%) : R$ {sind:.2f}\n= salario liquido : R$ {sall}')
