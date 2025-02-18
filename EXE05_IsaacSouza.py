preço = int(input('Qual o foi o preço do produto: '))

if preço <= 100:
    haddad = (preço * 0.45) + preço
    print('O preço do produto é {}'.format(haddad)) 
else:
    haddad = (preço * 0.35) + preço
    print('O preço do produto é {}'.format(haddad))
print('IsaacSouza')