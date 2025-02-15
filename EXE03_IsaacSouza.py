sal = int(input('Digite seu salario: '))
par = int(input('Quantas parcelas voce quer: '))
emp = int(input('Quanto de dinheiro voce quer: '))

taxa = sal * 0.08
if taxa >= emp:
    print('O emprestimo sera concedido') 
else:
    print('Infelizmente o emprestimo não sera concedido')