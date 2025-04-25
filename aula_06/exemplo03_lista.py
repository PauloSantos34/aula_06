
previsoes_tempo = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade' , 'Ensolarado']
print(previsoes_tempo)

PREVISAO_FELIZ = 'Ensolarado'

for previsao in previsoes_tempo:
    print(previsao)
    if previsao == PREVISAO_FELIZ:
        print(f'Aproveite para passear, previsao {previsao}')
    else:
        print(f'Leve o guarda chuva, previsao {previsao}')
