previsoes_tempo = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

dias_ensolarados = []
dias_sem_sol = []

for i, d in enumerate(previsoes_tempo):
    # print(i, d)
    if previsoes_tempo[i] == 'Ensolarado':
        dias_ensolarados.append(dias_semana[i])
    else:
        dias_sem_sol.append(dias_semana[i])

print(f'Dias ensolarados: {dias_ensolarados}')
print(f'Dias sem sol: {dias_sem_sol}')

