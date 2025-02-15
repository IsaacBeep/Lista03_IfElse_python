nome = input('Fale o nome do lutador: ')
peso = int(input('Fale o peso do lutador: '))

if peso < 52:
    print('O lutador {} esta na categoria Invalido'.format(nome))

elif peso >= 52 and peso < 65:
    print('O lutador {} esta na categoria Peso Pena'.format(nome))

elif peso >= 65 and peso < 72:
    print('O lutador {} esta na categoria Peso Leve'.format(nome))

elif peso >= 72 and peso < 79:
    print('O lutador {} esta na categoria Peso Ligeiro'.format(nome))

elif peso >= 79 and peso < 86:
    print('O lutador {} esta na categoria Peso Meio-Medio'.format(nome))

elif peso >= 86 and peso < 90:
    print('O lutador {} esta na categoria Peso Peso Medio'.format(nome))

elif peso >= 86 and peso < 100:
    print('O lutador {} esta na categoria Peso Peso Meio-Pesado'.format(nome))

elif peso >= 100:
    print('O lutador {} esta na categoria Peso Peso Peso Pesado'.format(nome))