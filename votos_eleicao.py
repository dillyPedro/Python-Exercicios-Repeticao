total_candidatos = 4
total_votos = 20

contador, contador_1, contador_2, contador_3, contador_4, contador_5, contador_6 = 0

for contador in range(0, 20):
    voto = int(input('Digite o seu voto [1, 2, 3 ou 4]: '))

    while(voto < 1 or voto > 6):
        print('Voto inválido. Tente denovo!')
        voto = int(input('Digite o seu voto [1, 2, 3 ou 4]: '))
    
    if(voto == 1):
        contador_1 += 1
    elif(voto == 2):
        contador_2 += 1
    elif(voto == 3):
        contador_3 += 1
    elif(voto == 4):
        contador_4 += 1
    elif(voto == 5):
        contador_5 += 1
    else:
        contador_6 += 1

print('\n-------------------------------------------')
print('              TOTAL DE VOTOS               ')
print('-------------------------------------------')

print(f'\nCandidato 1 = {contador_1} / Porcentagem = {contador_1 / 20}%')
print(f'Candidato 2 = {contador_2} / Porcentagem = {contador_2 / 20}%')
print(f'Candidato 3 = {contador_3} / Porcentagem = {contador_3 / 20}%')
print(f'Candidato 4 = {contador_4} / Porcentagem = {contador_4 / 20}%')
print(f'Votos nulos = {contador_5} / Porcentagem = {contador_5 / 20}%')
print(f'Votos em branco = {contador_6} / Porcentagem = {contador_6 / 20}%')
