
peso=float(input('Qual a quantidade em kg de peixe? '))
excesso=peso-50
multa=excesso*4
if peso >= 51:
    print('O excesso foi de {}kg, então você terá que pagar a multa de: R${}'.format(excesso,multa))
elif peso <= 50:
    print('Você não terá que pagar multa.')