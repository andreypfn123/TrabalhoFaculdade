area=float(input('Tamanho em metros quadrados da área a ser pintada: '))
valor_tinta=80
cobertura_tinda=3
capacidadeLata=18
litros=area/cobertura_tinda
latas=int(litros/capacidadeLata)
if litros%capacidadeLata != 0 :
    latas+=1
total=latas*valor_tinta
print('Você precisará de {} latas de tinta para pintar o tamanho escolhido.'.format(latas))
print('O valor total é: R$%.2f'%total)