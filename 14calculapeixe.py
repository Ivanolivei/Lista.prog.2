limite_peso = 50
valor_multa = 4.00
peso = float(input("Digite o peso dos peixes em quilos: "))
if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * valor_multa
else:
    excesso = 0
    multa = 0
print("Peso dos peixes:", peso, "kg")
print("Excesso de peso:", excesso, "kg")
print("Valor da multa a ser pago: R$", multa)