area=float(input('Tamanho em metros quadrados da área que deseja pintar: '))
# Tinta
cobertura_tinta=6
consumo_por_litro=area/cobertura_tinta
# Lata
latas_Litros=18
Lata_valor=80

# Galão
galao_tinta=3.6
galao_valor=25

latas_Litros_pintar=area/cobertura_tinta
latas_necessarias=int(latas_Litros_pintar/latas_Litros)
if latas_Litros_pintar%latas_Litros != 0:
    latas_necessarias+=1
valor_final_lata=latas_necessarias*80
print('Se for apenas latas, precisará comprar',latas_necessarias,'latas e custará R$%.2f'%valor_final_lata)

galao_litros_pintar=area/cobertura_tinta
galoes_necessarios=int(galao_litros_pintar/galao_tinta)
if galao_litros_pintar%galao_tinta !=0:
    galoes_necessarios+=1
valor_final_galao=galoes_necessarios*25
print('Se for apenas galões, precisará comprar',galoes_necessarios,'galões e custará R$%.2f'%valor_final_galao)
uasdhasdhu