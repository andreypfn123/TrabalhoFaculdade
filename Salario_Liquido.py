salario_hora=float(input('Quando ganha por hora? '))
hora_mes=int(input('Horas trabalhadas no mês: '))
salario_bruto=salario_hora*hora_mes
inss=salario_bruto*0.08
sindicato=salario_bruto*0.05
ir=salario_bruto*0.11
salario_liquido=salario_bruto-ir-inss-sindicato
print('+ Salário Bruto: R$%.2f'%salario_bruto)
print('- IR (11%) : R${}'.format('%.2f'%ir))
print('- INSS (8%) : R${}'.format('%.2f'%inss))
print('- Sindicato (5%) : R${}'.format('%.2f'%sindicato))
print('= Salário Líquido: R${}'.format('%.2f'%salario_liquido))