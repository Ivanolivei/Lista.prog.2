x = float(input('Qual sua altura ? '))
y = int (input('Digite 1 se voce for homem e digite 2 se vc for mulher: '))
if x == 1:
    print(f'Com  altura igua a {x:.2f} seu peso ideal é {(72.7*x)-58}')
elif x == 2:
    print(f'Com  altura igua a {x:.2f} seu peso ideal é {(62.1*x)-44.7}')
else:
    print('Gênero inválido')