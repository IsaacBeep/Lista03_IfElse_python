inv = input('Digite se voce prefere um investimento de baixa renda (bx) ou alta renda (al): ').lower()

if inv == "bx":
    valor = int(input('Qual o valor que voce deseja fazer esse investimento: '))
    if valor <= 1000:
        print('Recomendamos voce fazer um investimento em poupança')

    else:
        print('Recomendamos voce fazer um investimento em renda fixa')

elif inv == "al":
    valor = int(input('Qual o valor que voce deseja fazer esse investimento: '))
    if valor >= 1000:
        print('Recomendamos voce fazer um investimento em ações')

    else:
        print('Recomendamos voce fazer um investimento em bitcoin')

else:
    print('Valor incorreto')
