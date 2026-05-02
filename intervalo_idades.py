while(True):
    idade = int(input('Digite sua idade: '))
    if(idade < 0 or idade > 100):
        break
    else:
        if(idade >= 0 and idade <= 25):
            print(f'A sua idade de {idade} anos, está no intervalo de 0 a 25 anos!')
        elif(idade >= 26 and idade <= 50):
            print(f'A sua idade de {idade} anos, está no intervalo de 26 a 50 anos!')
        elif(idade >= 51 and idade <= 75):
            print(f'A sua idade de {idade} anos, está no intervalo de 51 a 75 anos!')
        else:
            print(f'A sua idade de {idade} anos, está no intervalo de 76 a 100 anos!')

print('Programa encerrado!')
