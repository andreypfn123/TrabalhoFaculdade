Tam_arquivo=float(input('Diga o tamanho do arquivo para download em MB: '))
Velocidade_internet=float(input('Diga a velocidade da internet em MBps: '))
tempo_aprox=(Tam_arquivo/Velocidade_internet)*60
print('Tempo aproximado do download é %.0f'%tempo_aprox,'minutos')