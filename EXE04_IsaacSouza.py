nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo (f) para feminino ou (m) para masculino: ')

if sexo == 'f':
    if idade >= 21 and idade <= 34:
        print('Você pode apta para se alistar')
    else:
        print('Voce nao pode se alistar')

elif sexo == 'm':
    if idade >= 18 and idade <= 39:
        print('Você pode apto para se alistar')
    else:
        print('Voce nao pode se alistar')

else:
    print('Identidade invalida')
print("IsaacSouza")