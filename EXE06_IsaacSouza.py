nome = input('Digite o nome do municipio: ')
Ndep = int(input('Digite o quanto votos o candidato mais votado tem: '))
votos = int(input('Digite quantas pessoas votaram: '))

votosT = votos / 2
if votosT < Ndep:
    print('Não havera 2 turno')

else:
    print('Havera 2 turno')